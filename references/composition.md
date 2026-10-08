# Composition system

Borrowed structure from `tait-crt-interface-skill` (one dominant subject + a hierarchy of overlapping interface layers + unequal close-up insets + a variation engine), re-skinned with the Orbitals game-screen vocabulary. The goal is that every image reads as **a captured moment from the game starring the user's subject** — not just a style filter.

## Contents
1. Layer stack (what every image contains)
2. Scene concept (the mini-story)
3. Layout archetypes
4. Variation axes
5. Compatibility rules
6. Preflight checklist

---

## 1. Layer stack

Build the frame from back to front:

| # | Layer | Rule |
|---|---|---|
| 1 | **Painted world** | Background scene in the chosen mood palette. Must contain 2–4 *world details* (pipes, cables, asteroids, overgrown machinery, starfield, control panels) so the frame feels inhabited. |
| 2 | **Hero** | Exactly one hero composition — the user's subject, or the anchored group as one unit. Covers **55–75%** of the frame (never below 45% after overlaps). Placed off-centre. Never boxed inside a frame or window. |
| 3 | **World enrichment** | 3–5 secondary story elements that did not exist in the source, chosen to *extend the subject's identity into the game world* (see §2). Smaller than the hero, distributed across at least two quadrants. |
| 4 | **FX** | One dominant FX family (speed lines, radial burst, hyperspace streaks, neon beam, sparkle stars, floating debris, explosion). It must interact with the hero (radiate from, frame, or trail behind it). |
| 5 | **Close-up insets** | 1–2 portrait cards (rounded square, folder-tab corner, blue frame for P1 / salmon frame for P2, small name label at bottom). Each shows a *partial distinctive element* — a reaction face, the signature accessory, a paw, an eye behind glasses. Never a second full copy of the hero. With two insets, give them different sizes and different crops. |
| 6 | **Typography & HUD** | 2–5 text elements from style-guide §3: exactly one *big type device* (chapter title / onomatopoeia / item title / logo), plus 1–4 small ones (dialogue subtitle, quest HUD, buttons, P1/P2 badges, counter). |
| 7 | **Screen surface** | Grain, chromatic aberration, bloom, vignette; optional letterbox. |

Hierarchy: Hero (L) > big type device (L/M) > insets & enrichment (M/S) > HUD (S). Overlap layers by 5–20%: the big title may cross in front of the hero's body but must never cover the face; insets may overlap the hero's edge. Keep **15–25% calm space** (sky, starfield, flat red field, letterbox) so the frame breathes.

## 2. Scene concept (do this before writing the prompt)

Invent a tiny game moment around the subject. Answer in one line each:

- **Chapter**: a 2–5 character Japanese title + Chinese translation that puns on the subject. (cat → 「猫の惑星」/「猫之星」; coffee cup → 「目覚めの炉」/「苏醒熔炉」)
- **Mission**: quest HUD text, e.g. 「找回逃跑的毛线球」/「◇ 已收集毛线 2/5」
- **Line**: one dialogue line ≤ 20 characters with a speaker name — funny, in-character, Chinese.
- **Enrichment**: 3–5 world elements that translate the subject's traits into Orbitals objects. Good enrichment is *specific to the subject*:
  - a dog → floating bone-shaped asteroid, scout pod with dog ears, a paw-print on the airlock
  - a person with a camera → camera turned into a chunky retro-future device with glowing lens, film strips drifting like debris, a teal scout pod photobombing
  - a city skyline → buildings as overgrown orbital towers with cables, the three-lamp scout pod flying past
  - generic fillers when needed: the teal three-lamp scout pod, a chibi mechanic mascot in goggles, floating cargo crates, red four-point star flares, glowing orange lamps.

If the user supplied any of these (title, dialogue, mood), use theirs verbatim.

## 3. Layout archetypes

Choose one. Each names a layout that actually appears in the game.

**A. 章节标题卡 Chapter card** — cinematic letterbox; hero in a deep painted environment at 55–65%; giant white Japanese title across the centre band crossing the hero's body (not face); small Chinese subtitle beneath; dialogue subtitle in lower third; one inset bottom-right. Best moods: ruins, furnace, aurora.

