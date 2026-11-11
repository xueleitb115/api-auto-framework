from selenium.webdriver.chrome.service import Service
from selenium import webdriver
# 直接自动下载驱动（小白必用）
driver = webdriver.Chrome()
# 1. 借工具：拿浏览器控制器
from selenium import webdriver
import time
# 2. 打开浏览器，起名字叫 driver
driver = webdriver.Chrome()
# 3. 打开网页
driver.get("https://www.baidu.com")
# 4. 等待2秒
time.sleep(2)
# 5. 关闭浏览器
driver.quit()
print("完成")
