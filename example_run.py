
from wifi_scanner import WiFiScanner
from stepper_control import move_to_position


def scan(x, y):
    wifi_scanner = WiFiScanner()
    text_file_name = axis_to_name(x, y)
    # usage: pass in interface and name of text file to be saved
    wifi_interface = "wlp2s0"
    wifi_scanner.run(wifi_interface, text_file_name)


def axis_to_name(x, y):
    # record current axis degrees for filename to be saved
    file_name = f"x:{x},y:{y}"
    return file_name


def scan_test():
    current_angle = 0
    x = 10
    y = 90
    while True:
        # move the dish over and then scan
        print("Current angle: " + str(current_angle))
        if current_angle >= abs(180):
            x = -x
            current_angle = 0
        current_angle += 10
        y = -y
        scan(x, y)
        move_to_position("x", x)
        scan(x, y)
        move_to_position("y", y)
