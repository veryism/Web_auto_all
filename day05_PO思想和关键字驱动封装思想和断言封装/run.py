import sys

import pytest



from loguru import logger

from common.handle_path import log_path,report_path

logger.add(
    sink=log_path,
    encoding="utf-8",
    level="INFO",
    rotation="20 MB",

)

pytest.main(["-s","-v","--clean-alluredir",f"--alluredir={report_path}","--reruns=1","--reruns-delay=5"])