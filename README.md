# 人资平台 UI 自动化测试

本项目用于对人资平台进行 Web UI 自动化测试，采用 Base-Page 模式，提高代码复用率

---

## 目录结构

```text
人资平台 UI 自动化测试/
├── README.md                      # 项目说明文档
├── requirements.txt               # Python依赖列表
├── .gitignore                     # Git忽略配置
├── src/                           # 核心源代码
│   ├── pages/                     # 页面对象层
│   │   ├── base_page.py           # 页面基类
│   │   ├── login_page.py          # 登录页面
│   │   └── home_page.py           # 首页页面
│   ├── actions/                   # 业务动作层
│   │   └── login_actions.py       # 登录业务流程
│   ├── components/                # 通用组件
│   │   └── header.py              # 页面头部组件
│   └── utils/                     # 工具类
│       ├── driver_factory.py      # 驱动工厂
│       ├── config.py              # 配置管理
│       ├── logger.py              # 日志工具
│       └── wait_utils.py          # 等待工具
├── tests/                         # 测试用例
│   ├── conftest.py                # pytest 配置
│   ├── login/                     # 登录模块测试
│   └── order/                     # 订单模块测试
├── resources/                     # 资源文件
│   ├── config/                    # 配置文件
│   │   ├── dev.yaml               # 开发环境
│   │   └── prod.yaml              # 生产环境
│   ├── testdata/                  # 测试数据
│   └── images/                    # 图片资源
├── reports/                       # 测试报告
│   ├── html/                      # HTML报告
│   ├── allure_raw/                # Allure 原始数据
│   └── logs/                      # 运行日志
├── scripts/                       # 脚本工具
│   ├── run.py                     # 运行脚本
│   └── docker_run.sh              # Docker 脚本