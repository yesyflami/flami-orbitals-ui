# flami-orbitals-ui

把一张照片或一句描述，变成《轨道双子星 / Orbitals》游戏画面风格的插画：80 年代赛璐璐动画画风 + 游戏里的章节标题、拟声词、对话字幕、任务 HUD、头像卡等界面元素。构图采用：一个主体 + 多层叠压的界面元素 + 局部特写小窗 + 围绕主体新增的世界观元素。

默认采用大小不同、错位交叠的游戏界面窗口，搭配局部特写；背景保持低对比、少细节和足够留白。底部对白及说话人标签默认使用日文，用户指定的文字和语言优先。每张图根据主体选择窗口内容，不固定套用足球示例。

## 安装

本地 ZIP 安装：解压后将完整的 `flami-orbitals-ui` 文件夹放入 `~/.codex/skills/`（Codex）或 `~/.claude/skills/`（Claude Code）。可直接修改本地文件并重新打包，无需 Git 提交。


**Codex**

```bash
git clone https://github.com/yesyflami/flami-orbitals-ui.git ~/.codex/skills/flami-orbitals-ui
```

**Claude Code**

```bash
git clone https://github.com/yesyflami/flami-orbitals-ui.git ~/.claude/skills/flami-orbitals-ui
```

## 使用

- 「把这张照片做成轨道双子星风格」
- 「画一张轨道双子星风格的橘猫，用熔炉色调、道具获得版式」

可选指定：
- 色调：红幕菜单 / 深空极光 / 遗迹森林 / 熔炉 / 金色漩涡 / 跃迁霓虹 / 控制室
- 版式：章节标题卡 / 角色切入 / 道具获得 / 双人分屏 / 主菜单 / 对话特写
- 比例：横版（默认）/ 竖版 / 方形

## 出图方式

1. 环境自带生图工具（如 Codex）时直接使用；
2. 否则使用 `scripts/generate.py` 调用 OpenAI Images API（仅需 Python 标准库），需设置 `OPENAI_API_KEY`。

## 目录

```
SKILL.md                     工作流
references/style-guide.md    画风 / 配色 / 字体 / 质感
references/composition.md    构图层级、六种版式、变化规则
assets/style-refs/           风格参考图（游戏截图，版权归原游戏所有，后续将替换为自制示例）
scripts/generate.py          OpenAI 出图脚本
agents/openai.yaml           Codex 界面元数据
```
