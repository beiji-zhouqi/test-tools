from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.locator("#kw").click()
    page.locator("#kw").fill("playwright")
    page.get_by_role("button", name="百度一下").click()
    page.screenshot(path='1.png')
    time.sleep(2)
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="playwright教程 (一)适合小白_小白白学爬虫的博客-CSDN博客").click()
        page.screenshot(path='2.png')
    page1 = page1_info.value
    page.screenshot(path='3.png')
    time.sleep(1)
    page1.close()
    time.sleep(1)
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
