#!/usr/bin/env python3
"""
Clean all markdown files in docs/vi/ to ensure 100% valid Vue/VitePress template syntax.
1. Removes any leftover raw HTML nav/div tags from scraping.
2. Replaces unescaped <T>, <int>, <typename> in text with `...` code blocks.
"""

import glob
import os
import re

DOCS_VI = "/home/nam/Documents/learncpp/docs/vi"

def clean_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Protect code blocks
    code_blocks = []
    def save_cb(m):
        code_blocks.append(m.group(0))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"
    content = re.sub(r'```[\s\S]*?```', save_cb, content)

    inline_code = []
    def save_ic(m):
        inline_code.append(m.group(0))
        return f"__INLINE_CODE_{len(inline_code)-1}__"
    content = re.sub(r'`[^`\n]+`', save_ic, content)

    # 2. Strip raw html leftovers like <a class="nav-link"...>...</a>
    content = re.sub(r'<a\s+class="nav-link"[^>]*>[\s\S]*?</a>', '', content)
    content = re.sub(r'</?a\b[^>]*>', '', content)
    content = re.sub(r'</?i\b[^>]*>', '', content)
    content = re.sub(r'</?div\b[^>]*>', '', content)
    content = re.sub(r'</?span\b[^>]*>', '', content)
    content = re.sub(r'</?p\b[^>]*>', '\n\n', content)
    content = re.sub(r'</?center\b[^>]*>', '', content)

    # 3. Handle unescaped template angle brackets like <int>, <T>, <typename>, <bool>
    # In Vue markdown, <T> is parsed as an HTML tag! If it has no closing tag, it causes compilation error!
    # Convert <type> in text to `type`
    content = re.sub(r'<([a-zA-Z0-9_:\*]+)>', r'`<\1>`', content)

    # 4. Restore inline code and code blocks
    for idx, ic in enumerate(inline_code):
        content = content.replace(f"__INLINE_CODE_{idx}__", ic)

    for idx, cb in enumerate(code_blocks):
        content = content.replace(f"__CODE_BLOCK_{idx}__", cb)

    # 5. Clean excess whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

def main():
    files = glob.glob(f"{DOCS_VI}/*/*.md")
    print(f"Cleaning {len(files)} files in docs/vi/...")
    for f in files:
        clean_file(f)
    print("Cleaned all files successfully!")

if __name__ == "__main__":
    main()
