#!/usr/bin/env python3
"""
Strip all remaining raw HTML tags outside of code blocks in docs/vi/
"""

import glob
import re

files = glob.glob('/home/nam/Documents/learncpp/docs/vi/*/*.md')
files.extend(glob.glob('/home/nam/Documents/learncpp/docs/*.md'))
print(f'Cleaning raw HTML from {len(files)} files...')

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()

    # Protect code blocks
    code_blocks = []
    def save_cb(m):
        code_blocks.append(m.group(0))
        return f"__CB_{len(code_blocks)-1}__"
    c = re.sub(r'```[\s\S]*?```', save_cb, c)

    inline_codes = []
    def save_ic(m):
        inline_codes.append(m.group(0))
        return f"__IC_{len(inline_codes)-1}__"
    c = re.sub(r'`[^`\n]+`', save_ic, c)

    # Convert common tags
    c = re.sub(r'</?(?:blockquote|footer|header|section|aside|div|span|p|center|nobr|font|u|cite|b|i|strong|em|a)\b[^>]*>', '', c, flags=re.I)
    # Strip any leftover closing tags
    c = re.sub(r'</[a-zA-Z0-9_\-]+>', '', c)

    # Restore
    for idx, ic in enumerate(inline_codes):
        c = c.replace(f"__IC_{idx}__", ic)
    for idx, cb in enumerate(code_blocks):
        c = c.replace(f"__CB_{idx}__", cb)

    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)

print('Cleaned all files of raw HTML tags successfully!')
