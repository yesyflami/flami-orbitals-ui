# 轨道双子星 (Orbitals) 视觉风格指南

Distilled from in-game screenshots. Use it to write the style paragraphs of the prompt; copy the English phrases, they are tuned for image models.

## 1. Rendering (画风)

The look is **late-1980s Japanese TV/OVA cel animation** (Dirty Pair, Urusei Yatsura, early Gundam era) rebuilt with modern colour and lighting. Two layers coexist:

- **Cel layer — characters, mecha, props.** Thin hand-inked outlines that are *coloured*, not black: dark red-brown (#5A2A1E) on warm surfaces, deep navy on cool ones. Flat base colour + one hard-edged shadow tone (sometimes a second, darker accent shadow). Small sharp white highlight blocks on hair, glasses, metal. No soft gradients on the cel layer.
- **Painted layer — backgrounds.** Gouache/airbrush-like painted backdrops, softer edges, atmospheric depth, volumetric light shafts, glowing particles. Less detail than the cel layer so the characters pop.

Characters:
- 80s anime faces: large irises with 2–3 highlights, defined upper lash line, thick expressive eyebrows, small angular nose, small mouth that opens wide when shouting. Mature-ish proportions (6–7 heads) for main cast; **chibi** proportions (2.5 heads) for mascots/side characters.
- Big, chunky hair masses with sharp tufts: sky blue, salmon pink, jet black with blue sheen, white/grey.
- The cast includes non-human skin tones (blue, purple, red) treated as normal anime characters — horns, goggles, round glasses, headbands.
- Expressions skew comedic and dramatic: exasperated, shouting, deadpan glare, giant reaction faces.

Mecha / props:
- Rounded retro-future industrial design: chunky capsule shapes, pastel armour plates (cream, sky blue, salmon), rivets, panel lines, glowing round lamps (warm orange/yellow), cables and hoses everywhere.
- Signature motif: small round teal scout pod with **three glowing orange lamps in a triangle**.
- Space-suit "mech suits" with bubble helmets, backpack thrusters, mitten hands.

FX:
- Anime speed lines and radial bursts (white/pale-blue spikes), streaked hyperspace light (vertical rainbow-coloured streaks), hand-drawn explosions with layered orange/yellow/red shapes, neon beams with bloom, chunky floating debris and asteroids with flat cel shading.

## 2. Scene moods / palettes (配色)

Pick one per image. Each is anchored in screenshots; hex values are approximate targets.

| Mood | Use for | Colours |
|---|---|---|
| **红幕菜单 Red menu** | portraits, character select, poster-like layouts | crimson #B3222F (dominant flat field), cream #F3E6D8, sky blue #6FA8EE, charcoal #2B2B2E, gold #F2B33D |
| **深空极光 Aurora space** | calm, nostalgic, title screens | blue-black #070B1A, teal aurora #2E6F72, violet #5A4A8C, star gold #F6D27A, signal red #E3342F |
| **遗迹森林 Overgrown ruins** | outdoor, daylight, nature, pets | terracotta #E07B4A, moss #6E9F3A, deep olive #23301F, warm amber #F4A259, rust #8C3B22 |
| **熔炉 Furnace** | dramatic, intense, workshop, food | oxblood #3A0F0C, ember orange #F06A1E, red #C8352B, amber #FFB347, soot #140806 |
| **金色漩涡 Golden vortex** | mystical, discovery, "what is this?" | ochre #C9A23A, pale gold #F5E7A8, lavender #B9B6E8, rose #D88AA0, teal #2F6E78 |
| **跃迁霓虹 Warp neon** | action, speed, battle, cut-in | deep purple #1C1030, magenta #C040F0, cyan #3FD6F0, hot orange #FF7A3D, near-black #0A0A12 |
| **控制室 Control room** | indoor, tech, night, conversation | slate navy #1B2333, steel #3A4558, cable green #3E7A3A, LED red #E8332A, LED cyan #4FD3F2, skin/peach accents |

General colour behaviour: saturated but slightly **faded film stock** — lifted blacks, warm cast in highlights, colours never neon-clean except actual light sources. Characters keep their own bright local colours (blue hair, pink hair, cream shirt) against the mood palette — that contrast is part of the look.

## 3. Typography (字体)

Text is a core part of the look. Every image gets 2–5 text elements from this list (see composition.md for how many):

| Element | Look | Example |
|---|---|---|
| **Chapter title card** | Massive ultra-heavy white Japanese gothic, hand-cut slightly jagged edges, tight spacing, spanning ~80% of frame width across the centre, faint red/cyan fringe. Small bold white Chinese subtitle centred beneath with wide letter-spacing. | 「秘密の庭」+「秘密花园」 |
| **Logo** | Slanted, angular, sharp-cut katakana with a red four-point star flare crossing it; cream fill. | 「オービタルズ」 |
| **Onomatopoeia / reaction** | Hand-lettered rounded manga kana, cream-yellow fill #F8D98A, thick dark-brown outline, tilted, stacked vertically, huge. | 「はあ!?」「ドーン」 |
| **Item-get title** | Bold rounded red katakana with white outline + drop shadow, slight arc; small grey Chinese label below. | 「ジャンプパック」+「喷气背包」 |
| **Dialogue subtitle** | Lower third, centred or left-aligned. Speaker name in pink-red #F06A7A (or periwinkle blue) on its own line, line text in yellow #F2D45A, rounded gothic, thin dark outline. | 「尾村」/「这个发光的机器究竟是什么东西——？」 |
| **Quest HUD** | Top-left, small white text with soft shadow; second line starts with a yellow ◇ diamond and ends with yellow progress "0/5". | 「启动主电梯」/「◇ 修复故障系统 0/5」 |
| **Menu / buttons** | Blue rounded-trapezoid pills with outer glow, cream circle button icon ("A", "B") + white label. | 「Ⓐ 开始」「Ⓑ 返回」 |
| **Player badges** | Top-right: two small rounded squares "P1" (blue) "P2" (grey or blue) with a cream gamepad icon below. | P1 P2 |
| **Big counter** | Single white digit in a red square plate, or a 7-segment-style LED readout "000.0" on a pastel device. | 「3」 |

Text rules: keep each string short (titles ≤ 5 characters, dialogue ≤ 20 characters) because image models garble long CJK strings. Always put the exact text in quotes in the prompt.

## 4. Film / screen surface (质感)

Applied over the whole frame — this is what makes it feel like a capture of a game, not a clean illustration:

- visible fine **film grain**, slightly heavier in shadows
- light **chromatic aberration** (red/cyan fringe) on high-contrast edges and text
- **halation / bloom** around light sources and glowing UI
- soft **vignette**, very mild CRT barrel softness at corners
- optional **cinematic letterbox** (black bars top and bottom) for cinematic shots
- slightly faded, warm VHS/film colour response

## 5. English style block (paste into every prompt)

```
Style: late-1980s Japanese cel animation (OVA / TV anime era) as seen in the video game "Orbitals". Cel-shaded characters and mecha with thin coloured ink outlines (dark red-brown or navy, not black), flat base colours with one hard-edged shadow tone and small sharp white highlights; expressive 80s anime faces with large multi-highlight irises and thick eyebrows. Painted gouache-style background with atmospheric depth and volumetric light. Rounded retro-futuristic industrial mecha with pastel armour, rivets, cables and glowing round orange lamps. Faded film-stock colour, lifted blacks, fine film grain, light chromatic aberration on edges, bloom around lights, soft vignette.
```
