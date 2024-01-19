# Sat-Wifi
A repo to manipulate stepper motors on a sat dish to scan wifi and compare strength of signals

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

# Hardware required (recommended)

Raspberry pi 3+ or newer
2 28BYJ-48 5V-DC stepper motors and their drivers
Jumper wires
USB Dongle that is linux compatible and can go into monitor mode
USB extension cord
Tape

# Sat dish math
To design a parabolic reflector with a width of 5 inches and a height of the antenna being 3 inches, you can use the following dimensions:

    Width (D): Set the width of the parabolic reflector to 5 inches, as you specified.

    Height (h): The height of the antenna is given as 3 inches.

    Focal Length (F): Calculate the focal length using the formula F≈D216hF≈16hD2​:

    F≈5216×3F≈16×352​

    F≈2548F≈4825​

    F≈0.52F≈0.52 inches (converted to approximately 13.208 mm).

Therefore, for your specified dimensions:

    Width (D): 5 inches
    Height (h): 3 inches
    Focal Length (F): Approximately 0.52 inches (converted to approximately 13.208 mm)

When constructing the parabolic reflector, shape it according to these dimensions, and experiment with the positioning and alignment to optimize the WiFi signal. Keep in mind that this is a simplified DIY approach, and adjustments may be necessary through experimentation to achieve the best results for your specific use case.

To convert the dimensions from inches to millimeters, you can use the conversion factor 1inch=25.4mm1inch=25.4mm. Here are the converted dimensions:

    Width (D): 5 inches
    Dmm≈5×25.4Dmm​≈5×25.4
    Dmm≈127Dmm​≈127 mm

    Height (h): 3 inches
    hmm≈3×25.4hmm​≈3×25.4
    hmm≈76.2hmm​≈76.2 mm

Therefore, the converted dimensions are approximately:

    Width (D): 127 mm
    Height (h): 76.2 mm

Use these converted values when shaping and constructing your parabolic reflector for the DIY WiFi signal booster. Experiment with the positioning and alignment to optimize the performance based on these converted dimensions.

if you reduce the height to 2 inches. Using the formula F≈D216hF≈16hD2​:

    New Height (hh): 2 inches
    hmm≈2×25.4hmm​≈2×25.4
    hmm≈50.8hmm​≈50.8 mm

    Calculate New Focal Length (FF):
    F≈D216×2F≈16×2D2​
    F≈D232F≈32D2​

Assuming you still have a width (DD) of 5 inches:

F≈5232F≈3252​
F≈2532F≈3225​
F≈0.78125F≈0.78125 inches (converted to approximately 19.844 mm)

Therefore, with a reduced height of 2 inches, the new focal length (FF) is approximately 19.844 mm. Use this new value when shaping and constructing your parabolic reflector. Experiment with the positioning and alignment to optimize the performance based on these adjusted dimensions.