from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

#NOTE: AI was used to generate this code, specifically deepseek. 

def scrape_course_links():
    base_url = "https://studiegids.uva.nl/xmlpages/page/2024-2025-en/search-course"
    course_links = []

    # Set up headless Chrome browser
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    wait = WebDriverWait(driver, 10)
    driver.get(base_url)

    cur_page = 0
    max_pages = 200

    while cur_page<max_pages:
        time.sleep(2)  # wait for JS content to load

        # Get the page source again and re-fetch elements
        wait.until(EC.presence_of_element_located((By.ID, "search-results")))

        # Get course links freshly on each iteration
        course_elements = driver.find_elements(By.CSS_SELECTOR, "div#search-results a[href*='/search-course/course/']")
        for i in range(len(course_elements)):
            try:
                # Refresh the element to avoid stale reference
                element = driver.find_elements(By.CSS_SELECTOR, "div#search-results a[href*='/search-course/course/']")[i]
                link = element.get_attribute("href")
                if link and link not in course_links:
                    course_links.append(link)
            except Exception as e:
                print(f"Skipping element due to error: {e}")
                continue

        # Try clicking "next"
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'next')]")))
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            time.sleep(1)
            next_button.click()
            
            # Wait for page to change (wait for current button to become stale)
            WebDriverWait(driver, 10).until(
                EC.staleness_of(next_button)
            )
            
            # Wait for new results
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search-results"))
            )
            time.sleep(1)  # Additional buffer
            
            cur_page += 1
        except:
            print("No more pages found. Exiting loop.")
            break

    driver.quit()
    return course_links


# Run the scraper and save the links
if __name__ == "__main__":
    links = scrape_course_links()
    print(f"Found {len(links)} courses.")
    
    output_file = "uva_course_links.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for link in links:
            if re.search(r"studiegids\.uva\.nl/xmlpages/page/2024-2025-en/search-course/course/\d{6}", link):
                f.write(link + "\n")