**B. 角色切入 Cut-in** — diagonal split: a giant dramatic reaction face of the hero (cut-in, top-left to centre, cel-shaded in a duotone of the mood) above an action shot of the hero (lower-right) with a neon beam or explosion; heavy speed lines; huge vertical onomatopoeia on one side; quest HUD top-left. Best moods: warp neon, furnace.

**C. 道具获得 Item get** — radial white/pale-blue burst behind the hero's signature object or the hero holding it, on a painted orange-flame or golden-swirl field; red katakana item title arched at top with Chinese label; dialogue subtitle bottom-left; one inset. Optional duplicated split-screen (two identical halves) like the game's co-op view. Best moods: furnace, golden vortex.

**D. 双人分屏 Co-op split screen** — vertical seam down the middle; each half shows the hero from a different angle (or, for a pair of subjects, one per side); quest HUD top-left of each half; P1 inset with blue frame on the left edge, P2 inset with salmon frame on the right edge; shared dialogue in the lower third. Best moods: ruins, control room.

**E. 主菜单 Main menu** — crimson flat diagonal panel on the left 35–45% holding 3 menu pills (the selected one blue and glowing); hero on the right in a starfield/aurora or painted scene; slanted logo-style title over the hero's area; P1/P2 badges top-right; button prompts bottom-right. Best moods: red menu, aurora.

**F. 对话特写 Dialogue close-up** — over-the-shoulder: a large out-of-focus back-of-head/shoulder of a supporting character in the foreground (left 30%), hero facing camera mid-ground at 50–60% with a strong expression; control-room panels with LEDs behind; dialogue subtitle centred bottom; one small inset. Best moods: control room, red menu.

## 4. Variation axes

Pick one value per axis. If earlier images in this conversation used a value, change at least two of: archetype, hero placement, crop, mood.

| Axis | Options |
|---|---|
| archetype | A chapter-card / B cut-in / C item-get / D split-screen / E main-menu / F dialogue |
| mood | red-menu / aurora-space / overgrown-ruins / furnace / golden-vortex / warp-neon / control-room |
| hero placement | left-third / right-third / low-rise (rising from bottom edge) / diagonal / over-shoulder |
| crop | reaction close-up / bust / waist-up / full-body / object-hero |
| big type device | chapter title / onomatopoeia / item title / logo |
| FX family | speed lines / radial burst / hyperspace streaks / neon beam / sparkle stars / floating debris / cel explosion |
| inset count | 1 / 2 (unequal sizes and crops) |
| small text set | dialogue only / dialogue + quest HUD / HUD + buttons + P1P2 / dialogue + counter |
| frame | full-bleed / letterbox / split-screen |

## 5. Compatibility rules

- Archetype fixes some axes: A → letterbox + chapter title; B → onomatopoeia + speed lines/neon beam; C → item title + radial burst; D → split-screen + quest HUD + 2 insets; E → logo + HUD/buttons/P1P2; F → dialogue + reaction close-up or bust.
- Total text elements ≤ 5. With 2 insets use ≤ 4 text elements so the frame does not clutter.
- Reaction close-up crop pairs with B or F only; full-body pairs with A, C, D, E.
- Hero coverage beats decoration: if layers crowd the hero, drop an enrichment element or the second inset before shrinking the hero.
- A group of subjects stays one hero composition — keep everyone, their left/right order and interaction; never merge or drop a person.

## 6. Preflight checklist

Before compiling the prompt, confirm:
- [ ] one hero, 55–75%, off-centre, unboxed, face uncovered
- [ ] 3–5 subject-specific enrichment elements across ≥ 2 quadrants
- [ ] one FX family touching the hero
- [ ] 1–2 insets showing partial features, unequal if two
- [ ] exactly one big type device; total text 2–5; every string short and quoted
- [ ] 15–25% calm space
- [ ] identity anchors (3–5 per subject) carried over; everything else redrawn in the 80s cel style
