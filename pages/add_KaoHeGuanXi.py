import csv
import time

import yaml

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

with open("../config/config.yaml", "r", encoding="utf-8") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

options = Options()
options.binary_location = config['chrome_path']
# options.add_argument("--start-maximized")
# 启用无头模式
options.add_argument("--headless")
# 设置窗口大小（无头模式必需）
options.add_argument("--window-size=1920,1080")
service = Service()
service.executable_path = config['chromedriver_path']
driver = webdriver.Chrome(service=service, options=options)

def start(dr):

    # 打开测试环境
    dr.get(config['test_url'])

    # 设置隐式等待的最大时间是10秒
    dr.implicitly_wait(10)
    return dr


# 登录绩效管理员账号
def admin_login(driver):
    # 输入用户名
    input_username = driver.find_element(By.XPATH, '//input[@class="el-input__inner"][@placeholder="用户名"]')
    input_username.send_keys(config['username']['袁苏苏'])

    # 输入密码
    input_password = driver.find_element(By.XPATH, '//input[@class="el-input__inner"][@placeholder="密码"]')
    input_password.send_keys(config['password']['p2'])

    # 点击登录
    login_button = driver.find_element(By.XPATH,
                                       '//button[contains(@class,"el-button") and contains(@class,"login-btn")]')
    login_button.click()
    time.sleep(2)

    # 登录之后会跳转到别的系统的一个报表看板，需要修正url
    # 如果在登陆后使用driver.get重新打开一个网页是不行的，因为重新打开一个网页不会携带session,所以需要用javascript跳转
    current_url = driver.current_url

    # 修正URL
    if "/center4perspectiveweb-app/cockpit" in current_url:
        # 删除多余部分，得到基础URL
        base_url = current_url.split("/center4perspectiveweb-app/cockpit")[0] + "/"
        # 使用JavaScript跳转，会保持登录状态
        driver.execute_script(f"window.location.href = '{base_url}';")
    time.sleep(1)


# 进入绩效管理
def enter_jxgl(driver):
    # 点击人业协同中心
    btn_ryxtzx = driver.find_element(By.XPATH, '//div[@class="el-submenu__title"]')
    btn_ryxtzx.click()
    time.sleep(0.5)

    # 点击绩效管理,进入绩效管理页面
    btn_jxgl = driver.find_element(By.XPATH, '//li[contains(text(),"绩效管理")]')
    btn_jxgl.click()
    time.sleep(0.5)

    # 点击菜单栏里面的绩效管理
    btn_jxgl_2 = driver.find_element(By.XPATH, '//span[contains(text(),"绩效管理")]')
    btn_jxgl_2.click()
    time.sleep(0.5)

    # 点击绩效关系管理
    btn_jxgxgl = driver.find_element(By.XPATH, '//span[contains(text(),"绩效关系管理")]')
    btn_jxgxgl.click()
    time.sleep(0.5)

    # 点击考核配置
    btn_khpz = driver.find_element(By.XPATH, '//li/span[contains(text(),"考核配置")]')
    btn_khpz.click()
    time.sleep(0.5)


