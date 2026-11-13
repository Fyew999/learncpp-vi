import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOCS_VI = os.path.join(BASE_DIR, "docs", "vi")

def write_lesson(ch_folder, filename, content):
    dest_dir = os.path.join(DOCS_VI, ch_folder)
    os.makedirs(dest_dir, exist_ok=True)
    filepath = os.path.join(dest_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f" -> Đã tạo: {ch_folder}/{filename} ({len(content)} bytes)")
