import pytest
from appium_driver import Appium
from driver import Driver
from android_utils import get_driver_options, reset_app


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption('--login', action='store_true', default=False, help='Reset app and login before tests session')


def login() -> None:
    reset_app(Driver.app_package)
    Driver.launch_app()
    Driver.grant_application_permissions()



@pytest.fixture(scope='session', autouse=True)
def appium_service():
    Appium.start()
    yield
    Appium.stop()


@pytest.fixture(scope='session', autouse=True)
def driver(appium_service, request: pytest.FixtureRequest):
    Driver.start(get_driver_options())
    Driver.terminate_app()
    Driver.launch_app()
    yield
    Driver.finish()
