#!/usr/bin/env python3
"""
HTML to Markdown Converter for LearnCpp.
Converts WordPress HTML posts into beautiful, semantic VitePress Markdown.
Preserves C++ code blocks, callouts (admonitions), quizzes, hints, and diagrams.
"""

import re
import html

def clean_html(raw_html):
    if not raw_html:
        return ""

    # Remove script, style, comments, and ad placeholders
    text = re.sub(r'<!--.*?-->', '', raw_html, flags=re.DOTALL)
    text = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<style.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<div class="cf_monitor".*?</div>\s*<hr>', '', text, flags=re.DOTALL)
    text = re.sub(r'<div id="ezoic-pub-ad-placeholder-.*?</div>', '', text, flags=re.DOTALL)
    
    # Remove prevnext buttons
    text = re.sub(r'<div class="prevnext".*?</div>\s*</div>\s*</div>', '', text, flags=re.DOTALL)
    text = re.sub(r'<div class="prevnext".*?</div>\s*</div>', '', text, flags=re.DOTALL)
    text = re.sub(r'<div class="prevnext".*?</div>', '', text, flags=re.DOTALL)

    # Remove solution toggle links (e.g., <p><a class="solution_link_show"...>Show Solution</a></p>)
    text = re.sub(r'<p>\s*<a class="solution_link_show"[^>]*>.*?</a>\s*</p>', '', text, flags=re.DOTALL)
    text = re.sub(r'<a class="solution_link_show"[^>]*>.*?</a>', '', text, flags=re.DOTALL)
    text = re.sub(r'<p>\s*<a class="hint_link_show"[^>]*>.*?</a>\s*</p>', '', text, flags=re.DOTALL)
    text = re.sub(r'<a class="hint_link_show"[^>]*>.*?</a>', '', text, flags=re.DOTALL)

    # Replace <pre ...><code ...>...</code></pre> with placeholder so we don't mess up code
    code_blocks = []
    def code_repl(match):
        code_content = match.group(1)
        # Unescape HTML entities inside code block
        code_content = html.unescape(code_content)
        idx = len(code_blocks)
        code_blocks.append(code_content)
        return f"\n\n__CODE_BLOCK_{idx}__\n\n"

    text = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', code_repl, text, flags=re.DOTALL)
    text = re.sub(r'<pre[^>]*>(.*?)</pre>', code_repl, text, flags=re.DOTALL)

    # Convert notes/callouts
    # Note colors mapping to VitePress admonitions
    callout_map = {
        'cpp-lightgreenbackground': ('tip', 'Thực hành tốt nhất (Best Practice)'),
        'cpp-lightbluebackground': ('info', 'Ghi chú quan trọng'),
        'cpp-lightredbackground': ('danger', 'Cảnh báo nguy hiểm / Cạm bẫy'),
        'cpp-lightyellowbackground': ('warning', 'Quy tắc (Rule)'),
        'cpp-lightpurplebackground': ('tip', 'Kiến thức chuyên sâu'),
        'cpp-lightgraybackground': ('info', 'Thông tin mở rộng')
    }

    # Pattern for note titles
    # <p class="cpp-note-title cpp-bottomline">...</p>
    def note_repl(match):
        div_class = match.group(1)
        inner = match.group(2)
        
        adm_type = 'info'
        adm_title = 'Ghi chú'
        for cls_name, (atype, atitle) in callout_map.items():
            if cls_name in div_class:
                adm_type = atype
                adm_title = atitle
                break
        
        # Check if there is an explicit title inside
        title_match = re.search(r'<p class="cpp-note-title[^"]*">(.*?)</p>', inner, flags=re.DOTALL)
        if title_match:
            custom_title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
            if custom_title:
                adm_title = custom_title
            inner = inner[:title_match.start()] + inner[title_match.end():]

        return f"\n\n::: {adm_type} {adm_title}\n{inner.strip()}\n:::\n\n"

    # Replace notes (may be nested or multiple, run multiple passes if needed)
    for _ in range(3):
        text = re.sub(r'<div class="([^"]*cpp-note[^"]*)">(.*?)</div>', note_repl, text, flags=re.DOTALL)

    # Solutions & Hints (wpsolution & wphint)
    def solution_repl(match):
        inner = match.group(1)
        return f"\n\n::: details Xem lời giải (Solution)\n{inner.strip()}\n:::\n\n"
    text = re.sub(r'<div class="wpsolution"[^>]*>(.*?)</div>', solution_repl, text, flags=re.DOTALL)

    def hint_repl(match):
        inner = match.group(1)
        return f"\n\n::: details Gợi ý (Hint)\n{inner.strip()}\n:::\n\n"
    text = re.sub(r'<div class="wphint"[^>]*>(.*?)</div>', hint_repl, text, flags=re.DOTALL)

    # Headings
    text = re.sub(r'<p class="cpp-section[^"]*">(.*?)</p>', r'\n\n## \1\n\n', text)
    text = re.sub(r'<p class="cpp-quiz-question[^"]*">(.*?)</p>', r'\n\n### \1\n\n', text)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n\n### \1\n\n', text)
    text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n\n#### \1\n\n', text)

    # Inline formatting
    text = re.sub(r'<code[^>]*>(.*?)</code>', lambda m: f"`{html.unescape(m.group(1))}`", text)
    text = re.sub(r'<(?:strong|b)>(.*?)</(?:strong|b)>', r'**\1**', text)
    text = re.sub(r'<(?:em|i)>(.*?)</(?:em|i)>', r'*\1*', text)

    # Links
    text = re.sub(r'<a href="([^"]+)">(.*?)</a>', r'[\2](\1)', text)

    # Images
    text = re.sub(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"[^>]*>', r'![\2](\1)', text)
    text = re.sub(r'<img[^>]*src="([^"]+)"[^>]*>', r'![](\1)', text)

    # Lists
    text = re.sub(r'<li>\s*(.*?)\s*</li>', r'- \1\n', text, flags=re.DOTALL)
    text = re.sub(r'</?[ou]l>', '\n', text)

    # Paragraphs and line breaks
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\n\1\n\n', text, flags=re.DOTALL)
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<hr\s*/?>', '\n\n---\n\n', text)

    # Strip any remaining HTML tags (except ::: containers)
    text = re.sub(r'</?(?:div|span|table|tbody|thead|tr|td|th|nobr|font|u|cite|center)[^>]*>', '', text)

    # Unescape HTML entities in normal text
    text = html.unescape(text)

    # Restore code blocks
    for idx, c in enumerate(code_blocks):
        text = text.replace(f"__CODE_BLOCK_{idx}__", f"```cpp\n{c.strip()}\n```")

    # Clean multiple blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

if __name__ == "__main__":
    import json
    with open("/home/nam/Documents/learncpp/data/indexed_posts.json") as f:
        posts = json.load(f)
    
    sample = posts["introduction-to-objects-and-variables"]
    md = clean_html(sample["content"])
    print("Converted Markdown preview (first 1000 chars):")
    print(md[:1000])
