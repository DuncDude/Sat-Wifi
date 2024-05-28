# Sat-Wifi
A repo to manipulate stepper motors on a sat dish to scan wifi and compare strength of signals


# why?
I cut my teeth on wifi hacking during the 2020 pandimc (legally), and I've always been a fan of the movie hackers, I happen to have a framed poster of it on my wall
but one of the few things that helped me get into programing was arduino and microcontrollers, so this kinda brings me back to my roots. As a novice programer as
many other things in life there was a large amount of tools required that as a child of 2 teachers I could never dream of affording, even simple things like a 
working hot glue gun. So ive tried to make this programing and the 3d printer files self suffient, so as easy to follow as possilbe and affordable, that does not 
require any special tools, or even glue. Althoug of course it can always be modified.

# to run
run exampe_run.py but change the interface to the interface you are going to use 

# Installing the driver for Kali for the reccomened wifi dongle
How to install ALFA AWUS036ACS drivers on Kali Linux 2023 (RTL8811AU - RTL8821AU)
:::::::
Commands:
sudo apt update && sudo apt upgrade
sudo reboot
mkdir -p ~/src
cd ~/src
git clone https://github.com/morrownr/8821au-20...
cd ~/src/8821au-20210708
sudo ./install-driver.sh


## Hardware and Software Requirements:

# Hardware:

    Ender 3 3D Printer:
        The Ender 3 serves as the primary platform for 3D printing the project components.

    Raspberry Pi 3+ or newer:
        The Raspberry Pi acts as the brains of the operation, facilitating the integration of software and hardware components.

    2 x 28BYJ-48 5V-DC Stepper Motors and Drivers:
        These stepper motors, along with their drivers, power the XY axis movement of the 3D printed rig.

    Jumper Wires:
        Jumper wires are essential for establishing electrical connections between components, ensuring seamless communication.

    USB Dongle (Linux Compatible, Monitor Mode):
        The ALFA AWUS036ACS WiFi dongle, known for Linux compatibility and monitor mode capabilities, is used for WiFi signal scanning.

    USB Extension Cord:
        The USB extension cord provides flexibility in positioning the WiFi dongle for optimal signal reception during scanning.

    Kali Light:
        The Kali Light distribution is employed as the operating system, providing a robust environment for ethical hacking and WiFi analysis.

# Software:

    Python:
        Python is the primary programming language used for scripting and automation in the project.

    Custom Python Library:
        A bespoke Python library is created to facilitate command-line control of the servos for precise XY axis movements. This library is utilized in the stepper_control.py program.

    Airodump-ng:
        Airodump-ng, a WiFi packet capture tool, is utilized for scanning and recording signal strengths of nearby WiFi networks. The scanning functionality is encapsulated in the wifi_scanner.py program.

    Compare.py Program:
        This custom Python program is crafted to analyze and compare the recorded signal strengths, providing the coordinates of the strongest signal for a specified WiFi BSSID.

    Kali Linux:
        The Kali Linux distribution provides a secure and powerful operating system for ethical hacking and WiFi analysis.

    wifi_scanner.py:
        The wifi_scanner.py program encapsulates the functionality for running WiFi signal scans using the ALFA AWUS036ACS WiFi dongle and airodump-ng.

    stepper_control.py:
        The stepper_control.py program is responsible for controlling the XY axis movement by interfacing with the custom Python library and the stepper motors.

    example_run.py:
        The example_run.py program acts as the orchestrator, bringing together the functionalities of WiFi scanning and XY axis control. It executes the wifi_scanner.py and stepper_control.py programs to run the entire system seamlessly.

These software components, along with the custom Python library, contribute to the automation and synchronization of the WiFi signal scanning system, making it accessible and user-friendly.