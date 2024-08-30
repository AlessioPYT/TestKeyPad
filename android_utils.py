import subprocess
from appium.options.android import UiAutomator2Options


adb_output = subprocess.getoutput('adb devices')
if not adb_output or len(adb_output.splitlines()) == 1:
    raise EnvironmentError('No Android device found')
else:
    udid = adb_output.splitlines()[1].split()[0]


def get_driver_options() -> UiAutomator2Options:
    options = UiAutomator2Options()
    options.no_reset = True
    options.udid = udid
    options.clear_device_logs_on_start = True
    options.auto_grant_permissions = True
    options.disable_window_animation = True
    return options


def reset_app(package) -> None:
    subprocess.run(
        ['adb', '-s', udid, 'shell', 'pm', 'clear', package],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

# def setup_logger():
#     logger = logging.getLogger('app_logger')
#     logger.setLevel(logging.DEBUG)

#     # Создаем консольный обработчик и устанавливаем уровень логирования
#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(logging.DEBUG)

#     # Создаем файловый обработчик и устанавливаем уровень логирования
#     file_handler = logging.FileHandler('logs/app.log', mode="w") # 
#     file_handler.setLevel(logging.DEBUG)

#     # Создаем форматеры
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     console_handler.setFormatter(formatter)
#     file_handler.setFormatter(formatter)

#     # Добавляем обработчики к логгеру
#     logger.addHandler(console_handler)
#     logger.addHandler(file_handler)

#     return logger