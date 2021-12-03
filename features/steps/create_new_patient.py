import time
from behave import *
from selenium import webdriver


@given('patient management system homepage is displayed')
def step_impl(context):
    context.driver = webdriver.Chrome("resources/chromedriver.exe")
    context.driver.get("http://localhost:3000/")
    context.driver.maximize_window()


@when('the user enters their firstname')
def enter_firstname(context):
    firstname = "john"
    firstname_element = context.driver.find_element_by_css_selector('[data-test-id="first-name"]')
    firstname_element.send_keys(firstname)


@when('enter their middle name')
def enter_middle_name(context):
    middle_name = "henderson"
    middle_name_element = context.driver.find_element_by_css_selector('[data-test-id="middle-name"]')
    middle_name_element.send_keys(middle_name)


@when('enter their lastname')
def enter_lastname(context):
    lastname = "doe"
    lastname_element = context.driver.find_element_by_css_selector('[data-test-id="last-name"]')
    lastname_element.send_keys(lastname)


@when('enter phone number')
def enter_phone_number(context):
    phone_element = context.driver.find_element_by_css_selector('[data-test-id="phone-number"]')
    phone_element.send_keys("0245876382")


@when('enter valid date of birth')
def enter_dob(context):
    dob = context.driver.find_element_by_css_selector('[data-test-id="dob"]')
    dob.send_keys("10/02/1991")


@when('enter address')
def enter_user_address(context):
    address = context.driver.find_element_by_css_selector('[data-test-id="address"]')
    address.send_keys("egya amponsah avenue")
    time.sleep(2)


@when('click on add new user button')
def click_add_new_user_button(context):
    context.driver.find_element_by_css_selector('[data-test-id="submit-btn"]').click()
    time.sleep(1)


@then('the user should be added to the system')
def user_added_to_system(context):
    user_added = context.driver.find_element_by_css_selector('[data-test-id="user-info"]').is_displayed()
    assert user_added is True


@then('close browser')
def close_browser(context):
    context.driver.close()

