import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 設定 Chrome 選項
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # 防止 Selenium 被偵測

# 啟動 WebDriver
driver = webdriver.Chrome(options=chrome_options)

# **1. 打開 Pimeyes 登入頁面**
driver.get("https://pimeyes.com/en/login")

# **2. 手動輸入帳密並登入**
print("🔴 請手動登入 Pimeyes...")
time.sleep(30)  # 等待 30 秒讓你手動登入

# **3. 登入成功後儲存 Cookie**
with open("cookies.pkl", "wb") as file:
    pickle.dump(driver.get_cookies(), file)

print("✅ Cookie 已儲存！")

# 關閉瀏覽器
driver.quit()
