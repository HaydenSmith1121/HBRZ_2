import time

from base.basic_opt import *
from base.process_opt import *

if __name__ == '__main__':
    # 创建浏览器驱动
    driver = create_driver("edge")
    # 打开首页
    open_page(driver, "http://192.168.1.25")
    # 登录
    login(driver,1.5)
    # 刷新一下,不然会白屏
    time.sleep(1)
    driver.refresh()
    # 进入绩效管理
    enter_jxgl(driver)
    # 进入绩效关系管理
    opt_jxgxgl(driver)
    # 进入考核方案管理
    opt_khfagl(driver)
    # 进入绩效流程管理
    opt_jxlcgl(driver)
    opt_ygjhqd(driver)
    # # 进入绩效考核监控
    # opt_jxkhjk(driver)
    # # 进入绩效结果管理
    # opt_jxjggl(driver)
    # # 进入绩效分析
    # opt_jxfx(driver)
    # # 进入领导人员考核
    # opt_ldrykh(driver)

    time.sleep(50)
    driver.quit()
