from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from test_data.config_data import base_data
from urllib.parse import urljoin
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebPage:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebPage()
        return cls.instance

    def __init__(self):
        options = Options()
        # options.add_argument("--headless")
        if str(base_data["browser"]).lower() == "edge":
            self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        elif str(base_data["browser"]).lower() == "chrome":
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        else:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(base_data["url"])

    def go_to_page(self, page):
        self.driver.get(urljoin(base_data["url"], page.lower()))

    def verify_component_exists(self, component):
        if component in self.driver.find_element(By.CSS_SELECTOR, "html").text:
            return True
        else:
            "Component {} not found on page".format(component)
            return False

    def quit_driver(self):
        self.driver.quit()


web_page = WebPage.get_instance()
