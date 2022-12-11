from selenium.webdriver.common.by import By
from framework.initialize_driver_website import web_page
from selenium.common.exceptions import NoSuchElementException


class HomePage:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = HomePage()
        return cls.instance

    def __init__(self):
        self.driver = web_page.get_driver()
        self.driver.implicitly_wait(10)

    def click_icon_or_button(self, element):
        self.driver.implicitly_wait(10)
        icon_on_header = self.driver.find_element(By.XPATH, element)
        icon_on_header.click()

    def search_field(self, text):
        self.driver.implicitly_wait(10)
        search_field = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div[1]/input")
        search_field.send_keys(text)

    def if_departure_place_delete_it(self):
        departure_place_close_button = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/form/div/div[2]/div[1]/ul/li[1]/div[2]/div[1]/div/div/div/div/span/i")
        departure_place_close_button.click()

    def find_flight_departure_arrival_place(self, from_where, to_where):
        self.driver.implicitly_wait(10)
        departure_place_field = self.driver.find_element(By.XPATH,
                                                      "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]"
                                                      "/div/div/div/form/div/div[2]/div[1]/ul/li[1]/div[2]"
                                                      "/div[1]/div/div/div/div/input")
        departure_place_field.click()
        departure_place_field.send_keys(from_where)

        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[2]/div[2]/div/div[2]"
                                 "/div/div[2]/div/div/div/form/div/div[1]").click()

        self.driver.implicitly_wait(10)
        arrive_place_field = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]"
                                                                "/div/div/div/form/div/div[2]/div[1]/ul/li[1]/div[2]"
                                                                "/div[3]/div/div/div/div/input")
        arrive_place_field.click()
        arrive_place_field.send_keys(to_where)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[2]/div[2]/div/div[2]"
                                 "/div/div[2]/div/div/div/form/div/div[1]").click()

    def find_flight_departure_arrival_date(self,  flight_date, calendar_departure_xpath):
        self.driver.implicitly_wait(10)
        list_week_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        li_element_num = 0
        date_split = flight_date.split("-")
        ul_element_num = int(date_split[0])//5
        for i, day in enumerate(list_week_days):
            if day == date_split[1]:
                li_element_num = i + 1
                break

        self.driver.implicitly_wait(10)
        calendar_departure = self.driver.find_element(By.XPATH, calendar_departure_xpath)
        calendar_departure.click()

        self.driver.implicitly_wait(10)
        select_date = self.driver.find_element(By.XPATH,
                                               f"//*[@id='searchBoxCon']/div[2]/div/form/div/div[2]/div[1]/ul/li[2]"
                                               f"/div[3]/div/div[1]/div[1]/div/"
                                               f"ul[{ul_element_num}]/li[{li_element_num}]/span")

        if select_date.text != date_split[0]:
            select_date = self.driver.find_element(By.XPATH,
                                                   f"//*[@id='searchBoxCon']/div[2]/div/form/div/div[2]/div[1]/ul/li[2]"
                                                   f"/div[3]/div/div[1]/div[2]/div/"
                                                   f"ul[{ul_element_num}]/li[{li_element_num}]/span")

        self.driver.implicitly_wait(10)
        select_date.click()

    def verify_opened_successfully_and_component_present(self, component):
        self.driver.implicitly_wait(10)
        try:
            if self.driver.find_element(By.XPATH, component).is_displayed():
                print("el appears")
                return True
        except NoSuchElementException as ex:
            print("Sorry couldn't find the element")
            return False

    def verify_component_text(self, text, component):
        if self.driver.find_element(By.XPATH, component).text == text:
            return True
        else:
            return False

    @staticmethod
    def close_window():
        web_page.quit_driver()


home_page = HomePage.get_instance()

