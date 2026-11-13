#!/usr/bin/env python3
"""
Fix markdown files so they compile cleanly with VitePress / Vue SFC compiler.
Rules:
1. Protect code blocks (``` ... ```) and inline code (` ... `).
2. Protect allowed HTML tags: <details>, </details>, <summary>, </summary>, <br>, <br/>, <hr>, <hr/>.
3. Remove lingering scraped structural HTML tags like <ol...>, </ol>, <ul...>, </ul>, <li...>, </li>, <p...>, </p>, etc.
4. Escape any other '<' and '>' to '&lt;' and '&gt;' so Vue doesn't mistake C++ templates (<T>), arrows (<->), headers (<xxx.h>), etc. for Vue components.
5. Restore code blocks and inline code.
"""

import glob
import re

files = glob.glob('/home/nam/Documents/learncpp/docs/vi/*/*.md')
files.extend(glob.glob('/home/nam/Documents/learncpp/docs/*.md'))
print(f"Processing {len(files)} markdown files...")

ALLOWED_TAG_PATTERN = re.compile(
    r'(</?(?:details|summary)\b[^>]*>|<(?:br|hr)\s*/?>)',
    re.IGNORECASE
)

TAGS_TO_REMOVE = re.compile(
    r'</?(?:ol|ul|li|p|div|span|blockquote|footer|header|section|aside|center|nobr|font|u|cite|b|i|strong|em|a|table|tr|td|th|tbody|thead|tfoot)\b[^>]*>',
    re.IGNORECASE
)

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Protect code blocks
    code_blocks = []
    def save_cb(m):
        code_blocks.append(m.group(0))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"
    content = re.sub(r'```[\s\S]*?```', save_cb, content)

    # 2. Protect inline code
    inline_codes = []
    def save_ic(m):
        inline_codes.append(m.group(0))
        return f"__INLINE_CODE_{len(inline_codes)-1}__"
    content = re.sub(r'`[^`\n]+`', save_ic, content)

    # 3. Protect allowed tags (<details>, <summary>, <br>, <hr>)
    allowed_tags = []
    def save_allowed(m):
        allowed_tags.append(m.group(0))
        return f"__ALLOWED_TAG_{len(allowed_tags)-1}__"
    content = ALLOWED_TAG_PATTERN.sub(save_allowed, content)

    # 4. Remove scrap leftovers like <ol>, </ol>, <li>, etc.
    content = TAGS_TO_REMOVE.sub('', content)

    # 5. Any remaining '<' or '>' in text outside code:
    # E.g. <xxx.h>, <class InputIterator>, <->, etc.
    # Replace '<' with '&lt;' and '>' with '&gt;'
    content = content.replace('<', '&lt;').replace('>', '&gt;')

    # 6. Restore allowed tags
    for idx, tag in enumerate(allowed_tags):
        content = content.replace(f"__ALLOWED_TAG_{idx}__", tag)

    # 7. Restore inline code
    for idx, ic in enumerate(inline_codes):
        content = content.replace(f"__INLINE_CODE_{idx}__", ic)

    # 8. Restore code blocks
    for idx, cb in enumerate(code_blocks):
        content = content.replace(f"__CODE_BLOCK_{idx}__", cb)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done fixing all markdown files!")
