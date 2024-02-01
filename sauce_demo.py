from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def start_google_chrome_and_go_site(url):
    driver = webdriver.Chrome(service=Service(), options=webdriver.ChromeOptions())
    driver.maximize_window()
    driver.get(url)
    return driver



def test_standard_user_login_and_app_logo_verified():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    print('Google Chrome started and saucedemo site is loaded')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    print('Locator ID is found with input user-name and standard_user is input')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    print('Locator ID with password is found and secret_sauce is input')
    driver.find_element(By.ID, 'login-button').click()
    print('Locator ID with login button is found and clicked')
    assert 'Swag Labs' in driver.find_element(By.CLASS_NAME, 'app_logo').text
    print('Locator class_name is found, and app logo swag labs in verified')
    print('Standard_user successfully logged in and swag labs app logo is verified')
    driver.close()




def test_locked_out_user_test_login_and_verify_error_message():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    print('Google Chrome started and saucedemo site is loaded')
    driver.find_element(By.ID, 'user-name').send_keys('locked_out_user')
    print('Locator ID with user-name tag found text locked_out_user is input')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    print('Locator ID with password found text secret_sauce is input')
    driver.find_element(By.ID, 'login-button').click()
    print('Locator ID with login-button located and clicked, to submit the login form')
    time.sleep(2)
    print('Pause for 2 seconds')
    assert 'Epic sadface: Sorry, this user has been locked out.' in driver.find_element(By.CLASS_NAME,'error-message-container.error').text
    print('Locator class_name found and error message verified')
    print('Locked out user unable to login')
    driver.close()



def test_click_on_first_product_verify_name():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    print('Google Chrome started and saucedemo site is loaded')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    print('Locator ID with user-name found and standard_user is input')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    print('Locator ID with password is found and secret_sauce is input')
    driver.find_element(By.ID, 'login-button').click()
    print('Locator ID with password is found and secret_sauce is input, to submit login form')
    time.sleep(2)
    print('Pause for 2 seconds')
    driver.find_element(By.XPATH, "//a[@id='item_4_title_link']").click()
    print('Locator Xpath is used to locate element with tag name a with attribute id which is submitted by click')
    time.sleep(2)
    print('Pause for 2 seconds')
    driver.save_screenshot('product1.png')
    print('Screenshot is saved')
    time.sleep(2)
    print('Pause for 2 seconds')
    assert 'Sauce Labs Backpack' in driver.find_element(By.CLASS_NAME, 'inventory_details_name.large_size').text
    print('First product name is verified by class_name locator')
    print('Name of first product is correct')
    driver.close()


def test_click_on_first_product_add_to_cart_and_verify_shopping_cart():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    print('Google Chrome started and saucedemo site is loaded')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)
    print('Pause for 2 seconds')
    driver.find_element(By.XPATH, "//a[@id='item_4_title_link']").click()
    print('Locator Xpath is used to locate element with tag name a with attribute id which is submitted by click')
    time.sleep(2)
    print('Pause for 2 seconds')
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    print('Locator ID with add-to-cart-sauce-labs-backpack is clicked and product is added to cart')
    time.sleep(2)
    print('Pause for 2 seconds')
    driver.find_element(By.ID, 'shopping_cart_container').click()
    print('Locator ID with shopping_cart_container is clicked and cart is loaded')
    time.sleep(2)
    print('Pause for 2 seconds')
    assert 'Your Cart' in driver.find_element(By.CLASS_NAME, 'title').text
    print('Shopping cart title verification with class_name locator and title text found ')
    print('Product added to cart and cart title is correct')
    driver.close()


def test_remove_first_product_from_cart_and_verify_the_cart_is_empty():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@id='item_4_title_link']").click()
    print('Locator Xpath is used to locate element with tag name a with attribute id which is submitted by click')
    time.sleep(2)
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    print('Locator ID with add-to-cart-sauce-labs-backpack is clicked and product is added to cart')
    time.sleep(2)
    driver.save_screenshot('add to cart.png')
    time.sleep(2)
    driver.find_element(By.ID, 'shopping_cart_container').click()
    print('Locator ID with shopping_cart_container is clicked and cart is loaded')
    time.sleep(2)
    driver.find_element(By.NAME, 'remove-sauce-labs-backpack').click()
    print('Locator name with remove-sauce-labs-backpack is clicked')
    time.sleep(2)
    cart_items = driver.find_elements(By.CLASS_NAME, 'cart items')
    print('Value of cart_items represented by class_name of the element')
    assert (len(cart_items), 0, "Cart is not empty after removing the product")
    print('It verifies whether the length (number of elements) in the cart_items list is equal to zero. If there are no elements in the list, it means the cart is empty.')
    driver.close()


