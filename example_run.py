from wifi_scanner import WiFiScanner
from stepper_control import move_to_position


def scan(x, y, current_angle):
    wifi_scanner = WiFiScanner()
    text_file_name = axis_to_name(current_angle, y)
    # usage: pass in interface and name of text file to be saved
    wifi_interface = "wlan1"
    wifi_scanner.run(wifi_interface, text_file_name)


def axis_to_name(x, y):
    # record current axis degrees for filename to be saved
    file_name = ("x:"+ str(x)+ ",y:" + str(y))
    return file_name


def scan_test():
    current_angle = 0
    x = 10
    y = 90
    while current_angle < 180:
        # move the dish over and then scan
        print("Current X angle : " + str(current_angle))
        current_angle += 10
        y = -y
        scan(x, y, current_angle)
        move_to_position("x", x)
        scan(x, y, current_angle)
        move_to_position("y", y)

scan_test()





