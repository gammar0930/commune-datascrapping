import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
import json


# enable the headless mode
def scrape_youtube_data(url):
    options = Options()
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    driver.get(url)

    # enable the headless mode
    options = Options()
    # options.add_argument('--headless=new')

    # initialize a web driver instance to control a Chrome window
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    # the URL of the target page
    url = "https://www.youtube.com/watch?v=kuDuJWvho7Q"
    # visit the target page in the controlled browser
    driver.get(url)

    try:
        # wait up to 15 seconds for the consent dialog to show up
        consent_overlay = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "dialog"))
        )

        # select the consent option buttons
        consent_buttons = consent_overlay.find_elements(
            By.CSS_SELECTOR, ".eom-buttons button.yt-spec-button-shape-next"
        )
        if len(consent_buttons) > 1:
            # retrieve and click the 'Accept all' button
            accept_all_button = consent_buttons[1]
            accept_all_button.click()
    except TimeoutException:
        print("Cookie modal missing")

    # wait for YouTube to load the page data
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.ytd-watch-metadata"))
    )

    # initialize the dictionary that will contain
    # the data scraped from the YouTube page
    video = {}

    # scraping logic
    title = driver.find_element(By.CSS_SELECTOR, "h1.ytd-watch-metadata").text

    # dictionary where to store the channel info
    channel = {}

    # scrape the channel info attributes
    channel_element = driver.find_element(By.ID, "owner")

    channel_url = channel_element.find_element(
        By.CSS_SELECTOR, "a.yt-simple-endpoint"
    ).get_attribute("href")
    channel_name = channel_element.find_element(By.ID, "channel-name").text
    channel_image = channel_element.find_element(By.ID, "img").get_attribute("src")
    channel_subs = channel_element.find_element(By.ID, "owner-sub-count").text.replace(
        " subscribers", ""
    )

    channel["url"] = channel_url
    channel["name"] = channel_name
    channel["image"] = channel_image
    channel["subs"] = channel_subs

    # click the description section to expand it
    driver.find_element(By.ID, "description-inline-expander").click()

    info_container_elements = driver.find_elements(
        By.CSS_SELECTOR, "#info-container span"
    )
    views = info_container_elements[0].text.replace(" views", "")
    publication_date = info_container_elements[2].text

    description = driver.find_element(
        By.CSS_SELECTOR, "#description-inline-expander .ytd-text-inline-expander span"
    ).text

    likes = driver.find_element(By.ID, "segmented-like-button").text

    video["url"] = url
    video["title"] = title
    video["channel"] = channel
    video["views"] = views
    video["publication_date"] = publication_date
    video["description"] = description
    video["likes"] = likes

    # close the browser and free up the resources
    driver.quit()

    return video


def on_submit():
    url = url_entry.get()
    video_data = scrape_youtube_data(url)
    with open("video.json", "w") as file:
        json.dump(video_data, file, indent=4)


# Create the GUI
root = tk.Tk()
root.title("YouTube Scraper App")

url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()
