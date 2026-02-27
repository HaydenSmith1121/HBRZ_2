"""
===============
模块说明文档
===============

create_driver:
    创建 webdriver 对象
open_page:
    打开网页
login:
    登录系统
enter_jxgl:
    进入绩效管理模块
enter_xcgl:
    进入薪酬管理
opt_jxgxgl:
    操作绩效关系管理
opt_khfagl:
    操作考核方案管理
opt_jxlcgl:
    操作绩效流程管理
opt_jxkhjk:
    操作绩效考核监控
opt_jxjggl:
    操作绩效结果管理
opt_jxfx:
    操作绩效分析
opt_ldrykh:
    操作领导人员考核
"""


def opt_ldrykh(driver, opt_num=1, time_out=0.5, wait_time=10):
    """
    操作领导人员考核
    :param driver: 浏览器驱动对象
    :param opt_num: 选择要操作的板块，1对应领导人员考核发起，默认是1
    :param time_out: 每次点击操作之后的停顿时间，默认是0.5秒
    :param wait_time: 显示等待超时时间，默认10秒
    :return: None
    """
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    # 点击领导人员考核
    btn_ldrykh = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"领导人员考核")]'))
    )
    btn_ldrykh.click()
    time.sleep(time_out)
    if opt_num == 1:
        # 点击领导人员考核发起
        btn_ldrykhfq = WebDriverWait(driver, wait_time).until(
            ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"领导人员考核发起")]'))
        )
        btn_ldrykhfq.click()
        time.sleep(time_out)
    else:
        print("请输入正确的操作编号")


def opt_jxfx(driver, time_out=0.5, wait_time=10):
    """
    操作绩效分析
    :param driver: 浏览器驱动对象
    :param time_out: 每次点击操作之后的停顿时间，默认是0.5秒
    :param wait_time: 显示等待超时时间，默认10秒
    :return: None
    """

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    # 点击绩效分析
    btn_jxfx = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"绩效分析")]'))
    )
    btn_jxfx.click()
    time.sleep(time_out)


def opt_jxjggl(driver, opt_num=1, time_out=0.5, wait_time=10):
    """
    操作绩效结果管理
    :param driver: 浏览器驱动对象
    :param opt_num: 选择要操作的板块，1对应员工结果查看，2对应我的绩效，默认是1
    :param time_out: 每次点击操作之后的停顿时间，默认是0.5秒
    :param wait_time: 显示等待超时时间，默认10秒
    :return: None
    """

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    # 点击绩效结果管理
    btn_jxgl = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"绩效结果管理")]'))
    )
    btn_jxgl.click()
    time.sleep(time_out)

    if opt_num == 1:
        # 点击员工结果查看
        btn_rgjgck = WebDriverWait(driver, wait_time).until(
            ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"员工结果查看")]'))
        )
        btn_rgjgck.click()
        time.sleep(time_out)
    elif opt_num == 2:
        # 点击我的绩效
        btn_wdjx = WebDriverWait(driver, wait_time).until(
            ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"我的绩效")]'))
        )
        btn_wdjx.click()
        time.sleep(time_out)


def opt_jxkhjk(driver, opt_num=1, time_out=0.5, wait_time=10):
    """
    操作绩效考核监控
    :param driver: 浏览器驱动对象
    :param opt_num: 选择要操作的板块，1对应人员考核监控，2对应流程监控，默认是1
    :param time_out: 每次点击操作之后的停顿时间，默认是0.5秒
    :param wait_time: 显示等待超时时间，默认10秒
    :return: None
    """

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    # 点击绩效考核监控
    btn_jxkhjk = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"绩效考核监控")]'))
    )
    btn_jxkhjk.click()
    time.sleep(time_out)

    if opt_num == 1:
        # 点击人员考核监控
        btn_rykhjk = WebDriverWait(driver, wait_time).until(
            ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"人员考核监控")]'))
        )
        btn_rykhjk.click()
    elif opt_num == 2:
        # 点击流程监控
        btn_lcjk = WebDriverWait(driver, wait_time).until(
            ec.element_to_be_clickable((By.XPATH, "//span[contains(text(),'流程监控')]"))
        )
        btn_lcjk.click()
    else:
        print("请输入正确的操作编号")


