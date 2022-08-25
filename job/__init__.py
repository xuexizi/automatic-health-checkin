from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
import time
import random
import traceback
from config import Configuration
from selenium import webdriver
from mail import sendmail
from verification import verific


def daka():

    # 获取当天的配置
    config = Configuration.config
    config_today = config["rules"]["default"]
    print("生成每日的配置: ", config_today)

    # # 此处也可以用edge浏览器的driver，都是一样的
    # # 开始执行脚本
    # edge_options = webdriver.EdgeOptions()
    # edge_options.add_argument('--no-sandbox')
    # edge_options.add_argument('--headless')
    # edge_options.add_argument('--disable-gpu')
    #
    # # 程序自己找不到浏览器位置，需要手动添加
    # edge_options.binary_location = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    # driver = webdriver.Edge(options=edge_options)

    # 开始执行脚本
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # 有时程序自己找不到谷歌浏览器位置，需要自己修改(一般在Windows上运行时会需要，在docker里不用)
    # chrome_options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"

    driver = webdriver.Chrome(options=chrome_options)

    # 这两个网址都可以用
    driver.get(
       "http://ca.zucc.edu.cn/cas/login?service=http%3A%2F%2Fyqdj.zucc.edu.cn%2Ffeiyan_api%2Fh5%2Fhtml%2Fdaka%2Fdaka.html"
       # "http://ca.zucc.edu.cn/cas/login?service=http://yqdj.zucc.edu.cn/feiyan_api/h5/html/index/index.html"
    )

    try:
        # 找到登录框，输入账号密码
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(config["username"])
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(config["password"])
        time.sleep(random.randint(2, 4))

        # 模拟点击登录
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[5]/div/input[1]').click()
        time.sleep(random.randint(2, 4))
        print("登录成功")

        # 跳转
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])

        # 首先确认表单是否改变
        ret = verific(driver)
        if not ret:
            sendmail("打卡表单已修改，请手动打卡", config["email"])
            return

        # 2.自动定位
        pag = driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[2]/div[2]/div/div/input')
        driver.execute_script("arguments[0].removeAttribute('readonly')", pag)
        driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[2]/div[2]/div/div/input').send_keys(config_today["location"])
        time.sleep(random.randint(2, 4))

        # 3.今日是否在校？
        driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[3]/div[2]/div/div/li[1]/label/div[2]/div').click()
        time.sleep(random.randint(2, 4))

        # 4.近2天内是否曾经离杭？
        driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[4]/div[2]/div/div/li[2]/label/div[2]/div').click()
        time.sleep(random.randint(2, 4))

        # 5.近7天是否有国内高中低风险地区旅居史?
        driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[5]/div[2]/div/div/li[2]/label/div[2]/div').click()
        time.sleep(random.randint(2, 4))

        # 6.近7天是否有（或被告知有）与疑似、确诊人员或密切接触者的接触史?
        driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[6]/div[2]/div/div/li[2]/label/div[2]/div').click()
        time.sleep(random.randint(2, 4))

        # 7.现是否处于健康管理（管控）期? 如是，请暂缓来校。
        driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[7]/div[2]/div/div/li[1]/label/div[2]/div').click()
        time.sleep(random.randint(2, 4))

        # 8.现身体状况，是否存在发热体温、寒战、咳嗽、胸闷以及呼吸困难等症状?
        driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[8]/div[2]/div/div/li[2]/label/div[2]/div').click()
        time.sleep(random.randint(2, 4))

        # 9.同住家属（人员）是否有上述与疫情相关的情况？
        driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[9]/div[2]/div/div/li[2]/label/div[2]/div').click()
        time.sleep(random.randint(2, 4))

        # 10.当前疫苗接种情况?-------------------
        driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[10]/div[2]/div/div/li[4]/label/div[2]/div').click()
        time.sleep(random.randint(2, 4))

        # 11.本人或家庭成员(包括其他亲密接触人员)是否有近10日入境或未来7天内拟入境的情况?
        driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[11]/div[2]/div/div/li[2]/label/div[2]/div').click()
        time.sleep(random.randint(2, 4))

        # 模拟点击提交
        driver.find_element(By.PARTIAL_LINK_TEXT, '提交').click()
        time.sleep(random.randint(2, 4))

        # 验证打卡成功
        if is_visible(driver, '//*[@class="modal-buttons "]/span'):
            driver.find_element(By.XPATH, '//*[@class="modal-buttons "]/span').click()
            print("打卡成功")
            sendmail("今日健康打卡成功", config["email"])
        else:
            print("打卡失败")
            sendmail("健康打卡失败，请手动打卡", config["email"])
    except Exception as e:
        print("打卡失败")
        sendmail("健康打卡失败，请手动打卡", config["email"])
        traceback.print_exc()
    finally:
        driver.quit()


# 一直等待某元素可见，默认超时10秒
def is_visible(driver, locator, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False
