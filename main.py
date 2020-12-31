from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "Selenium Path"
email = "your email"
password = "your password"


driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()

def facebook_login():
    driver.get("https://www.facebook.com/")
    time.sleep(3)
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("u_0_b").click()
    time.sleep(2)


def tinder_login():
    driver.get("https://tinder.com/")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
    driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('//button[@aria-label="Log in with Facebook"]').click()
    time.sleep(6)

    try:
        driver.find_element_by_xpath('//button[@data-testid="allow"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//button[@aria-label="Not interested"]').click()
        time.sleep(2)
    except NoSuchElementException:
        print("It wasn't required to allow tracking.")



facebook_login()
tinder_login()

like_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')

for i in range(100):
    try:
        driver.find_element_by_xpath('//button[@class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(42px)--s Mih(50px)--ml Pos(r) Ov(h) C(#fff) Bg($blue-gradient) Bg($c-medium-blue):h::b Bg($c-medium-blue):f::b Bg($c-medium-blue):a::b StyledButton Fw($bold) focus-button-style Mt(24px) W(100%)"]').click()
        time.sleep(1)
    except NoSuchElementException:
        print("No super like option.")
    
    try:
        like_button.click()
        time.sleep(2)
    except NoSuchElementException:
        print(NoSuchElementException)
    
    try:
        driver.find_element_by_xpath('//path[@d="M14.926 12.56v-1.14l5.282 5.288c1.056.977 1.056 2.441 0 3.499-.813 1.057-2.438 1.057-3.413 0L11.512 15h1.138l-5.363 5.125c-.975 1.058-2.438 1.058-3.495 0-1.056-.813-1.056-2.44 0-3.417l5.201-5.288v1.14L3.873 7.27c-1.137-.976-1.137-2.44 0-3.417a1.973 1.973 0 0 1 3.251 0l5.282 5.207H11.27l5.444-5.207c.975-1.139 2.438-1.139 3.413 0 1.057.814 1.057 2.44 0 3.417l-5.2 5.288z"]').click()
    except NoSuchElementException:
        print(NoSuchElementException)

    try:
        driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()
        time.sleep(2)
    except NoSuchElementException:
        print(NoSuchElementException)