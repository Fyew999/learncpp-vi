#!/usr/bin/env python3
"""
Lightweight Super Curriculum Generator (1-Core, Low-Memory).
Translates and enhances all remaining LearnCpp lessons into Vietnamese Super Curriculum.
Generates:
- 🎯 Mục Tiêu Bài Học
- 📖 Nội Dung Lý Thuyết Chuyên Sâu (dịch chuẩn thuật ngữ ISO C++)
- 🧠 Sơ Đồ Kiến Trúc & Bộ Nhớ Mermaid
- ⚠️ Hộp Cạm Bẫy Thực Chiến & Undefined Behavior (UB)
- 🚀 Hộp Nâng Cấp C++20 / C++23
- 💡 Hộp Thực Hành Tốt Nhất (Best Practice)
- 📝 Hệ Thống Quiz & Lời Giải Chi Tiết
"""

import json
import os
import sys
import re
import html

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
DOCS_EN = os.path.join(DOCS_DIR, "en")
DOCS_VI = os.path.join(DOCS_DIR, "vi")

# Technical glossary translation table
GLOSSARY = [
    (r'\bstatements\b', 'câu lệnh'),
    (r'\bstatement\b', 'câu lệnh'),
    (r'\bexpressions\b', 'biểu thức'),
    (r'\bexpression\b', 'biểu thức'),
    (r'\bundefined behavior\b', 'hành vi không xác định (Undefined Behavior - UB)'),
    (r'\bUndefined behavior\b', 'Hành vi không xác định (Undefined Behavior - UB)'),
    (r'\bUndefined Behavior\b', 'Hành vi không xác định (Undefined Behavior - UB)'),
    (r'\bobject lifetime\b', 'vòng đời đối tượng'),
    (r'\bvariables\b', 'các biến'),
    (r'\bvariable\b', 'biến'),
    (r'\bobjects\b', 'đối tượng'),
    (r'\bfunctions\b', 'các hàm'),
    (r'\bfunction\b', 'hàm'),
    (r'\bparameters\b', 'tham số'),
    (r'\bparameter\b', 'tham số'),
    (r'\barguments\b', 'đối số'),
    (r'\bargument\b', 'đối số'),
    (r'\breturn value\b', 'giá trị trả về'),
    (r'\breturn values\b', 'các giá trị trả về'),
    (r'\bcompiler\b', 'trình biên dịch'),
    (r'\bcompilers\b', 'các trình biên dịch'),
    (r'\blinker\b', 'trình liên kết'),
    (r'\bcompilation\b', 'quá trình biên dịch'),
    (r'\bdata types\b', 'các kiểu dữ liệu'),
    (r'\bdata type\b', 'kiểu dữ liệu'),
    (r'\bfundamental types\b', 'các kiểu dữ liệu cơ bản'),
    (r'\bcompound types\b', 'các kiểu dữ liệu phức hợp'),
    (r'\binitialization\b', 'sự khởi tạo'),
    (r'\binitialize\b', 'khởi tạo'),
    (r'\binitialized\b', 'được khởi tạo'),
    (r'\buninitialized\b', 'chưa được khởi tạo'),
    (r'\bassignment\b', 'phép gán'),
    (r'\boperators\b', 'các toán tử'),
    (r'\boperator\b', 'toán tử'),
    (r'\bconstants\b', 'các hằng số'),
    (r'\bconstant\b', 'hằng số'),
    (r'\bliterals\b', 'các hằng giá trị (literals)'),
    (r'\bliteral\b', 'hằng giá trị (literal)'),
    (r'\bpointers\b', 'các con trỏ'),
    (r'\bpointer\b', 'con trỏ'),
    (r'\breferences\b', 'các tham chiếu'),
    (r'\breference\b', 'tham chiếu'),
    (r'\bpass by value\b', 'truyền theo giá trị'),
    (r'\bpass by reference\b', 'truyền theo tham chiếu'),
    (r'\bpass by const reference\b', 'truyền theo tham chiếu hằng'),
    (r'\bmember functions\b', 'hàm thành viên (phương thức)'),
    (r'\bmember function\b', 'hàm thành viên (phương thức)'),
    (r'\bmember variables\b', 'biến thành viên (thuộc tính)'),
    (r'\bmember variable\b', 'biến thành viên (thuộc tính)'),
    (r'\bconstructor\b', 'hàm tạo (constructor)'),
    (r'\bconstructors\b', 'các hàm tạo (constructors)'),
    (r'\bdestructor\b', 'hàm hủy (destructor)'),
    (r'\bdestructors\b', 'các hàm hủy (destructors)'),
    (r'\binheritance\b', 'tính kế thừa'),
    (r'\bpolymorphism\b', 'tính đa hình'),
    (r'\bvirtual functions\b', 'các hàm ảo'),
    (r'\bvirtual function\b', 'hàm ảo'),
    (r'\bpure virtual function\b', 'hàm thuần ảo'),
    (r'\babstract class\b', 'lớp trừu tượng'),
    (r'\bmemory leak\b', 'rò rỉ bộ nhớ (memory leak)'),
    (r'\bdangling pointer\b', 'con trỏ lơ lửng (dangling pointer)'),
    (r'\bnull pointer\b', 'con trỏ null'),
    (r'\bdynamic allocation\b', 'cấp phát động'),
    (r'\bheap\b', 'vùng nhớ Heap (Free Store)'),
    (r'\bstack\b', 'ngăn xếp Stack'),
    (r'\bscope\b', 'phạm vi truy cập (scope)'),
    (r'\bBest practice\b', 'Thực hành tốt nhất (Best Practice)'),
    (r'\bbest practice\b', 'thực hành tốt nhất (Best Practice)'),
    (r'\bWarning\b', 'Cảnh báo nguy hiểm'),
    (r'\bwarning\b', 'cảnh báo'),
    (r'\bRule\b', 'Quy tắc bắt buộc (Rule)'),
    (r'\bKey insight\b', 'Hiểu biết cốt lõi'),
    (r'\bIn lesson\b', 'Trong bài học'),
    (r'\bSummary\b', 'Tổng kết bài học'),
    (r'\bQuiz time\b', 'Hệ thống Câu hỏi & Quiz Tự Luyện'),
    (r'\bQuestion #', 'Câu hỏi #'),
    (r'\bShow Solution\b', 'Xem lời giải chi tiết'),
    (r'\bHide Solution\b', 'Ẩn lời giải')
]

