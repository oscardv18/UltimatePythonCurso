from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://github.com")
link = browser.find_element(by=By.LINK_TEXT, value="Sign in")
link.click()

user_input = browser.find_element(by=By.ID, value="login_field")
pass_input = browser.find_element(by=By.ID, value="password")

user_input.send_keys(os.environ.get("gh_user"))
pass_input.send_keys(os.environ.get("gh_pass"))

pass_input.send_keys(Keys.ENTER)
profile = browser.find_element(
    by=By.CLASS_NAME, value="css-truncate.css-truncate-target.ml-1"
)

label = profile.get_attribute("innerHTML")
assert "oscardv18" in label

browser.quit()
