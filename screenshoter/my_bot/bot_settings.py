import telebot
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Screenshot import Screenshot_Clipping
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.ChromeOptions()
ob=Screenshot_Clipping.Screenshot()
DRIVER = '/home/mikle//projects/telegramBot/screenshoter/my_bot/chromedriver_linux64 (1)/chromedriver'
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(DRIVER, desired_capabilities = capa)

# driver = webdriver.Chrome(executable_path=DRIVER, chrome_options=options)
# /projects/telegramBot/screenshoter/my_bot


TOKEN = '1255902403:AAF1uQjkF6WeQBx60r_InVlb1znykOShp2A'

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def stend_message(message):
    bot.reply_to(message, 'hellow world')
    print(message)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

    wait = WebDriverWait(driver, 20)
    p = driver.get(message.text)
    # html_source = driver.page_source.get_attribute('body')
    heading1 = p.find_element_by_tag_name('h1')
    print(heading1)
    # for element in heading1:
    #     print(element)
        # for el in element:
        #     print(el)
    # NEED THIS
    # img_url = ob.full_Screenshot(driver, save_path=r'.', image_name="Myimage.png")
    # path = os.path.abspath("Myimage.png")
    # driver.save_screenshot("my_screenshot1cd pro    .png")
    # does not read the binary presentation of the file, so you need to open the file
    # f = open(path, "rb")
    # bot.send_document(message.chat.id, f)
    driver.quit()


bot.polling()
