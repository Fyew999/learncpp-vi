# 24.x — Tổng Kết Chương 24 & Bài Kiểm Tra Toàn Diện

---

## 🎯 Mục Tiêu
- Hệ thống hóa toàn bộ kiến thức về Tính Kế Thừa (Inheritance) trong C++.
- Đánh giá khả năng vận dụng qua bài tập lập trình hướng đối tượng thực chiến.

---

## 1. Tóm Tắt Các Khái Niệm Trọng Tâm

1. **Quan hệ "is-a"**: Lớp con là một phiên bản mở rộng chuyên biệt của lớp cha.
2. **Thứ tự Construction/Destruction**: Cha sinh trước Con, Con chết trước Cha.
3. **Gọi Constructor Cha**: Luôn gọi tường minh trong Member Initializer List của lớp con.
4. **Phạm vi truy cập**: `protected` cho phép lớp con truy cập nhưng giấu với bên ngoài.
5. **Đa kế thừa**: Cẩn trọng tuyệt đối với bài toán kim cương (The Diamond Problem).

---

## 2. Bài Tập Thực Chiến Toàn Diện: Hệ Thống Game Nhập Vai (RPG)

### Yêu cầu:
1. Xây dựng lớp cơ sở `Creature` có:
   - Tên (`std::string`), Lượng máu tối đa (`int`), Sát thương cơ bản (`int`).
   - Các phương thức: `getName()`, `getHp()`, `getDamage()`, `reduceHp(int damage)`, `isDead()`.
2. Xây dựng lớp dẫn xuất `Player` kế thừa từ `Creature`:
   - Bổ sung cấp độ `m_level{ 1 }`.
   - Phương thức `levelUp()`: Tăng cấp độ và tăng máu, sát thương.
3. Xây dựng lớp dẫn xuất `Monster` kế thừa từ `Creature`:
   - Bổ sung loại quái vật `enum class Type { Dragon, Orc, Slime }`.
4. Viết hàm `main()` mô phỏng một hiệp chiến đấu giữa Player và Dragon.

<details>
<summary><b>Xem lời giải mã nguồn hoàn chỉnh</b></summary>

```cpp
#include <iostream>
#include <string>
#include <string_view>

class Creature
{
protected:
    std::string m_name;
    int m_hp;
    int m_damage;

public:
    Creature(std::string_view name, int hp, int damage)
        : m_name{ name }, m_hp{ hp }, m_damage{ damage }
    {
    }

    const std::string& getName() const { return m_name; }
    int getHp() const { return m_hp; }
    int getDamage() const { return m_damage; }

    void reduceHp(int damage)
    {
        m_hp -= damage;
        if (m_hp < 0) m_hp = 0;
    }

    bool isDead() const { return m_hp <= 0; }
};

class Player : public Creature
{
private:
    int m_level{ 1 };

public:
    Player(std::string_view name)
        : Creature{ name, 100, 20 } // Khoi tao Base: 100 HP, 20 Damage
    {
    }

    int getLevel() const { return m_level; }

    void levelUp()
    {
        ++m_level;
        m_hp += 30;
        m_damage += 10;
        std::cout << m_name << " da len CAP DO " << m_level << "! (HP: " << m_hp << ", DMG: " << m_damage << ")\n";
    }
};

class Monster : public Creature
{
public:
    enum class Type { Dragon, Orc, Slime };

private:
    Type m_type;

public:
    Monster(Type type)
        : Creature{ "", 0, 0 }, m_type{ type }
    {
        switch (m_type)
        {
        case Type::Dragon:
            m_name = "Rong Co Dai";
            m_hp = 150;
            m_damage = 35;
            break;
        case Type::Orc:
            m_name = "Chien Binh Orc";
            m_hp = 60;
            m_damage = 15;
            break;
        case Type::Slime:
            m_name = "Quai Chat Nhon";
            m_hp = 20;
            m_damage = 5;
            break;
        }
    }
};

int main()
{
    Player hero{ "Hiep Si Arthur" };
    Monster boss{ Monster::Type::Dragon };

    std::cout << "--- TRAN CHIEN BAT DAU ---\n";
    std::cout << hero.getName() << " (HP: " << hero.getHp() << ") VS " 
              << boss.getName() << " (HP: " << boss.getHp() << ")\n\n";

    // Hiep Si danh Boss
    boss.reduceHp(hero.getDamage());
    std::cout << hero.getName() << " chem " << boss.getName() << " mat " << hero.getDamage() << " HP!\n";
    std::cout << boss.getName() << " con lai " << boss.getHp() << " HP.\n\n";

    // Boss phan cong
    hero.reduceHp(boss.getDamage());
    std::cout << boss.getName() << " phun lua thieu dot " << hero.getName() << " mat " << boss.getDamage() << " HP!\n";
    std::cout << hero.getName() << " con lai " << hero.getHp() << " HP.\n\n";

    // Hiep si len cap
    hero.levelUp();

    return 0;
}
```
</details>

---

## 3. Bước Tiếp Theo
Kế thừa giúp tái sử dụng mã, nhưng sức mạnh thực sự của lập trình hướng đối tượng chỉ bùng nổ khi kết hợp với **Hàm Ảo và Tính Đa Hình (Virtual Functions & Polymorphism)** trong Chương 25!
