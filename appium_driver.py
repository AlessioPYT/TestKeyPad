from appium.webdriver.appium_service import AppiumService
import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='test_log.log')


class Appium:
    service = AppiumService()
    HOST = "127.0.0.1"  # '0.0.0.0'
    PORT = "4723"  #'48777'

    @classmethod
    def start(cls) -> None:
        cls.service.start(
            args=['-a', cls.HOST, '-p', cls.PORT, '--relaxed-security', '--allow-insecure', 'adb_shell']
        )
        logging.info("Appium Star!")

    @classmethod
    def stop(cls) -> None:
        cls.service.stop()
        logging.info("Appium Stoped!")
