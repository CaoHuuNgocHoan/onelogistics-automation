# data/test_data.py
import os
from dotenv import load_dotenv

# Load biến từ file .env
load_dotenv()

# ==========================================
# URL
# ==========================================
BASE_URL = os.getenv("BASE_URL", "https://exxonhoan.360awareqa.com")
LOGIN_URL = f"{BASE_URL}/login"

# ==========================================
# CREDENTIALS — Lấy từ file .env (AN TOÀN)
# ==========================================
VALID_USERNAME = os.getenv("VALID_USERNAME")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")

# Invalid credentials (không cần giấu vì là data giả)
INVALID_USERNAME = "wrong@company.com"
INVALID_PASSWORD = "WrongPassword"
EMPTY_STRING = ""

# ==========================================
# EXPECTED VALUES
# ==========================================
DASHBOARD_URL_KEYWORD = "logistics/home"
HOME_PAGE_HEADING = "Home"                  # ← THÊM DÒNG NÀY
PAGE_TITLE_AFTER_LOGIN = "OneLogistics"
# ==========================================
# ERROR MESSAGES
LOGIN_ERROR_MESSAGE = "Username or password is"           # Sai username hoặc password
USERNAME_REQUIRED_MESSAGE = "Username is required."       # Để trống username
PASSWORD_REQUIRED_MESSAGE = "Password is required."       # Để trống password
