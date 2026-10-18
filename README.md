# 🔐 Password Strength Checker

Ek simple Python project jo aapka password check karta hai aur batata hai ki woh kitna **strong** ya **weak** hai.  
Yeh project **do tarike** se use kar sakte ho — terminal se ya browser mein web app ke through.

---

## ✨ Features

- ✅ **Common password detection** — 35+ sabse common passwords ki list se check karta hai (jaise `123456`, `admin`, `password` etc.)
- ✅ **Length check** — 8+ characters pe point, 12+ pe bonus point
- ✅ **Uppercase check** — kam se kam ek BADA letter (A–Z)
- ✅ **Lowercase check** — kam se kam ek chota letter (a–z)
- ✅ **Number check** — kam se kam ek digit (0–9)
- ✅ **Special character check** — kam se kam ek nishan (`@`, `#`, `$`, `!` etc.)
- ✅ **Score system** — 0 se 6 tak score milta hai
- ✅ **Colored web UI** — strength ke hisaab se rang badalta hai (laal → hara)
- ✅ **Beginner-friendly comments** — har line pe Hindi mein explanation

---

## 📁 Project Structure

```
password-checker/
│
├── password_checker.py   ← Core logic — sab checks yahan hain
├── app.py                ← Flask web server
└── templates/
    └── index.html        ← Web page (form + colored result)
```

---

## 🚀 Run Karne Ke Steps

### Option 1 — Terminal se (simple, no install needed)

```bash
python password_checker.py
```

> Password daalo aur Enter dabao — result terminal mein dikhega.

---

### Option 2 — Web App (browser mein)

#### Step 1: Flask install karo

Agar Flask pehle se install nahi hai toh yeh command chalao:

```bash
pip install flask
```

> ✅ Ek baar install karne ke baad dobara karne ki zaroorat nahi.

#### Step 2: Server start karo

```bash
python app.py
```

Aapko kuch aisa dikhega:

```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

#### Step 3: Browser mein kholo

Apna browser kholo aur yeh address daalo:

```
http://127.0.0.1:5000
```

> Server band karna ho toh terminal mein **Ctrl + C** dabao.

---

## 🎨 Strength Levels

| Score | Level | Rang |
|-------|-------|------|
| 0 | Bahut Kamzor — Common Password! | 🔴 Laal |
| 1–2 | Bahut Kamzor (Very Weak) | 🔴 Laal |
| 3 | Kamzor (Weak) | 🟠 Narangi |
| 4 | Theek-Thaak (Moderate) | 🟡 Peela |
| 5 | Strong | 🟢 Hara |
| 6 | Bahut Strong (Very Strong) | 🟢 Gehra Hara |

---

## 🛠️ Requirements

| Cheez | Version |
|-------|---------|
| Python | 3.7 ya usse zyada |
| Flask | 2.0+ (sirf web app ke liye) |

Flask install check karne ke liye:

```bash
pip show flask
```

---

## 💡 Naye Common Passwords Kaise Add Karein?

[`password_checker.py`](password_checker.py) mein `COMMON_PASSWORDS` set mein apna password daalo:

```python
COMMON_PASSWORDS = {
    "password", "123456",
    "apna_naya_common_password",   # ← yahan add karo
    ...
}
```

---

## 📖 Seekhne Layak Concepts (Beginners ke liye)

Yeh project banate waqt yeh Python concepts use hue hain:

- `set` — fast lookup ke liye list ki jagah
- `re` module — pattern matching (regex)
- `def` — functions banana
- `return` — multiple values return karna
- **Flask** — Python se web app banana
- **Jinja2** — HTML mein Python data dalna (`{{ }}`, `{% %}`)
- `GET` vs `POST` — web forms ka basic
