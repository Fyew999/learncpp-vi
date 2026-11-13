# 8.x — Tổng Kết Chương 08 & Bài Tập Toàn Diện (Chapter 8 Summary and Quiz)

---

## 🎯 Mục Tiêu Bài Học
- Hệ thống hóa toàn bộ kiến thức Chương 08: Rẽ nhánh (`if`, `switch`), Vòng lặp (`while`, `for`), Break/Continue, Dừng sớm, và Thư viện `<random>`.
- Thực hành xây dựng mini-game hoàn chỉnh "Đoán Số Bí Ẩn (Hi-Lo Game)".

---

## 📝 Dự Án Thực Chiến: Mini-Game Đoán Số Hi-Lo

Hãy viết chương trình trò chơi đoán số thỏa mãn các yêu cầu:
1. Máy tính tự động chọn một số bí mật ngẫu nhiên từ 1 đến 100.
2. Người chơi có 7 lượt đoán.
3. Sau mỗi lượt, nếu đoán sai, máy tính thông báo số đoán là "Quá lớn" hoặc "Quá nhỏ".
4. Nếu đoán đúng trong 7 lượt, người chơi chiến thắng! Ngược lại, máy tính thông báo thua cuộc và in số bí mật.
5. Sau khi kết thúc, hỏi người chơi có muốn chơi lại không (`y`/`n`).

::: details [Xem mã nguồn hoàn chỉnh]
```cpp
#include <iostream>
#include <random>

void playGame()
{
    std::random_device rd;
    std::mt19937 mt { rd() };
    std::uniform_int_distribution dist { 1, 100 };

    const int secretNumber { dist(mt) };
    constexpr int maxGuesses { 7 };

    std::cout << "Toi da chon 1 so tu 1 den 100. Ban co " << maxGuesses << " luot de doan!\n";

    for (int guessCount = 1; guessCount <= maxGuesses; ++guessCount)
    {
        std::cout << "Luot #" << guessCount << ": ";
        int guess {};
        std::cin >> guess;

        if (guess == secretNumber)
        {
            std::cout << "Chuc mung! Ban da doan chinh xac sau " << guessCount << " luot!\n";
            return;
        }
        else if (guess < secretNumber)
        {
            std::cout << "So cua ban qua nho!\n";
        }
        else
        {
            std::cout << "So cua ban qua lon!\n";
        }
    }

    std::cout << "Rat tiec, ban da het luot! So bi mat la: " << secretNumber << '\n';
}

int main()
{
    while (true)
    {
        playGame();

        std::cout << "Ban co muon choi lai khong? (y/n): ";
        char choice {};
        std::cin >> choice;

        if (choice != 'y' && choice != 'Y')
        {
            std::cout << "Cam on ban da choi game!\n";
            break;
        }
    }
    return 0;
}
```
:::
