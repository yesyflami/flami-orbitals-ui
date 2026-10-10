---
name: flami-orbitals-ui
description: Turn a photo or a described subject into a "轨道双子星 / Orbitals" game-screen illustration — late-1980s Japanese cel-anime characters, painted sci-fi backgrounds, faded film grain, plus the game's typography (giant white Japanese chapter titles, manga onomatopoeia, yellow dialogue subtitles, quest HUD, portrait cards) — and generate it with the built-in image tool or the OpenAI Images API. Use this whenever the user mentions 轨道双子星, Orbitals, オービタルズ, or asks for an 80s/昭和 anime, retro cel-anime, 复古赛璐璐, 老动画, or "game screenshot" style image of a person, pet, object or scene, even if they don't name the game. It enriches the composition with story elements, not just a style filter.
---

# flami-orbitals-ui — 轨道双子星 (Orbitals) image skill

All paths below are relative to the directory containing this SKILL.md (call it `SKILL_DIR`).

Make one image that looks like **a captured moment from the game *Orbitals*, starring the user's subject**. Two things must both happen:

1. **Style** — redraw the subject in the game's 80s cel-anime look, with its palette, film surface and typography.
2. **Composition** — don't just restyle the source. Build a layered game frame around the subject: chapter title or onomatopoeia, dialogue, HUD, portrait inset, FX, and new world elements that extend the subject into the game's universe.

Reference files (read both before writing a prompt):
- `references/style-guide.md` — rendering, palettes (scene moods), typography, film surface, and a ready-made English style block.
- `references/composition.md` — layer stack, scene concept, 6 layout archetypes, variation axes, preflight checklist.

## Workflow

### Accepted visual defaults

Use rich, unequal overlapping game-interface panels over a quiet background. Depth should come from scale, occlusion and partial-feature close-ups, not dense environmental detail. Keep the Orbitals cel-anime style; borrow only the composition principles of retro interface illustrations, not their pixel-art treatment, desktop menus or signatures. This skill is self-contained and does not require another skill.

Bottom dialogue and speaker labels default to natural Japanese; keep user-supplied text verbatim and follow an explicitly requested language instead. This default applies to dialogue, not automatically to every HUD or title.

### 1. Read the request

Find:
- **Subject**: an image path / attached image, or a text description. If there is neither, ask once what the image should be about, then stop.
- **Optional user choices**: mood (红幕菜单 / 深空极光 / 遗迹森林 / 熔炉 / 金色漩涡 / 跃迁霓虹 / 控制室), layout (章节标题卡 / 角色切入 / 道具获得 / 双人分屏 / 主菜单 / 对话特写), aspect ratio, any title or dialogue text. Use whatever is given verbatim; pick the rest yourself — don't send the user a questionnaire, choosing is part of the job.

