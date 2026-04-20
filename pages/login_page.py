# pages/login_page.py
# ==========================================
# PAGE OBJECT - Login Page
# ==========================================
# Chứa tất cả elements và actions của trang Login
# ==========================================

class LoginPage:
    #"""
    #Page Object cho trang Login của OneLogistics.
    
    #⚠️ Hoan cần làm:
    #1. Mở trang Login trên Chrome
    #2. Click chuột phải vào ô Username → Inspect
    #3. Tìm id, name, hoặc placeholder của element
    #4. Thay vào các locator bên dưới
    #"""
    
    def __init__(self, page):
        self.page = page
        
        # ==========================================
        # LOCATORS - ⚠️ THAY BẰNG LOCATORS THẬT
        # ==========================================
        # Cách tìm locator:
        #   Chrome → F12 → Click icon 🔍 → Click vào element
        #   → Xem id, name, placeholder, class...
        #
        # Playwright hỗ trợ nhiều cách tìm element:
        #   page.locator("#id")              → tìm theo ID
        #   page.locator("[name='xxx']")     → tìm theo name
        #   page.get_by_placeholder("xxx")   → tìm theo placeholder
        #   page.get_by_role("button", name="xxx") → tìm theo role
        #   page.get_by_text("xxx")          → tìm theo text
        # ==========================================
        
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password") 
        self.login_button = page.get_by_role("button", name="Sign In")

        
        # Error message (hiện khi login sai)
        # VD: <div class="error-message">Invalid credentials</div>
        self.error_message = page.get_by_text("Username or password is") 
        
        
        # Logo hoặc title trang login (dùng để verify đã vào trang login)
        self.page_title = page.get_by_role("heading", name="Home")
       

        # ==========================================
        # LOCATORS — Error messages 
        # ==========================================

        # Sai username hoặc password
        self.login_error = page.get_by_text("Username or password is")

        # Để trống username
        self.username_required_error = page.get_by_text("Username is required.")

        # Để trống password
        self.password_required_error = page.get_by_text("Password is required.")


    # ==========================================
    # ACTIONS - Các hành động trên trang Login
    # ==========================================
    
    def navigate(self, url: str):
        """Mở trang Login"""
        self.page.goto(url)
    
    def fill_username(self, username: str):
        """Nhập username"""
        self.username_input.clear()
        self.username_input.fill(username)
    
    def fill_password(self, password: str):
        """Nhập password"""
        self.password_input.clear()
        self.password_input.fill(password)
    
    def click_login(self):
        """Click nút Login"""
        self.login_button.click()
    
    def login(self, username: str, password: str):
        """
        Action tổng hợp: Nhập username + password + click Login
        Đây là action được REUSE nhiều nhất
        """
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
    
    def get_error_message(self) -> str:
        """Lấy text error message"""
        self.error_message.wait_for(state="visible", timeout=5000)
        return self.error_message.text_content()
    
    def is_error_displayed(self) -> bool:
        """Kiểm tra error message có hiển thị không"""
        return self.error_message.is_visible()
    
    def is_login_page_loaded(self) -> bool:
        """Kiểm tra trang Login đã load xong chưa"""
        return self.username_input.is_visible() and \
               self.password_input.is_visible() and \
               self.login_button.is_visible()
    


    # ==========================================
    # CHECKS
    # ==========================================
    def is_login_error_displayed(self) -> bool:
        return self.login_error.is_visible()

    def is_username_required_displayed(self) -> bool:
        return self.username_required_error.is_visible()

    def is_password_required_displayed(self) -> bool:
        return self.password_required_error.is_visible()

    def is_login_page_loaded(self) -> bool:
        return self.username_input.is_visible() and \
               self.login_button.is_visible()


    
    #Error message

    def is_login_error_displayed(self) -> bool:
        """Check error khi sai username/password"""
        return self.login_error.is_visible()

    def is_username_required_displayed(self) -> bool:
        """Check error khi để trống username"""
        return self.username_required_error.is_visible()

    def is_password_required_displayed(self) -> bool:
        """Check error khi để trống password"""
        return self.password_required_error.is_visible()

    def is_login_page_loaded(self) -> bool:
        """Check trang Login đã load"""
        return self.username_input.is_visible() and \
               self.password_input.is_visible() and \
               self.login_button.is_visible()   