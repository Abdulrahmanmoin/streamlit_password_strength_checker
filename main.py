import re
import streamlit as st
import random
import string

st.set_page_config(page_title="Password Strength Checker")
st.title("Password Strength Checker by Abdul Rahman")

def suggest_password():
    """Generate a strong random password with 13 characters."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(13))

# List of commonly used weak passwords
COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123", "password123",
    "12345678", "111111", "123123", "1234567890", "letmein", "welcome"
}

def check_password_strength(password):
    """Check the password strength and return suggestions."""
    errors = []

    # Blacklist Check
    if password.lower() in COMMON_PASSWORDS:
        return ["❌ This password is too common. Please choose a stronger one."]

    # Length Check
    if len(password) < 8:
        errors.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
        errors.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if not re.search(r"\d", password):
        errors.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if not re.search(r"[!@#$%^&*]", password):
        errors.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if not errors:
        return ["✅ Strong Password!"]
    else:
        suggested = suggest_password()
        errors.append(f"🔹 Suggested Strong Password: `{suggested}`")
        return errors

# Input field
password = st.text_input("Enter Password:", type="password")

if password:
    results = check_password_strength(password)
    for result in results:
        st.write(result)
