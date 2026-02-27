"""
===============
模块说明文档
===============

opt_ygjhqd:
    员工计划启动，
"""

def opt_ygjhqd(driver, time_out=0.5, wait_time=10):
    """
    员工计划启动
    :param driver: 浏览器驱动对象
    :param time_out: 每次点击操作之后的停顿时间，默认是0.5秒
    :param wait_time: 显示等待超时时间，默认10秒
    :return: None
    """
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    # 点击员工计划启动
    btn_ygjhqd = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//div[contains(text(),"员工计划启动")]'))
    )
    btn_ygjhqd.click()
    time.sleep(time_out)
    # 点击按部门查询
    btn_abmcx = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"按部门查询")]'))
    )
    btn_abmcx.click()
    time.sleep(time_out)
    # 点击年份输入框
    input_nf = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//div[contains(@class,"el-date-editor")]/input[@autocomplete="off"]'))
    )
    input_nf.click()
    time.sleep(time_out)
    # 点击年份选择2025
    btn_nf2025 = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//a[contains(text(),"2025")]'))
    )
    btn_nf2025.click()
    time.sleep(time_out)
    # 点击选择考核周期
    btn_xzkhzq = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//input[@placeholder="选择考核周期"]'))
    )
    btn_xzkhzq.click()
    time.sleep(time_out)
    # 点击2025年1月绩效考核
    btn_2025_1 = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"2025年1月绩效考核")]'))
    )
    btn_2025_1.click()
    time.sleep(time_out)
    # 点击考核方案
    btn_khfa = WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '(//input[@placeholder="请选择"])[1]'))
    )
    btn_khfa.click()
    time.sleep(time_out)
    btn_khfa.send_keys("全部门都能使用")
    time.sleep(time_out)
    # 鼠标移动到考核方案上
    btn_qbmdnsy= WebDriverWait(driver, wait_time).until(
        ec.element_to_be_clickable((By.XPATH, '//span[contains(text(),"全部门都能使用")]'))
    )
    btn_qbmdnsy.click()
    time.sleep(time_out)



    # 点击全部门都能使用
