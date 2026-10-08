#!/usr/bin/env python3
"""Generate images with the OpenAI Images API (stdlib only, no pip install needed).

Text-to-image:
    python3 generate.py --prompt "..." --out ./out/name.png

Style-anchored (passes reference images to /v1/images/edits so the model
can copy the look, not just read a description of it):
    python3 generate.py --prompt "..." --ref a.png --ref b.png --out ./out/name.png

Long prompts: write them to a file and pass --prompt-file prompt.txt instead of --prompt.
--dry-run prints the request without calling the API.

Env: OPENAI_API_KEY (required), OPENAI_BASE_URL (optional, default https://api.openai.com/v1),
     OPENAI_IMAGE_MODEL (optional, default gpt-image-1).
"""
import argparse
import base64
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path


def post_json(url, key, payload):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    return send(req)


def post_multipart(url, key, fields, files):
    boundary = uuid.uuid4().hex
    body = bytearray()
    for name, value in fields.items():
        body += f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n{value}\r\n".encode()
    for name, path in files:
        mime = mimetypes.guess_type(path)[0] or "image/png"
        body += (
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"; "
            f"filename=\"{Path(path).name}\"\r\nContent-Type: {mime}\r\n\r\n"
        ).encode()
        body += Path(path).read_bytes() + b"\r\n"
    body += f"--{boundary}--\r\n".encode()
    req = urllib.request.Request(
        url,
        data=bytes(body),
        headers={"Authorization": f"Bearer {key}", "Content-Type": f"multipart/form-data; boundary={boundary}"},
    )
    return send(req)


def send(req):
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"OpenAI API error {e.code}: {e.read().decode(errors='replace')}")


def main():
    p = argparse.ArgumentParser()
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--prompt")
    src.add_argument("--prompt-file", help="read the prompt from a UTF-8 text file")
    p.add_argument("--out", required=True, help="output path; with --n > 1, _1/_2 suffixes are added")
    p.add_argument("--ref", action="append", default=[], help="style reference image (repeatable, max 16)")
    p.add_argument("--size", default="1024x1536", help="1024x1024 | 1536x1024 | 1024x1536 | auto")
    p.add_argument("--quality", default="high", help="low | medium | high | auto")
    p.add_argument("--n", type=int, default=1)
    p.add_argument("--model", default=os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-1"))
    p.add_argument("--dry-run", action="store_true", help="print the request and exit")
    a = p.parse_args()
    prompt = a.prompt if a.prompt is not None else Path(a.prompt_file).read_text(encoding="utf-8").strip()

    missing = [r for r in a.ref if not Path(r).is_file()]
    if missing:
        sys.exit(f"reference image not found: {missing}")
    if a.dry_run:
        endpoint = "images/edits" if a.ref else "images/generations"
        print(json.dumps({"endpoint": endpoint, "model": a.model, "size": a.size, "quality": a.quality,
                          "n": a.n, "refs": a.ref[:16], "prompt_chars": len(prompt), "prompt": prompt},
                         ensure_ascii=False, indent=2))
        return

    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        sys.exit("OPENAI_API_KEY is not set. Export it in your shell profile, e.g. export OPENAI_API_KEY=sk-...")
    base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")

    common = {"model": a.model, "prompt": prompt, "size": a.size, "quality": a.quality, "n": a.n}
    if a.ref:
        data = post_multipart(f"{base}/images/edits", key, {k: str(v) for k, v in common.items()},
                              [("image[]", r) for r in a.ref[:16]])
    else:
        data = post_json(f"{base}/images/generations", key, common)

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    for i, item in enumerate(data.get("data", []), 1):
        path = out if a.n == 1 else out.with_name(f"{out.stem}_{i}{out.suffix}")
        if item.get("b64_json"):
            path.write_bytes(base64.b64decode(item["b64_json"]))
        elif item.get("url"):
            urllib.request.urlretrieve(item["url"], path)
        print(path)


if __name__ == "__main__":
    main()
