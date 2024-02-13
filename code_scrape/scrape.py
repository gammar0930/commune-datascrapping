import os
import time
import json

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Scraping():
    def __init__(self):
        super().__init__()
        self.options = webdriver.ChromeOptions()
        self.download_path = os.path.abspath(os.path.dirname(__file__))
        prefs = {
            "download.default_directory": self.download_path,
            "download.prompt_for_download": False,  # Disable download prompt
            "safebrowsing.enabled": True,  # Enable safe browsing,
        }
        self.options.add_experimental_option("prefs", prefs)
        
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        
        url = "https://platform.stability.ai/docs/api-reference"
        self.driver.get(url)
        
        self.driver.implicitly_wait(20)
        total_data = []
        div_tags = self.driver.find_elements(By.CSS_SELECTOR, '[class="sc-iGgWBj sc-gsFSXq exaNI bOFhJE"]')
        actions = ActionChains(self.driver)
        # print(div_tags.text)
        for div_tag in div_tags:
            item_data = []
            
            parent_btn = div_tag.find_element(By.CSS_SELECTOR, '[class="sc-eZYNyq bvLXRH"]')
            api_text = ""
            try:
                type_selecter = parent_btn.find_element(By.XPATH, "./*[0]")
            except NoSuchElementException:
                pass
            else:
                type_selecter = parent_btn.find_element(By.XPATH, "./*[0]")
                api_text += type_selecter.text + "|"
            
            try:
                api_selecter = parent_btn.find_element(By.CSS_SELECTOR, '[class="sc-EgOXT cvuzFu"]')
            except NoSuchElementException:
                pass
            else:
                api_selecter = parent_btn.find_element(By.CSS_SELECTOR, '[class="sc-EgOXT cvuzFu"]')
                api_text += api_selecter.text
                
            item_api = api_text
            
            try:
                selecter_language = div_tag.find_element(By.CSS_SELECTOR, '[class="react-tabs__tab-list"]')
            except NoSuchElementException:
                pass
            else:
                try:
                    btns = selecter_language.find_elements(By.CSS_SELECTOR, '[class="react-tabs__tab"]')
                except NoSuchElementException:
                    pass
                else:
                    for btn in btns:
                        if "Python" in btn.text:
                            try:
                                actions.move_to_element(btn).click().perform()
                            except ElementClickInterceptedException:
                                pass
                            else:
                                time.sleep(0.5)

            try:
                request_sample = div_tag.find_element(By.CSS_SELECTOR, '[class="sc-iHGNWf sc-dtBdUo fFdGkU kgWAzc"]')
            except NoSuchElementException:
                pass
            else:
                request_sample = div_tag.find_element(By.CSS_SELECTOR, '[class="sc-iHGNWf sc-dtBdUo fFdGkU kgWAzc"]')
                request_sample_text = request_sample.text
                item_data.append(request_sample_text)
                request_code = request_sample_text
                
            try:
                code_div = div_tag.find_element(By.TAG_NAME, 'code')
            except NoSuchElementException:
                pass
            else:
                try:
                    button_group = div_tag.find_element(By.CSS_SELECTOR, '[class="sc-koXPp ctwdsc"]')
                except NoSuchElementException:
                    pass
                else:
                    button_group = div_tag.find_element(By.CSS_SELECTOR, '[class="sc-koXPp ctwdsc"]')
                    try:
                        btns = button_group.find_elements(By.TAG_NAME, "button")
                    except NoSuchElementException:
                        pass
                    else:
                        for btn in btns:
                            if "Expand" in btn.text:
                                try:
                                    actions.move_to_element(btn).click().perform()
                                except ElementClickInterceptedException:
                                    pass
                                else:
                                    time.sleep(0.5)
                response_text = code_div.text
            
            item_json = {
                "api": item_api,
                "request_code": request_code,
                "response_json": response_text
            }
            
            total_data.append(item_json)
        
        url_array = [
            "https://platform.stability.ai/docs/features/text-to-image#Python",
            "https://platform.stability.ai/docs/features/image-to-image#Python",
            "https://platform.stability.ai/docs/features/inpainting#Python",
            "https://platform.stability.ai/docs/features/clip-guidance",
            "https://platform.stability.ai/docs/features/animation/install",
            "https://platform.stability.ai/docs/features/animation/using",
            "https://platform.stability.ai/docs/features/image-upscaling#Python",
            "https://platform.stability.ai/docs/features/multi-prompting#Sandbox",
            "https://platform.stability.ai/docs/features/variants"
        ]
        
        pretxt_array = []
        imgsrc_array = []
        for url in url_array:
            self.driver.get(url)
            self.driver.implicitly_wait(20)
            try:
                pre_tags = self.driver.find_elements(By.TAG_NAME, 'pre')
            except NoSuchElementException:
                pass
            else:
                pre_tags = self.driver.find_elements(By.TAG_NAME, 'pre')
                
                for pre_tag in pre_tags:
                    try:
                        code_div = pre_tag.find_element(By.CLASS_NAME, 'hljs')
                    except NoSuchElementException:
                        pass
                    else:
                        code_div = pre_tag.find_element(By.CLASS_NAME, 'hljs')
                        code_txt = code_div.text
                        pretxt_array.append(code_txt)
            
            try:
                img_tags = self.driver.find_elements(By.TAG_NAME, 'img')
            except NoSuchElementException:
                pass
            else:    
                img_tags = self.driver.find_elements(By.TAG_NAME, 'img')
                    
                for img_tag in img_tags:
                    img_src = img_tag.get_attribute('src')
                    imgsrc_array.append(img_src)
                
        
        print(total_data)
        total_data.append({
            "pre_text": pretxt_array,
            "img_src": imgsrc_array
        })
        
        with open('data.json', 'w') as f:
            json.dump(total_data, f)
            
        # while(1):
        #     time.sleep(1)
            
       