def opt_jxlcgl(driver, opt_num=1, time_out=0.5, wait_time=10):
    """
    操作绩效流程管理
    :param driver: 浏览器驱动对象
    :param opt_num: 选择要操作的板块，1对应人员绩效考核，默认是1
    :param time_out: 每次点击操作之后的停顿时间，默认是0.5秒
    :param wait_time: 显示等待超时时间，默认10秒
    :return: None
    """

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    # 点击绩效流程管理
    btn_jxlcgl = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"绩效流程管理")]'))
    )
    btn_jxlcgl.click()
    time.sleep(time_out)

    if opt_num == 1:
        # 点击人员绩效考核
        btn_ryjxkh = WebDriverWait(driver, wait_time).until(
            ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"人员绩效考核")]'))
        )
        btn_ryjxkh.click()
    else:
        print("请输入正确的操作编号")


def create_driver(browser="chrome", headless=False, config="../config/config.yaml"):
    """
    创建一个 Selenium WebDriver 实例
    根据指定的浏览器类型和是否无头模式，返回对应的 driver 对象
    :param browser: 浏览器类型，支持 "chrome" 或者 "edge" 或者 "firefox", 默认为 "chrome"
    :param headless: 是否以无头模式运行，默认为 False
    :param config: 配置浏览器和浏览器驱动相关信息,默认为 config 文件的相对位置
    :return: 配置好的 WebDriver 对象
    """

    import yaml
    with open(config, "r", encoding="utf-8") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    if browser == "chrome":
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from selenium import webdriver
        options = Options()
        options.add_argument("inprivate")
        if headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")
        service = Service()
        service.executable_path = config['chromedriver_path']
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    # 其他浏览器先不处理
    elif browser == "edge":
        from selenium.webdriver.edge.options import Options
        from selenium.webdriver.edge.service import Service
        from selenium import webdriver
        options = Options()
        options.add_argument("inprivate")
        # 添加此实验性选项，可以让浏览器在脚本运行完后不自动关闭，方便观察结果
        options.add_experimental_option("detach", True)
        if headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")
        service = Service()
        service.executable_path = config['edgedriver_path']
        driver = webdriver.Edge(service=service, options=options)
        return driver
    else:
        print("不支持的浏览器类型")
        return None


def open_page(driver, url):
    """
    打开指定页面
    :param driver: 浏览器驱动对象
    :param url: 要打开的页面地址
    :return: None
    """

    driver.get(url)


def login(driver, time_out=1, emp_num="00245064", password="mhMH12@@"):
    """
    登录系统
    :param driver: 浏览器驱动对象
    :param emp_num: 员工编号,默认是 00245064
    :param password: 密码,默认是 mhMH12@@
    :param time_out: 每次点击操作之后的停顿时间，默认是0.5秒
    :return: None
    """

    import time
    from selenium.webdriver.common.by import By

    # 输入用户名
    input_username = driver.find_element(By.XPATH, '//input[@class="el-input__inner"][@placeholder="用户名"]')
    input_username.send_keys(emp_num)

    # 输入密码
    input_password = driver.find_element(By.XPATH, '//input[@class="el-input__inner"][@placeholder="密码"]')
    input_password.send_keys(password)

    # 点击登录
    login_button = driver.find_element(By.XPATH,
                                       '//button[contains(@class,"el-button") and contains(@class,"login-btn")]')
    login_button.click()
    time.sleep(time_out)

    # 登录之后会跳转到别的系统的一个报表看板，需要修正url
    current_url = driver.current_url

    # 修正URL
    if "/center4perspectiveweb-app/cockpit" in current_url:
        # 删除多余部分，得到基础URL
        base_url = current_url.split("/center4perspectiveweb-app/cockpit")[0] + "/"
        # 使用JavaScript跳转，会保持登录状态
        driver.execute_script(f"window.location.href = '{base_url}';")


