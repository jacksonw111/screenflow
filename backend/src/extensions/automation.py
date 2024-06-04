from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Automation:
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.set_capability("browserVersion", "100.0")
        options.set_capability(
            "selenoid:options", {"enableVNC": True, "enableVideo": False}
        )
        self._driver = webdriver.Remote(
            command_executor="http://4.236.205.249:4444/wd/hub",
            options=options,
        )
        self.driver = WebDriverWait(driver=self._driver, timeout=8)
        self.action = ActionChains(self.driver)

    def visible(self, by: By, element: str) -> WebElement:
        return self.driver.until(EC.visibility_of_element_located((by, element)))

    def located(self, by: By, element: str) -> WebElement:
        return self.driver.until(EC.presence_of_element_located(by, element))

    def clickable(self, by: By, element: str) -> WebElement:
        return self.driver.until(EC.element_to_be_clickable(self.visible(by, element)))

    def click(self, by: By, element: str):
        self.clickable(by, element).click()

    def click_at(self, by: By, element: str):
        self.located(by, element).click()

    def move_to_click(self, by: By, element: str):
        self.action.move_to_element(self.located(by, element)).click()

    def input(self, by: By, element: str, value: str):
        self.located(by, element).send_keys(value)

    def execute_js(self, by: By, element: str, value: str):
        self._driver.execute_script(value, element)
