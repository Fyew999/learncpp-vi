#!/usr/bin/env python3
"""
LearnCpp Scraper & Data Pipeline
Scrapes all 388+ lessons and Table of Contents directly from LearnCpp's WordPress REST API.
Saves raw posts and structured chapters/lessons metadata.
"""

import urllib.request
import json
import re
import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
TOC_FILE = os.path.join(DATA_DIR, "toc.json")
POSTS_FILE = os.path.join(RAW_DIR, "all_posts.json")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def fetch_table_of_contents():
    print("[1/3] Đang tải mục lục từ trang chủ LearnCpp (page 8)...")
    url = "https://www.learncpp.com/wp-json/wp/v2/pages/8"
    data = fetch_json(url)
    content = data.get("content", {}).get("rendered", "")

    tables = content.split('<div class="lessontable">')
    toc = []
    total_lessons = 0

    for t in tables[1:]:
        chap_match = re.search(
            r'<div class="lessontable-header-chapter">(.*?)</div>\s*<div class="lessontable-header-title">(.*?)</div>',
            t,
            re.DOTALL
        )
        if not chap_match:
            continue
        chap_num = chap_match.group(1).replace("&nbsp;", " ").strip()
        chap_title = chap_match.group(2).strip()

        lessons = re.findall(
            r'<div class="lessontable-row-number">(.*?)</div>\s*<div class="lessontable-row-title"><a href="(.*?)">(.*?)</a>',
            t,
            re.DOTALL
        )

        lesson_list = []
        for num, link, title in lessons:
            clean_link = link.strip().rstrip("/") + "/"
            slug_match = re.search(r'/([^/]+)/$', clean_link)
            slug = slug_match.group(1) if slug_match else ""
            lesson_list.append({
                "number": num.strip(),
                "title": title.strip(),
                "url": clean_link,
                "slug": slug
            })
            total_lessons += 1

        toc.append({
            "chapter": chap_num,
            "title": chap_title,
            "lesson_count": len(lesson_list),
            "lessons": lesson_list
        })

    print(f" -> Đã lấy thành công {len(toc)} chương với {total_lessons} bài học.")
    return toc

def fetch_all_posts():
    print("[2/3] Đang tải toàn bộ bài viết từ WordPress REST API...")
    all_posts = []
    page = 1
    while True:
        url = f"https://www.learncpp.com/wp-json/wp/v2/posts?per_page=100&page={page}"
        print(f" -> Tải trang {page}...")
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req) as resp:
                total_pages = int(resp.headers.get("X-WP-TotalPages", 1))
                posts = json.loads(resp.read().decode("utf-8"))
                all_posts.extend(posts)
                if page >= total_pages:
                    break
                page += 1
                time.sleep(0.3)
        except Exception as e:
            print(f" -> Lỗi ở trang {page}: {e}")
            break

    print(f" -> Đã tải tổng cộng {len(all_posts)} bài viết.")
    return all_posts

def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    
    # 1. Fetch TOC
    toc = fetch_table_of_contents()
    with open(TOC_FILE, "w", encoding="utf-8") as f:
        json.dump(toc, f, ensure_ascii=False, indent=2)
    print(f" -> Đã lưu mục lục vào {TOC_FILE}")

    # 2. Fetch all posts
    posts = fetch_all_posts()
    with open(POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    print(f" -> Đã lưu raw posts vào {POSTS_FILE}")

    # 3. Create quick index mapping
    slug_to_post = {}
    for p in posts:
        slug = p.get("slug")
        if slug:
            slug_to_post[slug] = {
                "id": p.get("id"),
                "date": p.get("date"),
                "modified": p.get("modified"),
                "slug": slug,
                "link": p.get("link"),
                "title": p.get("title", {}).get("rendered"),
                "content": p.get("content", {}).get("rendered")
            }
    
    indexed_file = os.path.join(DATA_DIR, "indexed_posts.json")
    with open(indexed_file, "w", encoding="utf-8") as f:
        json.dump(slug_to_post, f, ensure_ascii=False, indent=2)
    print(f" -> Đã lập chỉ mục {len(slug_to_post)} bài vào {indexed_file}")

    # Verification: check TOC lessons against indexed posts
    matched = 0
    missing = []
    for ch in toc:
        for l in ch["lessons"]:
            if l["slug"] in slug_to_post:
                matched += 1
            else:
                missing.append((l["number"], l["title"], l["slug"], l["url"]))

    print(f"[3/3] Kiểm tra khớp bài học: Khớp {matched}/{sum(c['lesson_count'] for c in toc)} bài.")
    if missing:
        print(f"Các bài chưa khớp slug ({len(missing)} bài):")
        for m in missing[:5]:
            print(f"   {m[0]} - {m[1]} ({m[2]})")

    print("\n HOÀN THÀNH CÀO TOÀN BỘ NỘI DUNG GỐC TỪ LEARNCPP!")

if __name__ == "__main__":
    main()
