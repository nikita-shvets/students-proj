from fastapi import APIRouter
from src.schema.tasks import TasksSchema
from src.api.dependencies import SessionDep
from src.api.students import get_students
import re
import telebot
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from fastapi import HTTPException
router = APIRouter()

@router.post(
    '/send_tasks',
    tags=['Варианты ОГЭ'],
    summary='создать варианты ОГЭ и отправить ученикам с помощью бота'
)
async def send_tasks(data:TasksSchema,session:SessionDep):
    token = '7752640605:AAGTXJR_V9HSq0sRahRiBsZxlW7fMCTCFUY'
    bot = telebot.TeleBot(token)
    tg_names_database = await  get_students(session)
    ids = []
    links = []
    final_list = []
    print(tg_names_database[0].tg_id)
    for el in data.tg_names:
        for elem in tg_names_database:
            if elem.tg_name == el:
                ids.append(elem.tg_id)

    for i in range(len(data.tg_names)):
        driver = webdriver.Chrome()

        driver.set_window_size(1920, 1080)
        actions = ActionChains(driver)
        if (data.subject == "М"):
            driver.get("https://math-oge.sdamgia.ru")
        elif (data.subject == "Ф"):
            driver.get("https://phys-oge.sdamgia.ru")
        else:
            raise HTTPException(status_code=404, detail="<wrong subject>")
        driver.implicitly_wait(150)
        c = driver.find_element(By.NAME, 'email')
        c.send_keys("nikita.shvets.ns@gmail.com")
        b = driver.find_element(By.NAME, 'password')
        b.send_keys("kV!by5E&(,.Mk-6")
        driver.find_element(By.CSS_SELECTOR, "button.Button.Button_view_default.ProfileAuth-Button").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[contains(text(),'Учи')]").click()
        driver.find_element(By.XPATH, "//*[contains(text(),'СОСТАВИТЬ')]").click()
        for i in range(int(len(data.tasks)/2)):
            a = driver.find_element(By.NAME, "prob" + str(data.tasks[2*i])).send_keys(data.tasks[2*i+1])
        b = driver.find_element(By.XPATH, "//*[@value='Составить домашнюю работу']")
        b.click()
        time.sleep(0.25)
        driver.find_element(By.XPATH, "//*[@value='Настроить параметры работы']").click()
        time.sleep(0.25)
        u = driver.find_element(By.XPATH, "//input[@style='width:70px']")
        u.click()
        actions.send_keys(data.time_to_do)
        actions.perform()
        datas = driver.find_elements(By.CLASS_NAME, "hasDatepicker")
        datas[0].send_keys(datetime.datetime.today().strftime('%d.%m.%Y'))
        datas[1].send_keys((datetime.datetime.today() + datetime.timedelta(days=7)).strftime('%d.%m.%Y'))
        driver.find_element(By.CLASS_NAME, "test_prop_save").click()
        d = driver.current_url
        l = re.search(r'\d+', d)

        links.append('https://math-oge.sdamgia.ru/test?id=' + l[0])
        driver.quit()
    for i in range (len(ids)):
        bot.send_message(ids[i], links[i])
        final_list.append([data.tg_names[i], links[i]])
    return final_list
