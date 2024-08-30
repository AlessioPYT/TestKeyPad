from pages import Page
import logging
from XPATH import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='test_log.log')


class KeyPadOperation(Page):
    
    def enter_in_options(self):
        logging.info("Start entering in options KeyPadComdi")
        self.find_element_by_id(Devices).click()
        self.find_element_by_id(KeyPasCombi).click()
        self.find_element_by_id(Options_KeyPadCombi).click()
        logging.info("Enterted in options KeyPadComdi")

    def change_code(self, code1: str, code2: str):
        logging.info("Start changing code")
        self.find_element_by_id(code).click()
        a = self.find_element_by_id("code1")
        b = self.find_element_by_id("code2")
        Page.send_keys(a, code1)
        Page.send_keys(b, code2)
        self.find_element_by_id(done).click()
        self.find_element_by_id(code).click()
        logging.info("Finished changing code")


    def back_save(self):
        self.find_element_by_id(back).click()
        logging.info("was click on back button")

    def change_name(self, name: str):
        logging.info("Start change name")
        a = self.find_element_by_id(name)
        Page.send_keys(a, name)
        self.back_save()
        self.find_element_by_id(Options_KeyPadCombi).click()
        logging.info("Finished changing name")

    def change_sound_allarm(self):
        self.find_element_by_id(sound_allarm).click()

    def change_parametr_keypad(self):
        logging.info("Start changing param keypad")
        self.find_element_by_id(param_keypad).click()
        self.find_element_by_id(only_keypad).click()
        logging.info("Finished changing param keypad")

    def button_func(self):
        logging.info("Start button func")
        self.find_element_by_id(button_func).click()
        self.find_element_by_id(off).click()
        logging.info("Finished button func")

    def alarm_volume(self):
        logging.info("Start alarm volume")
        self.find_element_by_id(volume_alarm).click()
        self.find_element_by_id(basso).click()
        logging.info("Finished alarm volume")

    def duration_alarm(self):
        logging.info("Start duration alarm")
        self.find_element_by_id(duration_alarm).click()
        self.find_element_by_id("3s").click()
        logging.info("Finished duration alarm")



