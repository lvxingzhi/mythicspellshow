import json
d = json.load(open('site/data.json'))
# 检查所有行是否有破坏HTML的字符
for i, r in enumerate(d['rows']):
    for key, val in r.items():
        if isinstance(val, str):
            for c in val:
                if c in '<>' or ord(c) < 32:
                    print(f'row {i} {key} U+{ord(c):04X} in dungeon={r["dungeonZh"]} spell={r["spellName"]}')
                    print(f'  val: {repr(val[:120])}')
                    break