import time
from playwright.sync_api import Playwright, sync_playwright
from datetime import datetime


def write_log(log_info):
    with open('chy.log', 'a+') as file:
        file.write(log_info)


def run(playwright: Playwright) -> None:
    try:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://chyvpn.cyou/")
        time.sleep(3)
        page.get_by_role("link", name="登陆").click()
        time.sleep(3)
        page.locator("#email").click()
        page.locator("#email").fill("beiji.zhouqi@gmail.com")
        page.locator("#password").click()
        page.locator("#password").fill("Hellobeiji123@.")
        time.sleep(3)
        page.get_by_role("button", name="登录").click()
        time.sleep(5)
        page.get_by_role("button", name=" 每日签到").click()
        time.sleep(3)
        page.get_by_role("button", name="OK").click()

        write_log(f"{datetime.now().strftime('%Y%m%d')}" + "run success.\n")
    except Exception as e:
        write_log(f"{datetime.now().strftime('%Y%m%d')}" + "run fail.\n")
    finally:
        # ---------------------
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)
