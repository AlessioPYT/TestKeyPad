from KeyPadCombiPage import KeyPadOperation
import pytest


drive = KeyPadOperation()

def test_enterIN():
    drive.enter_in_options()
    element = drive.find_element_by_id("some")
    assert element.is_displayed(), "Страница не была загружена корректно"



def test_changepassw(code1: str, code2: str):
    drive.change_code(code1, code2)
    a = drive.find_element_by_id("code1")
    b = drive.find_element_by_id("code2")
    assert a == code1 and b == code2

def test_change_name(name):
    drive.change_name(name)
    a = drive.find_element_by_id("name")
    assert a == name

def test_changeoptions():
    drive.change_parametr_keypad()
    drive.button_func()
    drive.alarm_volume()
    drive.duration_alarm()



if __name__ == "__main__":
    pytest.main()