from selenium import webdriver
from webdrivermanager import *

class Browser(object):
    driver = None
    element_wait_timeout = None

    def open_browser(self, browser, url, headless = False):
        options = Options()
        options.headless = headless
        options.add_argument('--no-sandbox')

        if browser.lower() == "firefox":
            self.driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().download_and_install()[1])
        elif browser.lower() == "chrome":
            if platform.system() == "Windows":
                os.system("taskkill /IM \"chromedriver.exe\" /F")
            self.driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().download_and_install()[1])
        
        self.driver.maximize_window()
        self.driver.get(url)
        return self

    def find_element(self, by=By.ID, value=None, timeout=None):
        if timeout is None:
            timeout = self.element_wait_timeout

        return WebDriverWait(self._driver, timeout, POLL_FREQUENCY).until(EC.visibility_of_element_located((by, value)))

    def execute_script(self, script, *args):
        result = self._driver.execute_script(script, *args)
        return result

    def wait_for_element_invisible(self, by=By.ID, value=None, timeout=None):
        self.is_element_invisible(by, value, timeout)

    def wait_for_element_visible(self, by=By.ID, value=None, timeout=None):
        self.is_element_visible(by, value, timeout)

    def wait_for_element_clickable(self, by=By.ID, value=None, timeout=None):
        self.is_element_clickable(by, value, timeout)

    def is_element_visible(self, by=By.ID, value=None, timeout=None):
        if timeout is None:
            timeout = self._driverSetting.element_wait_timeout
        result = None
        result = WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located((by, value)))
        return result is not None

    def is_element_invisible(self, by=By.ID, value=None, timeout=None):
        if timeout is None:
            timeout = self._driverSetting.element_wait_timeout
        result = None
        result = WebDriverWait(self._driver, timeout, POLL_FREQUENCY).until(EC.invisibility_of_element_located((by, value)))
        return result is True

    def is_element_clickable(self, by=By.ID, value=None, timeout=None):
        if timeout is None:
            timeout = self._driverSetting.element_wait_timeout
        result = None
        result = WebDriverWait(self._driver, timeout, POLL_FREQUENCY).until(EC.element_to_be_clickable((by, value)))
        return result is not None
    
    def close(self):
        self._driver.close()
        if self.window_handles:
            self.switch_to_main_window()

    def refresh(self):
        self._driver.refresh()

    def quit(self):
        self._driver.quit()

    def switch_to_alert(self):
        self._print_action("Switch to alert")
        return self._driver.switch_to.alert

    def switch_to_main_window(self):
        self.switch_to_window(0)

    def switch_to_window(self, index=0):
        self._driver.switch_to.window(self.window_handles[index])
        self.switch_to_default_content()

    def switch_to_default_content(self):
        self._driver.switch_to.default_content()

    def switch_to_frame(self, frame_id):
        self._driver.switch_to.frame(frame_id)