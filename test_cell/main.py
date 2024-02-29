import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://digital-screen-cell.uat.inrobot.cloud/passage/microscope")
    # page.goto("https://platform-iam.uat.inrobot.cloud/api/#/?authRequestID=1cc73911-3227-483c-8031-3d6d7eddab5e&redirect=https%3A%2F%2Fdigital-screen-cell.uat.inrobot.cloud%2Fpassage%2Fmicroscope&options={%22title%22:%22%e7%bb%86%e8%83%9e%e5%b7%a5%e5%8e%82%22,%22version%22:%221.1.1%22,%22expireTime%22:86400}&code_verifier=MjA2ZTQ4ZGEtOTU5OC00YTM3LTlkZjMtYzI2YjVhM2UxNDgx")
    page.locator("div").filter(has_text=re.compile(r"^AIR云平台LDAP账号$")).get_by_role("img").nth(1).click()
    page.get_by_placeholder("请输入OA账号").click()
    page.get_by_placeholder("请输入OA账号").fill("zhouqi1")
    page.get_by_placeholder("请输入OA账号").press("Tab")
    page.get_by_placeholder("请输入OA密码").fill("Helloyinghe123@.")
    page.get_by_role("button", name="登 录").click()
    print("登录成功.")
    
    page.wait_for_timeout(10000)
    page.get_by_text("自动对焦测试", exact=True).click()
    page.get_by_role("button", name="确认").click()
    print(222222222222)
    page.locator("div").filter(has_text=re.compile(r"^微调照片1微调照片2微调照片3微调照片4$")).locator("img").first.click()
    num = 1
    while True:
        page.get_by_text("自动对焦测试", exact=True).click()
        page.get_by_role("button", name="确认").click()
        page.locator("div").filter(has_text=re.compile(r"^微调照片1微调照片2微调照片3微调照片4$")).locator("img").first.click()
        num += 1
        print(num)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