# 配置考核关系
def khpz(driver, bkh_ygbh, bkh_ygxm, kh_ygbh, kh_ygxm):
    # 点击考核关系配置
    btn_khgxpz = driver.find_element(By.XPATH, '//div[@id="tab-relation"]')
    btn_khgxpz.click()
    time.sleep(0.5)

    # 点击新增
    btn_xz = driver.find_element(By.XPATH, '//span[contains(text(),"新增")]')
    btn_xz.click()
    time.sleep(0.5)

    # 点击选择年份
    btn_xznf = driver.find_elements(By.XPATH, '//input[@placeholder="选择年份"]')
    # 点击第二个元素
    btn_xznf[1].click()
    time.sleep(0.5)

    # 点击2025年
    btn_2025 = driver.find_elements(By.XPATH, '//a[@class="cell"][contains(text(),"2025")]')
    btn_2025[0].click()
    time.sleep(0.5)

    # 点击选择考核周期
    btn_xzkhzq = driver.find_element(By.XPATH, '//input[@placeholder="选择考核周期"]')
    btn_xzkhzq.click()
    time.sleep(0.5)

    # 点击1月
    btn_1_month = driver.find_elements(By.XPATH, '//span[contains(text(),"2025年1月绩效考核")]')
    btn_1_month[0].click()
    time.sleep(0.5)

    # 点击新增被考核人
    btn_xzbe = driver.find_elements(By.XPATH, '//span[contains(text(),"新增")]')
    btn_xzbe[1].click()
    time.sleep(0.5)

    # 输入员工编号！！！写死
    input_ygbh = driver.find_elements(By.XPATH, '//input[@placeholder="请输入"]')
    input_ygbh[2].send_keys(bkh_ygbh)
    time.sleep(0.5)

    # 输入员工姓名！！！写死
    input_ygxm = driver.find_elements(By.XPATH, '//input[@placeholder="请输入"]')
    input_ygxm[3].send_keys(bkh_ygxm)
    time.sleep(0.5)

    # 点击查找
    btn_cz = driver.find_element(By.XPATH, '//span[contains(text(),"查找")]')
    btn_cz.click()
    time.sleep(0.5)

    # 勾选第一个查找到的结果
    btn_gx = driver.find_elements(By.XPATH, '//span[@class="el-checkbox__inner"]')
    btn_gx[3].click()
    time.sleep(0.5)

    # 点击确定
    btn_qd = driver.find_elements(By.XPATH, '//span[contains(text(),"确定")]')
    btn_qd[2].click()
    time.sleep(0.5)

    # 点击新增考核人
    btn_xzkh = driver.find_elements(By.XPATH, '//span[contains(text(),"新增")]')
    btn_xzkh[2].click()
    time.sleep(0.5)

    # 输入员工编号
    input_ygbh = driver.find_elements(By.XPATH, '//input[@placeholder="请输入"]')
    input_ygbh[4].send_keys(kh_ygbh)
    time.sleep(0.5)

    # 输入员工姓名
    input_ygxm = driver.find_elements(By.XPATH, '//input[@placeholder="请输入"]')
    input_ygxm[5].send_keys(kh_ygxm)
    time.sleep(0.5)

    # 点击查找
    btn_cz = driver.find_elements(By.XPATH, '//span[contains(text(),"查找")]')
    btn_cz[1].click()
    time.sleep(0.5)

    # 勾选第一个查找到的结果
    btn_gx = driver.find_elements(By.XPATH, '//span[@class="el-checkbox__inner"]')
    btn_gx[4].click()
    time.sleep(0.5)

    # 点击确定
    btn_qd = driver.find_elements(By.XPATH, '//span[contains(text(),"确定")]')
    btn_qd[2].click()
    time.sleep(0.5)

    # 勾选目标审核和打分
    btn_gx1 = driver.find_elements(By.XPATH, '//span[@class="el-checkbox__inner"]')
    btn_gx1[3].click()
    btn_gx1[4].click()
    time.sleep(0.5)

    # 输入权重为100
    input_srqz = driver.find_elements(By.XPATH,
                                      '//div[@class="el-input el-input--small"]/input[@class="el-input__inner"]')
    input_srqz[0].send_keys("100")
    time.sleep(0.5)

    # 点击保存
    btn_bc = driver.find_elements(By.XPATH, '//span[contains(text(),"保存")]')
    btn_bc[0].click()
    time.sleep(0.5)

    # 等待错误弹窗
    try:
        # 等待错误弹窗出现（最长5秒）
        error_toast = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@role='alert' and contains(@class, 'el-message--error')]"))
        )
        print(error_toast.text)
        # 点击取消
        btn_qx = driver.find_elements(By.XPATH, '//span[contains(text(),"取消")]')
        btn_qx[1].click()
        time.sleep(0.5)
    except:
        print(bkh_ygxm+"的考核关系配置成功")



with open("../res/emp_info_test.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name = row[0]
        username = row[1]
        driver = start(driver)
        admin_login(driver)
        enter_jxgl(driver)
        khpz(driver, username, name, "00245064", "袁苏芳")
        driver.quit()
