import sys

import pytest



from loguru import logger

from common.handle_path import log_path,report_path

import sys

logger.add(
    sink=log_path,
    encoding="utf-8",
    level="INFO",
    rotation="20 MB",

)

#测试地址:http://mall.lemonban.com:3344/"

#添加自定义命令参数--env-url

param = sys.argv[1] if len(sys.argv) > 1 else 'http://mall.lemonban.com:3344/'

pytest.main(["-s",
             "-v",
             "--clean-alluredir",
             f"--alluredir={report_path}",
             "--reruns=1",
             "--reruns-delay=5",
             f"--env-url={param}"])


