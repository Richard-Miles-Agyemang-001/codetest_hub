# Import Selenium WebDriver modules
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

# Import Time modules
import time

# Initialize the WebDriver
driverz = webdriver.Chrome()

driverz.maximize_window()

print('--------- Web driver launched ---------')

# Navigate to the Page
driverz.get("https://hubtel.com")

time.sleep(2)

print('--------- Webpage loaded ---------')

driverz.find_element(By.LINK_TEXT, 'Grow Revenues').click()

time.sleep(2)

print('--------- Redirected to Grow revenue page ---------')

driverz.find_element(By.PARTIAL_LINK_TEXT, 'RaiseUp').click()

time.sleep(2)

print('--------- Redirected to RaiseUp page ---------')


# function to check the existence of images
def has_images(url):
    driver = webdriver.Chrome()

    try:
        driver.get(url)

        # Wait for the page to load completely
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'img')))

        # Find all img elements on the page
        images = driver.find_elements_by_tag_name('img')

        # Check if there are any images
        if images:
            print(f"The page has {len(images)} image(s).")
            for img in images:
                print("Image source:", img.get_attribute('src'))
        else:
            print("No images found on the page.")

    finally:
        driver.quit()


# Example usage
url_to_check = "https://explore.hubtel.com/schools/"
has_images(url_to_check)

time.sleep(2)

try:
    driverz.find_element(By.PARTIAL_LINK_TEXT, 'INSTALL').click()

    time.sleep(5)

    # navigate back to the first page
    driverz.back()

finally:
    # scroll down
    driverz.execute_script("window.scrollBy(0, 1600);")

    time.sleep(5)

    driverz.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div[1]/div/a").click()

    time.sleep(2)

    # close current window/tab
    driverz.close()

    driverz.quit()