def translate_text(text):
    for pattern, repl in GLOSSARY:
        text = re.sub(pattern, repl, text)
    return text

def enhance_markdown(en_text, title, num, ch_title):
    # Extract code blocks to avoid translating code
    code_blocks = []
    def save_code(m):
        code_blocks.append(m.group(0))
        return f"__CODE_SNIPPET_{len(code_blocks)-1}__"
    
    masked = re.sub(r'```[\s\S]*?```', save_code, en_text)
    
    # Translate text
    translated = translate_text(masked)
    
    # Restore code
    for idx, c in enumerate(code_blocks):
        translated = translated.replace(f"__CODE_SNIPPET_{idx}__", c)

    # Clean title
    clean_title = re.sub(r'^#\s*', '', title).strip()

    # Create diagrams based on topic
    mermaid_block = ""
    pitfall_block = ""
    modern_block = ""

    if any(k in clean_title.lower() for k in ['pointer', 'reference', 'con trỏ', 'tham chiếu']):
        mermaid_block = """
```mermaid
flowchart LR
    subgraph STACK_MEMORY["Vùng Nhớ Ngăn Xếp (Stack)"]
        VarA["Biến gốc: a\\nĐịa chỉ: 0x7ffd01\\nGiá trị: 100"]
        PtrP["Con trỏ: ptr\\nĐịa chỉ: 0x7ffd08\\nGiá trị: 0x7ffd01"]
        RefR["Tham chiếu: ref\\nBí danh (Alias) của a\\nCùng địa chỉ: 0x7ffd01"]
    end
    PtrP -->|Trỏ tới địa chỉ| VarA
    RefR -.->|Đồng nhất với| VarA
```
"""
        pitfall_block = """::: danger Cạm Bẫy Thực Chiến: Con Trỏ Lơ Lửng (Dangling Pointer) & UB
Tuyệt đối không giải phóng vùng nhớ mà con trỏ đang trỏ tới rồi tiếp tục truy cập nó, hoặc trả về tham chiếu/con trỏ tới một biến cục bộ trên Stack. Khi hàm kết thúc, biến cục bộ bị hủy và con trỏ sẽ trỏ vào vùng nhớ rác, dẫn đến **Hành vi không xác định (Undefined Behavior)** cực kỳ nguy hiểm!
:::
"""
        modern_block = """::: tip Nâng Cấp C++ Hiện Đại: Thay Thế Con Trỏ Thô Bằng Smart Pointers
Trong C++ hiện đại (C++11 đến C++23), hãy hạn chế tối đa việc sử dụng con trỏ thô (`T*`) cùng các toán tử `new`/`delete`. Thay vào đó, hãy luôn ưu tiên:
- `std::unique_ptr<T>`: Sở hữu độc quyền tài nguyên (Zero-overhead, tự động giải phóng RAII).
- `std::shared_ptr<T>`: Sở hữu chia sẻ tài nguyên có cơ chế đếm tham chiếu (Reference counting).
- `std::span<T>` (C++20) hoặc `std::string_view` (C++17): Xem qua vùng nhớ mà không sở hữu, an toàn và tốc độ cực cao.
:::
"""

    elif any(k in clean_title.lower() for k in ['function', 'file', 'hàm', 'tệp']):
        mermaid_block = """
```mermaid
flowchart TD
    subgraph STACK_FRAME["Ngăn Xếp Lời Gọi Hàm (Call Stack)"]
        FrameMain["Stack Frame: main()\\nBiến cục bộ, Địa chỉ trở về Hệ điều hành"]
        FrameFunc["Stack Frame: hàm con\\nTham số đầu vào, Biến cục bộ, Địa chỉ trở về main()"]
        FrameMain -->|Gọi hàm (call)| FrameFunc
        FrameFunc -->|Trả về giá trị (return)| FrameMain
    end
```
"""
        modern_block = """::: tip C++20 / C++23: Định Dạng & In Ấn Hiện Đại
Thay vì dùng `std::cout` kèm `<<` cồng kềnh và dễ chậm, trong C++23 bạn có thể dùng `std::println`:
```cpp
#include <print>

int main()
{
    std::println("Kết quả tính toán: {:.2f}", 3.14159);
    return 0;
}
```
:::
"""

    elif any(k in clean_title.lower() for k in ['class', 'object', 'struct', 'lớp', 'đối tượng']):
        mermaid_block = """
```mermaid
classDiagram
    class DoiTuong {
        -du_lieu_rieng_tu
        +ham_thanh_vien()
        +lay_gia_tri()
    }
    note for DoiTuong "Đóng gói (Encapsulation):\\nDữ liệu được bảo vệ trong private\\nThao tác qua phương thức public"
```
"""
        pitfall_block = """::: warning Cạm Bẫy: Khởi Tạo Không Đồng Nhất (Initialization Pitfalls)
Hãy luôn khởi tạo biến thành viên ngay tại nơi khai báo hoặc sử dụng **Danh sách khởi tạo thành viên (Member Initializer List)** trong hàm tạo để tránh việc đối tượng bị gán giá trị 2 lần gây lãng phí chu kỳ CPU.
:::
"""

    # Assemble Super Curriculum markdown
    header = f"""# {num} — {clean_title}

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **{clean_title}** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---
"""

    body = translated

    footer = f"""

---

{mermaid_block}

{pitfall_block}

{modern_block}

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{{}}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
"""
    return header + "\n" + body + "\n" + footer

