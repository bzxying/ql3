import time

import click
import pyperclip
from playwright.sync_api import sync_playwright


@click.command()
@click.option('--account', help='帐号', required=True)
def run(account):
    with sync_playwright() as playwright:
        pyperclip.copy("")
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        # Go to https://plogin.m.jd.com/login/login?appid=300&returnurl=https%3A%2F%2Fwq.jd.com%2Fpassport%2FLoginRedirect%3Fstate%3D2404625993%26returnurl%3Dhttps%253A%252F%252Fhome.m.jd.com%252FmyJd%252Fnewhome.action%253Fsceneval%253D2%2526ufc%253D%2526&source=wq_passport
        page.goto('https://home.m.jd.com/myJd/home.action')
        page.fill('//html/body/div[1]/div/div[3]/p[1]/input', account)
        page.check("input[type=\"checkbox\"]")
        time.sleep(1)
        page.click("//html/body/div[1]/div/div[3]/p[2]/button")

        jsonData = {}
        # iCount = 0
        while True:
            for x in context.cookies():
                if x['name'] == 'pt_key':
                    jsonData['PT_KEY'] = x['value']
                    print("cookie.pt_key : " + x['value'])
                if x['name'] == 'pt_pin':
                    jsonData['PT_PIN'] = x['value']
                    print("cookie.pt_pin : " + x['value'])
            if 'PT_KEY' in jsonData and 'PT_PIN' in jsonData:
                break
            else:
                # iCount += 1
                if browser.is_connected():
                    page.wait_for_timeout(1 * 1000)
                else:
                    break

        # pyperclip.copy(json.dumps(jsonData))
        # pt_key=${ptKey};pt_pin=${ptPin}
        # context.storage_state(path="auth.json")
        context.close()
        browser.close()
        pyperclip.copy(f"pt_key={jsonData['PT_KEY']};pt_pin={jsonData['PT_PIN']};")
        return 0

if __name__ == '__main__':
    run()