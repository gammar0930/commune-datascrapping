import commune as c
import json
from selenium import webdriver
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


class BountyScraper(c.Module):
    def __init__(self, protocol_url):
        self.protocol_url = protocol_url
        self.set_config(kwargs=locals())

    def scrape_bounties(self):
        driver = webdriver.Chrome()
        driver.get(self.protocol_url)

        # Add logic to find and extract bounty data from the website
        # You may need to inspect the HTML structure of the website and adjust the XPath accordingly
        # Example:
        bounty_rows = driver.find_elements_by_xpath(
            "//tr[contains(@class, 'bounty-row')]"
        )

        bounty_data = []
        for bounty_row in bounty_rows:
            # Extract relevant information for each bounty
            bounty_info = {
                "name": bounty_row.find_element_by_xpath(".//td[1]").text,
                "reward": float(bounty_row.find_element_by_xpath(".//td[2]").text),
                "description": bounty_row.find_element_by_xpath(".//td[3]").text,
                # Add more fields as needed
            }
            bounty_data.append(bounty_info)

        driver.quit()
        return bounty_data

    def save_to_json(self, data, filename):
        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent=2)
        c.print(f"Data saved to {filename}")

    def call(self, output_json="bounties.json"):
        c.print(f"Scraping bounties from {self.protocol_url}")
        bounty_data = self.scrape_bounties()
        self.save_to_json(bounty_data, output_json)
        return bounty_data


# Example usage
protocol_url = "https://example-protocol.com/bounties"
bounty_scraper = BountyScraper(protocol_url)
bounty_data = bounty_scraper.call()

# Now you can use the bounty_data for further processing or display in Streamlit