def test_verify_checkout_step_one():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@id='item_4_title_link']").click()
    print('Locator Xpath is used to locate element with tag name a with attribute id which is submitted by click ')
    time.sleep(2)
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    print('Locator ID with add-to-cart-sauce-labs-backpack is clicked and product is added to cart')
    time.sleep(2)
    driver.find_element(By.ID, 'shopping_cart_container').click()
    print('Locator ID with shopping_cart_container is clicked and cart is loaded')
    time.sleep(2)
    driver.find_element(By.ID, 'checkout').click()
    print('Locator ID with checkout is clicked')
    time.sleep(2)
    assert ("checkout-step-one" in driver.current_url, "Checkout process failed")
    print('Condition that "checkout-step-one" is present in the current URL of the WebDriver instance (driver). If the substring is present, the condition is true.')
    driver.close()


def test_about_page():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    print('Locator ID with react-burger-menu-btn is found and the menu option is clicked')
    time.sleep(2)
    print(driver.find_element(By.ID, 'about_sidebar_link').get_attribute("href"))
    print('Locator ID with about_sidebar_link is found and url is printed')
    time.sleep(2)
    assert 'https://saucelabs.com/' == driver.find_element(By.ID, 'about_sidebar_link').get_attribute("href"), 'Wrong URL'
    print('Verification of previous URL in locator ID found about_sidebar_link')
    driver.close()

def test_verify_x_link():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    print(driver.find_element(By.CSS_SELECTOR,"a[href='https://twitter.com/saucelabs']").get_attribute("href"))
    time.sleep(2)
    assert driver.find_element(By.CSS_SELECTOR,"a[href='https://twitter.com/saucelabs']").get_attribute("href") == "https://twitter.com/saucelabs", 'Wrong URL for X'
    print('Verification of previous URL in locator css selector with tag name a and attribute href ')
    driver.close()

def test_verify_facebook_link():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    print(driver.find_element(By.CSS_SELECTOR,"a[href='https://www.facebook.com/saucelabs']").get_attribute("href"))
    print('Locator css selector is used to locate element with tag name a with attribute href which prints the URL')
    time.sleep(2)
    assert 'https://www.facebook.com/saucelabs' in driver.find_element(By.CSS_SELECTOR, "a[href='https://www.facebook.com/saucelabs']").get_attribute("href"), 'Wrong URL for FB'
    print('Verification of previous URL in locator css selector with tag name a and attribute href ')
    driver.close()


def test_verify_linkedin_page():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    print(driver.find_element(By.CSS_SELECTOR,"a[href='https://www.linkedin.com/company/sauce-labs/']").get_attribute("href"))
    print('Locator css selector is used to locate element with tag name a with attribute href which prints the URL')
    assert 'https://www.linkedin.com/company/sauce-labs/' in driver.find_element(By.CSS_SELECTOR,"a[href='https://www.linkedin.com/company/sauce-labs/']").get_attribute("href"), 'Wrong URL for linkedin'
    print('Verification of previous URL in locator css selector with tag name a and attribute href ')
    driver.close()

def test_logout_side_bar():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    print('Locator ID with react-burger-menu-btn is found and clicked')
    time.sleep(2)
    driver.find_element(By.ID, 'logout_sidebar_link').click()
    print('Locator ID with logout_sidebar_link is found and clicked')
    time.sleep(2)
    assert "https://www.saucedemo.com/" in driver.current_url, "Logout failed"
    print('Condition that current URL contains the expected URL https://www.saucedemo.com/')
    driver.close()

