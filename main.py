from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Set up Chrome options
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

# Initialize Chrome service
cService = Service('C:/Users/wangj/chromedriver-win64/chromedriver.exe')

# Initialize WebDriver
driver = webdriver.Chrome(service=cService, options=options)
driver.get('https://github.com/cvrve/New-Grad-2025?tab=readme-ov-file')
print("load complete")
# # Get all game buttons with data-key='content_detail_button'
groceries_links = driver.find_elements(By.XPATH, "//a[contains(@href, 'redirect.cvrve.me')]")
if groceries_links:
    # Access the first link (or iterate through all)
    for link in groceries_links:
        try:
            link_url = link.get_attribute("href")
            driver.execute_script(f"window.open('{link_url}', '_blank');")

            # Wait for the new tab to load
            time.sleep(3)

            # Switch to the new tab (the last tab in the window handles list)
            driver.switch_to.window(driver.window_handles[-1])

            # Perform actions on the new tab (e.g., interacting with elements, scraping data)
            print(f"Now in the new tab: {driver.current_url}")
            
            # After performing actions on the new tab, switch back to the original tab
            driver.switch_to.window(driver.window_handles[0])
            print(f"Switched back to the original tab: {driver.current_url}")

            # Optional: Wait before continuing to the next link
            time.sleep(3)
        except Exception as e:
            print(f"Error in main workflow: {e}")
        finally:
        # Close the browser
            continue
        
    # # Wait for dynamic content to load (adjust the selector as needed)
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "css-r77ujg"))  # Wait for a specific element that confirms page load
    # )

    # # Optionally, you can also wait for other elements you want to interact with here.
    # # Retrieve the specific component (adjust selector as needed)
    # component = driver.find_element(By.XPATH, "(//*[starts-with(@class, 'game-detail game-detail--type-summary')])[1]")

    # # Example: Print the text of the component (you can customize this part)
    # print(component.text)

# Close the driver
driver.quit()
