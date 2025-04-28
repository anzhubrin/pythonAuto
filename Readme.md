### generate allure report
```
allure serve tests/allure-results
```
### headless mode
```
driver_options = webdriver.ChromeOptions()
driver_options.add_argument('--headless')
browser.config.driver_options = driver_options
```