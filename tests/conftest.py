import pytest
from selenium import webdriver
import  os


@pytest.fixture(scope='class')
def init_driver(request):

    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff ']

    browser = os.environ.get('BROWSER')
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set ")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provider browser '{browser}'is not one of the supported"
                        f"Supported are: {supported_browsers}")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.firefox()

    request.cls.driver = driver
    yield
    driver.quit()

#@pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra


# def _capture_screenshot(name):
#         driver.get_screenshot_as_file(name)