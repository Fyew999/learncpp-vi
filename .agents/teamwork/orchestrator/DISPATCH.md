# Dispatch Log

## 2026-11-13T14:47:30Z
From: a69260af-05ba-4ff5-8688-6d0b29abf745

Dự án Siêu Giáo Trình C++ (LearnCpp Tiếng Việt): Điều phối nhóm biên soạn và nâng cấp toàn diện các chương còn lại (Chương 01 đến Chương 28, Phụ lục) theo tiêu chuẩn Siêu Giáo Trình, phục vụ xuất bản tài liệu học tập chuẩn mực (Production).

Working directory: /home/nam/Documents/learncpp
Integrity mode: development

## Requirements

### R1. Biên soạn toàn diện các chương còn lại
Dịch và biên soạn toàn bộ các bài học từ docs/en/ sang docs/vi/ cho tất cả các chương còn lại từ Chương 01 đến Chương 28 cùng các Phụ lục theo đúng cấu trúc mục lục data/toc.json. Các thuật ngữ kỹ thuật phải tuân thủ nghiêm ngặt bảng quy chuẩn docs/quy-chuan-thuat-ngu.md và chuẩn hóa theo ISO C++.

### R2. Nâng cấp chuẩn Siêu Giáo Trình
Nâng cấp nội dung từng bài học với các thành phần chuyên sâu: sơ đồ Mermaid trực quan hóa cơ chế bộ nhớ RAM (Stack, Heap, con trỏ, tham chiếu, vòng đời đối tượng), các callout box cảnh báo cạm bẫy và hành vi không xác định (Undefined Behavior - UB), cập nhật các tính năng và tiêu chuẩn hiện đại C++20/C++23, cùng ngân hàng câu hỏi Quiz và bài tập thực hành kèm lời giải chi tiết.

### R3. Tích hợp hệ thống tài liệu VitePress
Đảm bảo toàn bộ các file bài viết mới được tích hợp liền mạch vào cấu trúc VitePress hiện tại, duy trì cấu hình điều hướng và đồng bộ giao diện, tính năng với Chương 00 đã hoàn thành.

## Acceptance Criteria

### Độ bao phủ và cấu trúc tài liệu
- [ ] Toàn bộ các bài học thuộc Chương 01 đến Chương 28 và các Phụ lục được tạo đầy đủ file markdown tương ứng trong thư mục `docs/vi/` theo đúng cấu trúc `data/toc.json`.
- [ ] Không có file bài học nào bị bỏ sót hoặc để trống nội dung so với nguồn `docs/en/`.
- [ ] Cấu trúc sidebar và điều hướng tài liệu hiển thị đầy đủ liên kết tới toàn bộ các chương đã biên soạn.

### Tiêu chuẩn nội dung Siêu Giáo Trình
- [ ] Thuật ngữ chuyên môn trong tất cả các bài dịch tuân thủ bảng quy chuẩn tại `docs/quy-chuan-thuat-ngu.md`.
- [ ] Các bài học chứa giải thích cơ chế bộ nhớ có tích hợp sơ đồ Mermaid trực quan hóa vùng nhớ (Stack, Heap, biến, con trỏ).
- [ ] Mỗi bài học chứa ít nhất một hộp cảnh báo (callout box) về lỗi thường gặp hoặc cạm bẫy Undefined Behavior (UB) liên quan đến chủ đề bài học.
- [ ] Các tính năng mới từ C++20 và C++23 liên quan đến bài học được chú thích hoặc cập nhật vào phần lý thuyết và ví dụ code.
- [ ] Mỗi bài học có phần Quiz hoặc bài tập thực hành kèm đáp án và lời giải thích chi tiết.

### Kiểm thử và tính hợp lệ kỹ thuật
- [ ] Lệnh build tài liệu VitePress (`npm run docs:build`) thực thi thành công không có lỗi cú pháp markdown, lỗi render Mermaid, hoặc lỗi liên kết gãy.
- [ ] Tất cả các khối mã nguồn C++ (code blocks) tuân thủ cú pháp chuẩn C++20/C++23 và không chứa lỗi cú pháp biên dịch.
