# MythicSpellShow

WoW 大秘境技能速查站 —— 从 Excel 数据生成可查询的网页和视频脚本素材。

## 项目结构

```
MythicSpellShow/
├── xlsx/                       # Excel 数据源（按赛季存放）
│   └── 12-S1.xlsx              # 12 版本 S1 赛季
├── site/                       # 网页查询站
│   ├── index.html              # 单文件查询页（支持赛季/副本筛选）
│   ├── convert_xlsx_to_json.py # xlsx → data.json（自动扫描、去重）
│   └── data.json               # 查询数据（脚本生成）
└── scripts/                    # 视频脚本素材
    └── 01_必打断TOP20.md
```

## 数据管理

把 Excel 文件放到 `xlsx/` 目录，文件名即为赛季名（`X-Y.xlsx`，如 `12-S1.xlsx` 表示"12 版本的 S1 赛季"）：

```
xlsx/
├── 12-S1.xlsx              # 12 版本 S1 赛季
├── 11-S2.xlsx              # 11 版本 S2 赛季
└── ...
```

脚本会：
- 自动扫描 `xlsx/` 下所有 `.xlsx` 文件
- 从文件名提取赛季标识（`12-S1.xlsx` → `12-S1`）
- 同赛季同副本内按 `(npcId, spellId)` 去重
- 新赛季数据追加，老数据保留，前端可按赛季切换

## 网页查询站

单文件 HTML + DataTables，部署到 GitHub Pages 即可上线。

### 生成数据

```bash
# 1. 建虚拟环境（首次）
python3 -m venv .venv
.venv/bin/pip install openpyxl

# 2. 转换 xlsx → data.json
.venv/bin/python site/convert_xlsx_to_json.py
```

以后新增赛季数据，放到 `xlsx/` 目录后重跑第 2 步即可。

### 本地预览

```bash
cd site
python3 -m http.server 8000
# 浏览器打开 http://localhost:8000
```

### 部署到 GitHub Pages

1. 把 `site/` 目录里的 `index.html` + `data.json` 推到本仓库
2. 仓库 Settings → Pages → Source 选 `main` 分支根目录
3. 几分钟后访问 `https://lvxingzhi.github.io/MythicSpellShow/` 即可

---

## 视频脚本（scripts/）

- [`scripts/01_必打断TOP20.md`](scripts/01_必打断TOP20.md) — 第一支定调视频的完整逐字稿 + 分镜表