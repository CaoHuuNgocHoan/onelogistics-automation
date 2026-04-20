# tests/test_login.py
# ==========================================
# TEST CASES - Login Feature
# ==========================================
# Đây là file CHÍNH chứa tất cả test cases cho Login
# ==========================================
import re
from playwright.sync_api._generated import Page
import pytest
from playwright.sync_api import expect
from data.test_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD,
    EMPTY_STRING,
    DASHBOARD_URL_KEYWORD,
    HOME_PAGE_HEADING,
)

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


class TestLoginPositive:
    """
    ✅ POSITIVE TEST CASES - Login thành công
    """

    def test_login_with_valid_credentials(self, login_page: LoginPage, dashboard_page: DashboardPage, page: Page):
        """
        TC-LOGIN-001: Verify user can login with valid credentials
        
        Precondition: User is on Login page
        Steps:
            1. Enter valid username
            2. Enter valid password
            3. Click Login button
        Expected:
            - Redirect to Dashboard page
            - Welcome message is displayed
        """

        # Action
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        
        # Assertions
        # Verify URL chuyển đến Home
        expect(page).to_have_url(re.compile(f".*{DASHBOARD_URL_KEYWORD}.*"),
            timeout=20000
        )

        # # Assertion 2 — Verify heading "Home" hiển thị
        home_heading = page.get_by_role("heading", name="Home")
        expect(home_heading).to_be_visible(timeout=10000)

        # THÊM DÒNG NÀY — Đợi 5 giây để XEM kết quả trước khi tắt
        # page.wait_for_timeout(5000)   # 5000ms = 5 giây


    def test_login_page_elements_displayed(self, login_page: LoginPage, page: Page):
        """
        TC-LOGIN-002: Verify all login page elements are displayed
        
        Precondition: User navigates to Login page
        Steps:
            1. Observe Login page
        Expected:
            - Username field is visible
            - Password field is visible
            - Login button is visible
        """
        # Assertions
        # assert login_page.is_login_page_loaded(), \
        #     "All login page elements should be visible"
        # def test_login_page_elements_displayed(self, login_page: LoginPage, page: Page):
        # """
        # TC-LOGIN-002: Verify all login page elements are displayed
        # """
        # Assertion — Check từng element riêng lẻ
        expect(login_page.username_input).to_be_visible(timeout=10000)
        expect(login_page.login_button).to_be_visible(timeout=10000)
        
        # Check password bằng locator khác (vì type="password")
        password_field = page.locator("input[type='password']")
        expect(password_field).to_be_visible(timeout=10000)


class TestLoginNegative:
    """
    ❌ NEGATIVE TEST CASES - Login thất bại
    """

    def test_login_with_invalid_username(self, login_page):
        """
        TC-LOGIN-003: Verify error when login with invalid username
        
        Steps:
            1. Enter INVALID username
            2. Enter valid password
            3. Click Login
        Expected:
            - Error message is displayed
            - User stays on Login page
        """
        # Action
        login_page.login(INVALID_USERNAME, VALID_PASSWORD)
        
        # Assertion — Error message hiển thị
        expect(login_page.login_error).to_be_visible(timeout=10000)

    def test_login_with_invalid_password(self, login_page):
        """
        TC-LOGIN-004: Verify error when login with invalid password
        
        Steps:
            1. Enter valid username
            2. Enter INVALID password
            3. Click Login
        Expected:
            - Error message is displayed
        """
        # Action
        login_page.login(VALID_USERNAME, INVALID_PASSWORD)
        
        # Assertions
        expect(login_page.login_error).to_be_visible(timeout=10000)

    def test_login_with_empty_username(self, login_page):
        """
        TC-LOGIN-005: Verify error when username is empty
        
        Steps:
            1. Leave username empty
            2. Enter valid password
            3. Click Login
        Expected:
            - Validation error / Required field message
        """
        # Action
        login_page.login(EMPTY_STRING, VALID_PASSWORD)
        
        # Assertion — Username required message hiển thị
        expect(login_page.username_required_error).to_be_visible(timeout=10000)

    def test_login_with_empty_password(self, login_page):
        """
        TC-LOGIN-006: Verify error when password is empty
        
        Steps:
            1. Enter valid username
            2. Leave password empty
            3. Click Login
        Expected:
            - Validation error
        """
        # Action
        login_page.login(VALID_USERNAME, EMPTY_STRING)
        
        # Assertion — Password required message hiển thị
        expect(login_page.password_required_error).to_be_visible(timeout=10000)


    def test_login_with_all_empty_fields(self, login_page):
        """
        TC-LOGIN-007: Verify error when both fields are empty
        
        Steps:
            1. Leave username empty
            2. Leave password empty
            3. Click Login
        Expected:
            - Validation error
        """
        # Action
        login_page.login(EMPTY_STRING, EMPTY_STRING)
        
        # Assertion — CẢ 2 messages đều hiển thị
        expect(login_page.username_required_error).to_be_visible(timeout=10000)
        expect(login_page.password_required_error).to_be_visible(timeout=10000)


class TestLoginSecurity:
    """
    🔒 SECURITY TEST CASES
    """

    def test_password_field_is_masked(self, login_page):
        """
        TC-LOGIN-008: Verify password field is masked (type='password')
        
        Steps:
            1. Check password field type attribute
        Expected:
            - Input type = "password" (hiện *** thay vì plain text)
        """
        # Assertion
        password_type = login_page.password_input.get_attribute("type")
        assert password_type == "password", \
            f"Password field should be masked, but type is '{password_type}'"