"""模拟渲染通天峰 spell 1254669，检查生成的 HTML 是否有效。"""
import json

ESC = {"\u0026": "\u0026amp;", "\u003c": "\u0026lt;", "\u003e": "\u0026gt;", "\u0022": "\u0026quot;", "\u0027": "\u0026#39;"}
def escapeHtml(s):
    return str(s == None or s or "").replace() if False else ""
# 简化版
def eh(s):
    if s is None: s = ""
    s = str(s)
    for c in ["&", "<", ">", '"', "'"]:
        s = s.replace(c, {"&": "&", "<": "<", ">": ">", '"': """, "'": "&#39;"}[c])
    return s

d = json.load(open('site/data.json'))
for r in d['rows']:
    if r['spellId'] == '1254669':
        WOWHEAD_BASE = "https://www.wowhead.com/spell="
        row_html = (
            "<tr>" +
            '<td class="dungeon">' + eh(r['dungeonZh']) + '</td>' +
            '<td class="mob">' + ('<span class="tag tag-boss">BOSS</span> ' if r['isBoss'] else '') + eh(r['mobZh']) + '<br><span class="en">' + eh(r['mobEn']) + '</span></td>' +
            '<td class="spellname"><a href="' + WOWHEAD_BASE + str(r['spellId']) + '" target="_blank" rel="noopener">' + eh(r['spellName']) + '</a>' +
            '<div class="sid">ID ' + eh(r['spellId']) + '</div></td>' +
            '<td>' + ('<span class="tag tag-int">可打断</span>' if r['interruptible'] else '<span class="tag tag-no">—</span>') + '</td>' +
            '<td>' + ('<span class="tag tag-mag">魔法</span>' if r['isMagic'] else '<span class="tag tag-no">—</span>') + '</td>' +
            '<td>' + ('<span class="tag tag-enrage">激怒</span>' if r['isEnrage'] else '<span class="tag tag-no">—</span>') + '</td>' +
            '<td>' + ('<span class="tag tag-bleed">流血</span>' if r['isBleed'] else '<span class="tag tag-no">—</span>') + '</td>' +
            '<td>' + ('<span class="tag tag-poison">中毒</span>' if r['isPoison'] else '<span class="tag tag-no">—</span>') + '</td>' +
            '<td>' + ('<span class="tag tag-disease">疾病</span>' if r['isDisease'] else '<span class="tag tag-no">—</span>') + '</td>' +
            '<td>' + ('<span class="tag tag-curse">诅咒</span>' if r['isCurse'] else '<span class="tag tag-no">—</span>') + '</td>' +
            '<td class="desc">' + eh(r.get('description', '')) + '</td>' +
            '</tr>'
        )
        # 数 td
        td_count = row_html.count('<td')
        tr_count = row_html.count('<tr')
        close_tr = row_html.count('</tr>')
        print(f'<td> count: {td_count}, <tr> count: {tr_count}, </tr> count: {close_tr}')
        # 检查是否有未闭合标签
        print(f'description field: {repr(r.get("description", ""))}')
        break