def test_successful_order():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.XPATH, "//a[@id='item_4_title_link']").click()
    print('Locator xpath is used to find tag a with ID attribute and is clicked')
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    print('Locator ID is found with add-to-cart-sauce-labs-backpack, and product is clicked')
    driver.save_screenshot('add to cart.png')
    print('SS is saved')
    driver.find_element(By.ID, 'shopping_cart_container').click()
    print(' Locator ID with shopping_cart_container is found and product is added to the cart by click')
    driver.find_element(By.ID, 'checkout').click()
    print('Locator id with checkout is found and checkout is clicked')
    driver.find_element(By.ID, 'first-name').send_keys("Test")
    print('Locator ID with first-name is found and Test is input')
    driver.find_element(By.ID, 'last-name').send_keys('Test')
    print('Locator ID with last-name is found and Test is input')
    driver.find_element(By.ID, 'postal-code').send_keys('11080')
    print('Locator ID with postal-code is found and 11080 is input')
    driver.find_element(By.NAME, 'continue').click()
    print('Locator with Name continue is found and continue button is clicked')
    driver.find_element(By.ID, 'finish').click()
    print(' Locator ID finish is found and button is clicked')
    time.sleep(2)
    print(driver.find_element(By.CSS_SELECTOR, "h2[class='complete-header']").text)
    print(' Locator css selector is used to find h2 tag with attribute class and text is printed')
    time.sleep(2)
    assert 'Thank you for your order!' == driver.find_element(By.CSS_SELECTOR, "h2[class='complete-header']").text
    print('Confirmation that text Thank you for your order! is in previously found locator css selector')
    driver.close()

def test_number_of_products_in_home_page():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)
    products = driver.find_elements(By.CLASS_NAME,'inventory_item')
    print('Result of products located by class name that contains inventory item value')
    number_of_products = len(products)
    print('Calculating the number of elements in the products list, which was previously populated with web elements find_elements')
    assert ("f'Number of products on home page':{number_of_products}"), 'Products are not shown'
    print('Checking if the number of products on the home page is greater than 0. If there are products (i.e., number_of_products is greater than zero), the assertion passes silently, and the program continues. ')
    driver.close()


def test_first_product_price():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.XPATH, "//a[@id='item_4_title_link']").click()
    time.sleep(2)
    price_element = driver.find_element(By.XPATH, "//div[@class='inventory_details_price']")
    print('Locator xpath is used to find tag div with attribute class which is assigned to the price of the element')
    price_text = price_element.text
    print('Price_text will be presented by price element')
    print(f"The price of the first product is: {price_text}")

    expected_price = "$29.99"
    expected_price_str = str(expected_price)
    print('Expected price is converted to string for proper comparison')

    assert price_text == expected_price_str, f"Expected price: {expected_price_str}, Actual price: {price_text}"
    print(' Confirmation if the text content of the price_element matches the expected price string (expected_price_str). If the condition is True, the script continues to execute')
    driver.save_screenshot('price_assertion.png')
    driver.close()



def test_verify_sorting():
    driver = start_google_chrome_and_go_site("https://www.saucedemo.com/")
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.CLASS_NAME, 'product_sort_container').click()
    print('Locator class name is found with product_sort_container and the button is clicked ')
    driver.find_element(By.XPATH, "//option[text()='Price (low to high)']").click()
    print(' Locator cpath is used to find tag option with attribute text and low to high is chosen and clicked')
    product_prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    print('Product prices will be presented by locator class name with inventory_item_price value')
    prices = [float(price.text.replace('$', '')) for price in product_prices]
    assert prices == sorted(prices), "Products are not sorted by price (low to high)"
    print(' he assert statement checks if the list prices is equal to its sorted version. If the prices are not sorted in ascending order, an AssertionError is raised with the specified error message: "Products are not sorted by price (low to high)".')
    driver.close()

#In summary, the code is attempting to ensure that the product prices, represented by the list prices, are sorted in ascending order (from low to high).
# The code first extracts the prices, removes the dollar sign, converts them to floats, and then checks if the resulting list is equal to its sorted version.
# If the prices are not in ascending order, the script raises an AssertionError with an error message indicating that the products are not sorted by price.
# This is a common check in web testing scenarios to ensure that displayed prices are in the expected order.



def close(driver):
    driver.minimize_window()
    driver.close()