import allure
from selenium import webdriver


class Test001:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("第二步")
    def abc(self):
        print("1111")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("第一步")
    def test_01(self):
        self.abc()
        allure.attach(self.driver.get_screenshot_as_png(), "截图图", allure.attachment_type.PNG)
        print("\n test_001")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_02(self):
        print("\n test_002")
        assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_03(self):
        print("\n test_003")

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_04(self):
        print("\n test_004")