Aspect ratio → `--size`: landscape (default, matches the game's 16:9 screens) `1536x1024`; portrait / 9:16 / 3:4 / phone wallpaper `1024x1536`; square `1024x1024`.

### 2. Anchor the subject

If there is a source image, look at it once and note **3–5 identity anchors per subject**: hair shape and colour, glasses/accessories, signature clothing colour, body type, pose or relationship between subjects. These anchors are what make it recognisable; everything else is redrawn in the 80s cel style (proportions, line, shading, background). For several people, list each one with their anchors and left/right order so nobody gets merged or dropped.

### 3. Build the scene concept and recipe

Follow `composition.md` §2–§5:
- Invent the mini-story: chapter title (JP + CN), mission HUD, one short Japanese dialogue line, and 1–3 restrained subject-specific world details. Functional interface panels may carry additional story details.
- Pick one value per variation axis. Fit the archetype to the subject (a dramatic pet → cut-in; an object → item-get; two people → split-screen; a portrait → main-menu or dialogue). If you already made images in this conversation, change at least two high-impact axes so outputs don't repeat.
- Run the preflight checklist.

For the default rich composition, select 4–5 unequal panels including 1–2 partial-feature close-ups. Use 3 for a tighter crop and at most 6 when space permits. Specify panel positions, overlaps and calm background regions using composition.md; do not copy the soccer example onto unrelated subjects.

### 4. Choose reference images

The script passes images to the API in order. Put the **subject photo first** (if any), then 2–3 style refs from `assets/style-refs/` matching the archetype:

| Archetype | Style refs |
|---|---|
| A chapter card | 05-title-card, 01-characters, 03-space-mecha |
| B cut-in | 06-cut-in, 02-onomatopoeia, 01-characters |
| C item get | 04-item-burst, 01-characters, 03-space-mecha |
| D split screen | 07-hud-splitscreen, 01-characters, 02-onomatopoeia |
| E main menu | 08-red-menu, 01-characters, 05-title-card |
| F dialogue | 01-characters, 02-onomatopoeia, 03-space-mecha |

Style refs carry the look far better than words, so always include them, even for text-only subjects.

### 5. Write the prompt

Write it in English (image models follow English best), with all on-image text as exact quoted CJK strings. Save it to a file and keep this structure:

```
[Image roles]
Image 1 is the subject to redraw (identity reference only — do not keep its photographic look, lighting or background). Images 2–4 are style references from the game "Orbitals": match their rendering, colour, typography and film texture; do not copy their characters or text.
(Text-only subject: "All images are style references ..." )

[Subject]
<hero: who/what, identity anchors per subject, pose/expression, crop, placement, coverage %>

[Scene & layout]
<archetype layout in concrete positions: what is top-left, centre band, lower third, right edge; frame type (letterbox / split / full-bleed); mood palette with hex colours; calm space>

[Enrichment & FX]
<1–3 quiet world details; one localized FX family; 3–6 unequal overlapping panels including 1–2 partial-feature close-ups, each with a subject-relevant function; specify clean negative space and what stays visually subdued>

[Typography]
<each text element: exact string in quotes, position, look from style-guide §3>

[Style]
<paste the style block from style-guide §5>

[Avoid]
photorealism, 3D render look, modern flat vector, glossy digital painting, black outlines everywhere, extra or garbled text beyond the listed strings, watermarks, duplicated hero, merged or missing people, extra fingers.
```

Be concrete about positions and sizes — "giant white title spanning 80% of the width across the middle third, crossing in front of the hero's torso" beats "a big title".

### 6. Generate

Save the prompt and the result under `./orbitals-art/` in the current working directory, with a slug like `cat-cut-in`. Make one image per request unless the user asks for more — generation is slow and costs money.

**Option A — built-in image generation (preferred when available, e.g. Codex).** If the environment gives you an image-generation or image-editing tool, use it directly: send the compiled prompt and attach the subject photo plus the chosen style refs from `SKILL_DIR/assets/style-refs/` if the tool accepts input images. If it doesn't accept images, send the prompt alone — the style block carries the look. Use the tool's closest size to the chosen aspect ratio, then save or copy the result to `./orbitals-art/<slug>.png`.

**Option B — bundled script (when there is no built-in tool).** It calls the OpenAI Images API with only the Python standard library:

```bash
python3 SKILL_DIR/scripts/generate.py --prompt-file ./orbitals-art/<slug>.txt \
  --ref <subject.jpg> --ref SKILL_DIR/assets/style-refs/<a>.jpg --ref SKILL_DIR/assets/style-refs/<b>.jpg \
  --size 1536x1024 --out ./orbitals-art/<slug>.png
```

- Needs `OPENAI_API_KEY`. If it's missing, tell the user how to set it (`export OPENAI_API_KEY=...` in their shell profile), give them the prompt file path, and stop — don't try to work around it.
- `OPENAI_IMAGE_MODEL` overrides the default model (`gpt-image-1`); `OPENAI_BASE_URL` points at a compatible proxy.
- `--dry-run` prints the request without calling the API.

### 7. Check and deliver

Open the result and compare it with the preflight checklist: is the hero recognisable through its anchors, is it clearly 80s cel anime (not a filtered photo), are unequal interface layers clearly overlapping, is the background calm rather than filled with stars/debris/architecture, is the text legible, and is the bottom dialogue Japanese unless the user requested otherwise?

Then reply briefly (in the user's language) with:
- the image path, and the image itself,
- one line on the scene concept (chapter / mission / layout / mood) so the user knows what was intended,
- any visible flaw worth fixing (e.g. garbled text, a missing element), with an offer to regenerate with a tweak.

Don't regenerate automatically. Image models often garble CJK text, so if the text came out wrong, suggest shortening it or dropping a text element rather than retrying the same prompt.