def enter_jxgl(driver, time_out=0.5, wait_time=10):
    """
    进入绩效管理
    :param driver: 浏览器驱动对象
    :param time_out: 每次点击操作之后的停顿时间，默认是0.5秒
    :param wait_time: 显示等待超时时间，默认10秒
    :return: None
    """

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    # 点击人业协同中心
    btn_ryxtzx = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//i/parent::div[contains(text(), "人业协同中心")]'))
    )
    btn_ryxtzx.click()
    time.sleep(time_out)

    # 点击绩效管理,进入绩效管理页面
    btn_jxgl1 = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//li[contains(text(),"绩效管理")]'))
    )
    btn_jxgl1.click()
    time.sleep(time_out)

    # 点击菜单栏里面的绩效管理
    btn_jxgl2 = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"绩效管理")]'))
    )
    btn_jxgl2.click()
    time.sleep(time_out)


def enter_xcgl(driver, time_out=0.5, wait_time=10):
    """
    进入薪酬管理
    :param driver: 浏览器驱动对象
    :param time_out: 每次点击操作之后的停顿时间，默认是0.5秒
    :param wait_time: 显示等待超时时间，默认10秒
    :return: None
    """

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    # 点击人业协同中心
    btn_ryxtzx = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//div[contains(text(),"人业协同中心")]'))
    )
    btn_ryxtzx.click()
    time.sleep(time_out)

    # 点击薪酬管理,进入薪酬管理页面
    btn_xcgl = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//li[contains(text(),"薪酬管理")]'))
    )
    btn_xcgl.click()


def opt_jxgxgl(driver, opt_num=4, time_out=0.5, wait_time=10):
    """
    操作绩效关系管理
    :param driver: 浏览器驱动对象
    :param opt_num: 选择要操作的板块，1对应组织人员维护，2对应参数配置，3对应绩效数据权限，4对应考核配置，默认是4
    :param time_out: 每次点击操作之后的停顿时间，默认是0.5秒
    :param wait_time: 显示等待超时时间，默认10秒
    :return: None
    """

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    # 点击绩效关系管理
    btn_jxgxgl = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"绩效关系管理")]'))
    )
    btn_jxgxgl.click()
    time.sleep(time_out)

    if opt_num == 1:
        # 点击组织人员维护
        pass
    elif opt_num == 2:
        # 点击参数配置
        pass
    elif opt_num == 3:
        # 点击绩效数据权限
        pass
    elif opt_num == 4:
        # 点击考核配置
        btn_khpz = WebDriverWait(driver, wait_time).until(
            ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"考核配置")]'))
        )
        btn_khpz.click()
    else:
        print("请输入正确的操作编号")


def opt_khfagl(driver, opt_num=2, time_out=0.5, wait_time=10):
    """
    操作考核方案管理
    :param driver: 浏览器驱动对象
    :param opt_num: 选择要操作的板块，1对应考核周期定义，2对应基础配置，3对应绩效等级配置，默认是2
    :param time_out: 每次点击操作之后的停顿时间，默认是0.5秒
    :param wait_time: 显示等待超时时间，默认10秒
    :return: None
    """

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec

    # 点击考核方案管理
    btn_khgxgl = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"考核方案管理")]'))
    )
    btn_khgxgl.click()
    time.sleep(time_out)

    if opt_num == 1:
        # 点击考核周期定义
        pass
    elif opt_num == 2:
        # 点击基础配置
        btn_jcpz = WebDriverWait(driver, wait_time).until(
            ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"基础配置")]'))
        )
        btn_jcpz.click()
    elif opt_num == 3:
        # 点击绩效等级配置
        pass
    else:
        print("请输入正确的操作编号")
