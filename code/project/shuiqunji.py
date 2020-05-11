import time


def keyboard_input(string):
    from pynput.keyboard import Controller
    keyboard = Controller()
    keyboard.type(string)
    return True


def mouse_click():
    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.press(Button.left)
    # time.sleep(0.01)
    mouse.release(Button.left)
    # return None


def run(string):

    if keyboard_input(string) is True:

        mouse_click()


try:
    f = open("test.txt", mode='r')
except Exception:
    f = open('test.txt', mode='w')
else:
    content_list = f.readlines()
    # content_list = ''.join(content_list)
    time.sleep(5)
    for i in content_list:
        # time.sleep(0.1)

        run(i.strip('\n'))
finally:
    f.close()
