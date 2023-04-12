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
        driver.get(f"https://www.inspur.com/eportal/ui?struts.portlet.action=/portlet/download-front!toView.action&pageId=2367231&index=2&product_id=6984&productSN={sn}")

        # 等待查询结果出现
        wait = WebDriverWait(driver, 10)
        time.sleep(2)
        warranty_info = driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/dl[4]/dd')
        warranty_info1 = driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/dl[6]/dd')

        # 获取查询结果文本并写入文件

        print(f"{sn}，{warranty_info.text}，{warranty_info1.text}")

# 关闭浏览器
driver.quit()
