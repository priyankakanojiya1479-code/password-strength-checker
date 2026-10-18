# ============================================================
# Password Strength Checker
# ============================================================
# Yeh program check karta hai ki aapka password kitna strong hai.
# Yeh 6 cheezein check karta hai:
#   1. Common passwords ki list (sabse pehle!)
#   2. Length (lambai)
#   3. Uppercase letters (BADE letters)
#   4. Lowercase letters (chote letters)
#   5. Numbers (ank)
#   6. Special characters (jaise @, #, !, $ etc.)
# ============================================================

import re       # regular expressions ke liye — pattern matching mein help karta hai
# NOTE: getpass hata diya — ab yeh module Flask web app ke through use hoga,
#       jahan browser khud password field ko hide karta hai (type="password").


# ============================================================
# COMMON PASSWORDS KI LIST
# ============================================================
# Yeh woh passwords hain jo duniya mein sabse zyada use hote hain.
# Hackers sabse pehle inhi ko try karte hain — isliye inhe KABHI use mat karo!
# Hum yahan ek list banate hain (set use kiya hai — searching fast hoti hai set mein).
# Aap is list mein aur passwords bhi add kar sakte ho.
COMMON_PASSWORDS = {
    "password", "password1", "password123", "password123!",
    "123456", "1234567", "12345678", "123456789", "1234567890",
    "111111", "000000", "123123", "654321",
    "qwerty", "qwerty123", "qwertyuiop",
    "abc123", "abcdef", "abcd1234",
    "iloveyou", "welcome", "monkey", "dragon",
    "master", "letmein", "sunshine", "princess",
    "admin", "admin123", "root", "toor",
    "pass", "pass123", "test", "test123",
    "hello", "hello123", "football", "shadow",
    "superman", "batman", "trustno1",
}
# ============================================================


def check_password_strength(password):
    """
    Is function mein password daalte hain aur yeh score + feedback return karta hai.
    Score 0 se 6 tak hota hai — jitna zyada utna strong.
    Agar password common list mein mila toh turant 'Weak' return hoga.
    """

    score = 0          # shuru mein score zero hoga
    feedback = []      # yahan suggestions store honge

    # ------------------------------------------------------------
    # CHECK 0: COMMON PASSWORD LIST (Sabse pehle yeh check hoga!)
    # ------------------------------------------------------------
    # .lower() isliye use kiya taaki "Password", "PASSWORD", "password"
    # teeno common list se match ho jayein — case ignore karte hain.
    if password.lower() in COMMON_PASSWORDS:
        # Agar common list mein mila toh aage kuch bhi check karne ki zaroorat nahi.
        # Seedha return kar do — score 0, strength "Weak".
        feedback.append("❌ Yeh ek bahut common password hai! Hackers sabse pehle ise hi try karte hain.")
        feedback.append("💡 Kuch alag aur unique password choose karo.")
        return 0, "🔴 Bahut Kamzor (Very Weak) — Common Password!", feedback

    # ------------------------------------------------------------
    # CHECK 1: LENGTH (Lambai)
    # ------------------------------------------------------------
    # Ek strong password mein kam se kam 8 characters hone chahiye.
    # Agar 8 se zyada ho toh aur bhi acha.
    if len(password) >= 8:
        score += 1                        # score mein 1 add karo
        if len(password) >= 12:
            score += 1                    # 12+ characters pe bonus point
    else:
        feedback.append("❌ Password kam se kam 8 characters ka hona chahiye.")

    # ------------------------------------------------------------
    # CHECK 2: UPPERCASE LETTERS (Bade letters — A, B, C ...)
    # ------------------------------------------------------------
    # re.search() se hum check karte hain ki string mein koi bada letter hai ya nahi.
    # [A-Z] matlab koi bhi capital letter.
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Kam se kam ek BADA letter (A-Z) daalo.")

    # ------------------------------------------------------------
    # CHECK 3: LOWERCASE LETTERS (Chote letters — a, b, c ...)
    # ------------------------------------------------------------
    # [a-z] matlab koi bhi small letter.
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Kam se kam ek chota letter (a-z) daalo.")

    # ------------------------------------------------------------
    # CHECK 4: NUMBERS (Ank — 0 se 9 tak)
    # ------------------------------------------------------------
    # \d matlab koi bhi digit (0-9).
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Kam se kam ek number (0-9) daalo.")

    # ------------------------------------------------------------
    # CHECK 5: SPECIAL CHARACTERS (Khaas nishan — @, #, $, ! etc.)
    # ------------------------------------------------------------
    # [^a-zA-Z0-9] matlab koi bhi character jo letter ya number NAHI hai.
    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        feedback.append("❌ Kam se kam ek special character daalo (jaise @, #, $, !).")

    # ------------------------------------------------------------
    # STRENGTH LEVEL — score ke hisaab se level decide hota hai
    # ------------------------------------------------------------
    # Score 0-5 tak ho sakta hai (CHECK 1 mein 12+ pe 2 points milte hain,
    # isliye max 6 ho sakta hai — lekin hum 5+ ko "Very Strong" mante hain).
    if score <= 2:
        strength = "🔴 Bahut Kamzor (Very Weak)"
    elif score == 3:
        strength = "🟠 Kamzor (Weak)"
    elif score == 4:
        strength = "🟡 Theek-Thaak (Moderate)"
    elif score == 5:
        strength = "🟢 Strong"
    else:
        strength = "🟢 Bahut Strong (Very Strong)"

    return score, strength, feedback


def main():
    """
    Main function — user se password leta hai aur result dikhata hai.
    """
    print("=" * 50)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 50)

    # User se password input lete hain (terminal se — directly run karne ke liye)
    password = input("\nApna password daalo: ")

    # Password strength check karte hain
    score, strength, feedback = check_password_strength(password)

    # ------------------------------------------------------------
    # RESULT PRINT KARO
    # ------------------------------------------------------------
    print("\n--- RESULT ---")
    print(f"Password   : {'*' * len(password)}")   # password hide karte hain
    print(f"Score      : {score}/6")
    print(f"Strength   : {strength}")

    # Agar koi feedback ho toh print karo
    if feedback:
        print("\n--- SUDHAARNE KE LIYE SUGGESTIONS ---")
        for tip in feedback:
            print(f"  {tip}")
    else:
        print("\n✅ Wah! Aapka password bahut strong hai!")

    print("=" * 50)


# ------------------------------------------------------------
# ENTRY POINT
# ------------------------------------------------------------
# Yeh check karta hai ki yeh file directly run ho rahi hai ya
# kisi aur file ne import kiya hai. Direct run hone pe main() chalega.
if __name__ == "__main__":
    main()
