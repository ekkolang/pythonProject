import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 读取待查询的序列号列表
with open("ip_list.txt", "r") as f:
    sn_list = f.read().splitlines()

# 打开浏览器
driver = webdriver.Chrome()

# 循环遍历序列号列表并查询
with open("guarantee_info.txt", "w") as f:
    for sn in sn_list:
        # 打开查询页面
        driver.get(f"https://newthink.lenovo.com.cn/deviceGuarantee.html?selname={sn}")

        # 等待查询结果出现
        wait = WebDriverWait(driver, 10)
        time.sleep(2)
        warranty_info = driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div[5]/div[1]/div[4]/ul/li[2]/div[2]/div/div/div[4]/p[3]')
        warranty_info1 = driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div[5]/div[1]/div[4]/ul/li[1]/div[2]/div/div/div[3]/p[3]')

        # 获取查询结果文本并写入文件

        print(f"{sn}: {warranty_info1.text}----{warranty_info.text}")

# 关闭浏览器
driver.quit()
