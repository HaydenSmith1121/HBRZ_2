人资平台自动化测试代码

selenium-ui/
├─ pyproject.toml / requirements.txt
├─ README.md
├─ .env / config/
│  ├─ config.yaml
│  ├─ config.dev.yaml
│  └─ config.prod.yaml
├─ src/
│  └─ ui/
│     ├─ core/
│     │  ├─ driver_factory.py      # driver创建/参数化(本地/远程/grid)
│     │  ├─ base_page.py           # Page基类：find/click/type/wait/screenshot
│     │  ├─ waits.py               # 显式等待封装
│     │  ├─ logger.py              # 日志封装
│     │  ├─ exceptions.py          # 自定义异常
│     │  └─ utils.py               # 通用工具(时间、随机、文件等)
│     ├─ pages/
│     │  ├─ login_page.py
│     │  ├─ home_page.py
│     │  └─ ...
│     ├─ flows/                    # 业务流封装（可选但强烈建议）
│     │  ├─ auth_flow.py
│     │  ├─ order_flow.py
│     │  └─ ...
│     ├─ locators/                 # 定位器集中管理（可选）
│     │  ├─ login_locators.py
│     │  └─ ...
│     └─ data/
│        ├─ accounts.yaml
│        └─ testdata.yaml
├─ tests/
│  ├─ conftest.py                  # pytest fixture：driver、登录态、清理等
│  ├─ test_login.py
│  ├─ test_order.py
│  └─ ...
├─ artifacts/                      # 运行产物
│  ├─ screenshots/
│  ├─ logs/
│  └─ reports/
└─ scripts/
   ├─ run_local.sh
   └─ run_grid.sh