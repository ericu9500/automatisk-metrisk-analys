from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urlparse, parse_qs
import os
import time

# Create a folder if it doesn't exist
folder_name = "hypotactic_htmls_greek"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Create a Chrome Options object
chrome_options = Options()
chrome_options.add_argument("--headless")

# Initialize the Chrome driver with headless option
print("Initializing headless Chrome driver...")
try:
    driver = webdriver.Chrome(options=chrome_options)
except Exception as e:
    print(f"Error initializing Chrome driver: {e}")

work_urls = [
    'https://hypotactic.com/latin/index.html?Use_Id=persians',
    'https://hypotactic.com/latin/index.html?Use_Id=prometheus',
    'https://hypotactic.com/latin/index.html?Use_Id=seven',
    'https://hypotactic.com/latin/index.html?Use_Id=apollonius1',
    'https://hypotactic.com/latin/index.html?Use_Id=apollonius2',
    'https://hypotactic.com/latin/index.html?Use_Id=apollonius3',
    'https://hypotactic.com/latin/index.html?Use_Id=apollonius4',
    'https://hypotactic.com/latin/index.html?Use_Id=aratus',
    'https://hypotactic.com/latin/index.html?Use_Id=bion',
    'https://hypotactic.com/latin/index.html?Use_Id=callimachusHymns',
    'https://hypotactic.com/latin/index.html?Use_Id=callimachusEp',
    'https://hypotactic.com/latin/index.html?Use_Id=cleanthes',
    'https://hypotactic.com/latin/index.html?Use_Id=colluthus',
    'https://hypotactic.com/latin/index.html?Use_Id=theogony',
    'https://hypotactic.com/latin/index.html?Use_Id=worksanddays',
    'https://hypotactic.com/latin/index.html?Use_Id=scutum',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad1',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad2',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad3',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad4',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad5',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad6',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad7',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad8',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad9',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad10',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad11',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad12',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad13',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad14',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad15',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad16',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad17',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad18',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad19',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad20',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad21',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad22',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad23',
    'https://hypotactic.com/latin/index.html?Use_Id=iliad24',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey1',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey2',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey3',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey4',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey5',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey6',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey7',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey8',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey9',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey10',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey11',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey12',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey13',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey14',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey15',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey16',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey17',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey18',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey19',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey20',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey21',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey22',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey23',
    'https://hypotactic.com/latin/index.html?Use_Id=odyssey24',
    'https://hypotactic.com/latin/index.html?Use_Id=HHDemeter',
    'https://hypotactic.com/latin/index.html?Use_Id=HHAphrodite',
    'https://hypotactic.com/latin/index.html?Use_Id=HHApollo',
    'https://hypotactic.com/latin/index.html?Use_Id=HHermes',
    'https://hypotactic.com/latin/index.html?Use_Id=HHymns',
    'https://hypotactic.com/latin/index.html?Use_Id=lycophron',
    'https://hypotactic.com/latin/index.html?Use_Id=moschus',
    'https://hypotactic.com/latin/index.html?Use_Id=nicander',
    'https://hypotactic.com/latin/index.html?Use_Id=opcyn',
    'https://hypotactic.com/latin/index.html?Use_Id=ophal',
    'https://hypotactic.com/latin/index.html?Use_Id=olympians',
    'https://hypotactic.com/latin/index.html?Use_Id=pythians',
    'https://hypotactic.com/latin/index.html?Use_Id=nemeans',
    'https://hypotactic.com/latin/index.html?Use_Id=isthmians',
    'https://hypotactic.com/latin/index.html?Use_Id=semonides',
    'https://hypotactic.com/latin/index.html?Use_Id=solon',
    'https://hypotactic.com/latin/index.html?Use_Id=theoc1',
    'https://hypotactic.com/latin/index.html?Use_Id=theoc2',
    'https://hypotactic.com/latin/index.html?Use_Id=theoc3',
    'https://hypotactic.com/latin/index.html?Use_Id=theoc4',
    'https://hypotactic.com/latin/index.html?Use_Id=theognis',
    'https://hypotactic.com/latin/index.html?Use_Id=tryph',
    'https://hypotactic.com/latin/index.html?Use_Id=tyrtaeus',
    'https://hypotactic.com/latin/index.html?Use_Id=batmumach'
]

for i, url in enumerate(work_urls):
    print(f"Processing URL {i + 1} out of {len(work_urls)}: {url}")
    
    # Parse the URL to get the Use_Id value
    parsed_url = urlparse(url)
    use_id = parse_qs(parsed_url.query).get('Use_Id', ['unknown'])[0]
    
    # Go to the URL
    driver.get(url)

    # Wait for JavaScript to load the dynamic content
    print("  Waiting for dynamic content to load...")
    time.sleep(5)  # waiting for 5 seconds

    # Fetch the dynamic content populated by JavaScript
    try:
        print("  Fetching dynamic content...")
        latin_div_content = driver.find_element(By.ID, "latindiv").get_attribute("outerHTML")
    except NoSuchElementException:
        print("  Element not found. Skipping...")
        continue
    except Exception as e:
        print(f"  Unexpected error: {e}")
        continue

    # Save it to a file in the specified folder
    filename = os.path.join(folder_name, f'{use_id}.html')
    print(f"  Saving content to {filename}...")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(latin_div_content)

# Close the browser
print("Closing the browser...")
driver.quit()

print("Done.")
