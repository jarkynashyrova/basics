# Finding the Elements:
# by name,
# by id, ( fastest if the elements ID is unique)
# by class name,
# by link text, by partial link text

# by xpath ( customizable, flexible, element hierachy can be used better),
# by css selector (customizable, flexible),

# Functions from selenium
# find_element_by_id(id)

# start the browser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.common.keys import Keys

# Global
from utilities import *

driver = webdriver.Chrome()
# implicit wait is defined once when you start the browser and this will apply all find element steps
driver.implicitly_wait(5)
driver.maximize_window()

def open_website(url):
    """open the website, and click on 'No, thanks! button"""
    try:
        #url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
        driver.get(url)
        print(f"Title of the page 1:{driver.title}")

        #time.sleep(10) # one way of holding the execution and wait for somthing
        print("now clicking the 'No, thanks' button..")
        driver.find_element_by_link_text('No, thanks!').click()
    except NoSuchElementException as err:
        print(f'pop did not appear this time.\n{err}')

def back_forward():
    img1 = f'./../screenshots/{get_str_seconds()}datapage.png'
    img2 = f'./../screenshots/{get_str_seconds()}seleniumdemo.png'

    driver.back()
    time.sleep(5)
    print(f"Title of the page 2: {driver.title}")
    driver.get_screenshot_as_file(img1)

    driver.forward()
    print(f"Title of the page 3: {driver.title}")
    driver.get_screenshot_as_file(img2)
    time.sleep(5)


def get_total_input_fields():
    """
    find the "Enter a" input box
    find the "Enter b" input box
    enter the "30" text in a
    enter the "30" text in b
    """
    img1 = f'./../screenshots/{get_str_seconds()}_result.png'

    driver.find_element_by_id('sum1').send_keys("20")
    bvalue_input = driver.find_element_by_id('sum2')
    bvalue_input.send_keys("30")

    # find the "Get Total"button, then click on that button
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    sum_button = driver.find_element_by_xpath("//button[text()='Get Total']")
    #sum_button = driver.find_element_by_class_name(btn btn -defoult")
    sum_button.click()
    driver.get_screenshot_as_file(img1)


def close_browser():
    driver.close()  # close the current tab
    driver.quit()  #closes the browser


def checkbox_test():
    # todo: code here
    #find the element(using xpath) to check, and click
    check_xpath = "//input[@id='isAgeSelected']"

    print("checkbox test started....")
    checkbox = driver.find_element_by_xpath(check_xpath)
    checkbox.click()
    time.sleep(5)
    
    #verify the checkbox is checked
    print(f"Is Checkbox Selected (True/False): {checkbox.is_selected()}")

    #find the message element and get text
    msg_css_selector = "#txtage"
    msg = driver.find_element_by_css_selector(msg_css_selector)
    msg_text = msg.txt
    print(f"Final message: {msg_text}")

    assert "Success" in msg_text
