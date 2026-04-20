# pages/dashboard_page.py
# ==========================================
# PAGE OBJECT - Dashboard Page (sau khi login thành công)
# ==========================================

class DashboardPage:
    """
    Page Object cho trang Dashboard sau khi login.
    
    ⚠️ Hoan: Inspect trang Dashboard để tìm locators
    """
    
    def __init__(self, page):
        self.page = page
        
        # ==========================================
        # LOCATORS - ⚠️ THAY BẰNG LOCATORS THẬT
        # ==========================================
        
        # Welcome message
        # VD: <span class="welcome-text">Welcome, Hoan!</span>
        self.welcome_message = page.get_by_role("heading", name="Home")
        # ↑ THAY bằng locator thật

        
        
        # User profile / avatar (chứng minh đã login)
        self.user_profile = page.get_by_role("img", name="User Avatar")
        # ↑ THAY bằng locator thật
        
        # Navigation menu
        self.nav_menu = page.get_by_test_id("sidebar-item-link-home")
        # ↑ THAY bằng locator thật
        
        # Logout button
        self.logout_button = page.get_by_test_id("toolbar-account-menu-signout-button")
        # ↑ THAY bằng locator thật

    # ==========================================
    # ACTIONS
    # ==========================================
    
    def get_welcome_text(self) -> str:
        """Lấy text welcome message"""
        self.welcome_message.wait_for(state="visible", timeout=10000)
        return self.welcome_message.text_content()
    
    def is_dashboard_loaded(self) -> bool:
        """Kiểm tra Dashboard đã load xong"""
        return self.welcome_message.is_visible()
    
    def get_current_url(self) -> str:
        """Lấy URL hiện tại"""
        return self.page.url
    
    def click_logout(self):
        """Click Logout"""
        self.logout_button.click()