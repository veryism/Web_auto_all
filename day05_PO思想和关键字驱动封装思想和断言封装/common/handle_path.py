



#统一管理文件路径


from  pathlib import Path


log_path = Path(__file__).parent.parent / "output" / "web_wuto.log"

report_path = Path(__file__).parent.parent /  "output" / "allure_results"



image_path = Path(__file__).parent.parent /  "testdatas" / "yuansu.png"

print(image_path)