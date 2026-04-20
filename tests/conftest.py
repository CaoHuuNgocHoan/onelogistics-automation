# tests/conftest.py
# ==========================================
# PYTEST FIXTURES - Setup & Teardown
# ==========================================
# File này chạy TỰ ĐỘNG trước/sau mỗi test
# ==========================================

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from data.test_data import LOGIN_URL


@pytest.fixture(scope="function")
def login_page(page):
    """
    Fixture: Tạo LoginPage object và navigate đến trang Login
    - Chạy TRƯỚC mỗi test
    - 'page' là fixture có sẵn của pytest-playwright (tự tạo browser + page)
    """
    login = LoginPage(page)
    login.navigate(LOGIN_URL)
    return login


@pytest.fixture(scope="function")
def dashboard_page(page):
    """
    Fixture: Tạo DashboardPage object
    """
    return DashboardPage(page)