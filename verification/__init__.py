from selenium.webdriver.common.by import By


def verific(driver):
    print("进入表单验证")

    text = driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[1]/div[1]').get_attribute('textContent')
    print(text)
    if text != "1.填报日期(Date)（必填）":
        return False

    text = driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[2]/div[1]').get_attribute('textContent')
    print(text)
    if text != "2.自动定位(Automatic location)（必填）":
        return False

    text = driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[3]/div[1]').get_attribute('textContent')
    print(text)
    if text != "3.今日是否在校？(Are you on campus today?)（必填）":
        return False

    text = driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[4]/div[1]').get_attribute('textContent')
    print(text)
    if text != "4.近2天内是否曾经离杭？(Did you ever leave Hangzhou in past two days?)（必填）":
        return False

    text = driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[5]/div[1]').get_attribute('textContent')
    print(text)
    if text != "5.近7天是否有国内高中低风险地区旅居史?( In the past 7 days, have you ever been to any low, medium or high risk areas?)（必填）":
        return False

    text = driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[6]/div[1]').get_attribute('textContent')
    print(text)
    if text != "6.近7天是否有（或被告知有）与疑似、确诊人员或密切接触者的接触史? (In the past 7 days，did you contact any COVID-19 suspected or confirmed person(s) or close contacts ?)（必填）":
        return False

    # 该表单项多一个空格
    text = driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[7]/div[1]').get_attribute('textContent')
    print(text)
    if text != "7.现是否处于健康管理（管控）期? 如是，请暂缓来校。(Are you under health management period currently ? If yes, please do not come to school for the time being.) （必填）":
        return False

    text = driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[8]/div[1]').get_attribute('textContent')
    print(text)
    if text != "8.现身体状况，是否存在发热体温、寒战、咳嗽、胸闷以及呼吸困难等症状? (Do you have any symptoms such as fever, chills, cough, chest tightness and dyspnea?)（必填）":
        return False

    text = driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[9]/div[1]').get_attribute('textContent')
    print(text)
    if text != "9.同住家属（人员）是否有上述与疫情相关的情况？(Did your family members(s) living together have any situation mentioned above ?)（必填）":
        return False

    text = driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[10]/div[1]').get_attribute('textContent')
    print(text)
    if text != "10.当前疫苗接种情况? (Vaccination status?)（必填）":
        return False

    text = driver.find_element(By.XPATH, '//*[@id="question-form"]/ul/li[11]/div[1]').get_attribute('textContent')
    print(text)
    if text != "11.本人或家庭成员(包括其他亲密接触人员)是否有近10日入境或未来7天内拟入境的情况? (Have you or your family members(including other close contact persons) entered China over the past 10 days or plan to enter China in 7 days?)（必填）":
        return False

    print("表单验证通过")
    return True
