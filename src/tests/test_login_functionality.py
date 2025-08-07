from playwright.sync_api import sync_playwright

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com/login")
        
        # Fill the login form
        page.fill("input[name='username']", "testuser")
        page.fill("input[name='password']", "securepassword123")
        page.click("button[type='submit']")
        
        # Validate login success (example condition)
        assert page.url == "https://example.com/dashboard"
        browser.close()