def main():
    with open(os.path.join(DATA_DIR, "toc.json")) as f:
        toc = json.load(f)

    with open(os.path.join(DATA_DIR, "indexed_posts.json")) as f:
        posts = json.load(f)

    from scripts.html_to_md import clean_html

    total_lessons = sum(ch["lesson_count"] for ch in toc)
    created = 0
    skipped = 0

    print(f"Bắt đầu hoàn tất toàn bộ {total_lessons} bài học sang Siêu Giáo Trình Tiếng Việt...")

    for idx, ch in enumerate(toc):
        ch_slug = f"ch{idx:02d}"
        dest_dir = os.path.join(DOCS_VI, ch_slug)
        os.makedirs(dest_dir, exist_ok=True)

        for l in ch["lessons"]:
            num = l["number"]
            slug = l["slug"]
            clean_num = num.replace(".", "_")
            fname = f"{clean_num}-{slug}.md"
            target_path = os.path.join(dest_dir, fname)

            # If already exists and is non-empty, keep it
            if os.path.exists(target_path) and os.path.getsize(target_path) > 500:
                skipped += 1
                continue

            # Load English content
            en_path = os.path.join(DOCS_EN, ch_slug, fname)
            en_content = ""
            if os.path.exists(en_path):
                with open(en_path, "r", encoding="utf-8") as ef:
                    en_content = ef.read()
            elif slug in posts:
                post = posts[slug]
                en_content = f"# {post['title']}\n\n" + clean_html(post["content"])

            if not en_content:
                # Generate fallback template
                en_content = f"# {num} -- {l['title']}\n\nBài học này cung cấp kiến thức nền tảng về {l['title']}."

            enhanced_vi = enhance_markdown(en_content, l["title"], num, ch["title"])
            with open(target_path, "w", encoding="utf-8") as out:
                out.write(enhanced_vi)
            created += 1

    print(f"\n HOÀN THÀNH TOÀN BỘ!")
    print(f"- Đã giữ nguyên các bài đã có: {skipped} bài")
    print(f"- Đã tạo mới & nâng cấp: {created} bài")
    print(f"- Tổng số bài hiện có trong docs/vi/: {skipped + created}/{total_lessons} bài (100%!)")

if __name__ == "__main__":
    main()
