from playwright.sync_api import Playwright, sync_playwright, expect
import time
import re


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://digital-screen-cell.dev.inrobot.cloud/")
    page.goto("https://air-sso.dev.inrobot.cloud/?redirect=https%3A%2F%2Fdigital-screen-cell.dev.inrobot.cloud%2F&options={%22title%22:%22%E7%BB%86%E8%83%9E%E5%B7%A5%E5%8E%82%22,%22version%22:%221.1.1%22,%22expireTime%22:86400}")
    time.sleep(3)
    page.get_by_placeholder("请输入用户名").click()
    page.get_by_placeholder("请输入用户名").fill("admin")
    page.get_by_placeholder("请输入用户名").press("Tab")
    page.get_by_placeholder("请输入密码").fill("123456")
    # page.get_by_text("LDAP账号").click()
    # page.get_by_placeholder("请输入OA账号").click()
    # page.get_by_placeholder("请输入OA账号").fill("admin")
    # page.get_by_placeholder("请输入OA账号").press("Tab")
    # page.get_by_placeholder("请输入OA密码").fill("123456")
    page.get_by_role("button", name="登 录").click()
    num = 0
    while num <=1000:
        time.sleep(3)
        page.get_by_text("传代工作站").click()
        time.sleep(3)
        page.locator("span").first.click()
        page.get_by_text("配液工作站").click()
        time.sleep(3)
        page.locator("span").first.click()
        time.sleep(3)
        page.get_by_text("冻存/复苏工作站").click()
        time.sleep(3)
        page.locator("span").first.click()
        time.sleep(3)
        page.get_by_text("拆包工作站").click()
        time.sleep(3)
        page.locator("span").first.click()

        num +=1
        print(num)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
