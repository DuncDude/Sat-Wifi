import os
import subprocess
import signal
import time


class WiFiScanner:
    def set_monitor_mode(self, interface):
        # Disable the interface before setting it to monitor mode
        os.system(f"sudo ifconfig {interface} down")
        
        # Unblock potential RF kill switch
        os.system(f"sudo rfkill unblock 0")

        # Put the wireless interface into monitor mode using airmon-ng
        os.system(f"sudo airmon-ng start {interface}")
        return f"{interface}"

    def start_airodump(self, interface, output_file):
        command = f"sudo airodump-ng --wps -w {output_file} {interface}"
        print(f"Running command: {command}")

        process = subprocess.Popen(command, shell=True, preexec_fn=os.setsid)
        return process

    def stop_airodump(self, process):
        # Stop the airodump-ng process
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)

    def get_highest_signal_bssids(self, output_file):
        with open(output_file + "-01.csv", "r") as file:
            lines = file.readlines()[2:]  # Skip the header lines

        highest_bssid_dict = {}
        for line in lines:
            values = line.split(",")
            if len(values) >= 14:  # Ensure the line has at least 14 columns
                bssid = values[0]
                essid = values[13].strip()  # Extract and remove leading/trailing whitespaces
                signal = int(values[8])
                if bssid not in highest_bssid_dict or signal > highest_bssid_dict[bssid][1]:
                    highest_bssid_dict[bssid] = (essid, signal)

        return highest_bssid_dict




    def save_to_txt(self, highest_bssid_dict, txt_file):
        with open(txt_file, "w") as file:
            file.write("BSSIDs, ESSIDs, and their highest signal strengths:\n")
            for bssid, (essid, highest_signal) in highest_bssid_dict.items():
                file.write(f"BSSID: {bssid}, ESSID: {essid}, Highest Signal Strength: {highest_signal} dBm\n")


    def run(self, interface, txt_file):
        output_file = "wifiNetworks"
        txt_file = f"{txt_file}.txt"

        print(f"Setting {interface} to monitor mode...")
        monitor_mode_interface = self.set_monitor_mode(interface)

        try:
            print(f"Starting airodump-ng on interface {monitor_mode_interface}...")
            airodump_process = self.start_airodump(monitor_mode_interface, output_file)

            # Run airodump-ng for 30 seconds
            time.sleep(30)

            print("30 seconds have passed. Getting BSSIDs with their highest signal strengths...")
            highest_bssid_dict = self.get_highest_signal_bssids(output_file)
            self.save_to_txt(highest_bssid_dict, txt_file)
            print(f"Results saved to {txt_file}")

        except KeyboardInterrupt:
            pass  # Allow the user to interrupt the script with Ctrl+C

        finally:
            print(f"Stopping airodump-ng on interface {monitor_mode_interface}...")
            self.stop_airodump(airodump_process)

            # Enable the interface back after capturing
            os.system(f"sudo ifconfig {monitor_mode_interface} up")

            print(f"Reverting {monitor_mode_interface} to managed mode...")
            os.system(f"sudo airmon-ng stop {monitor_mode_interface}")

            self.cleanup_files()
    def cleanup_files(self):
        for file_name in os.listdir():
            if file_name.endswith((".py", ".txt")) or os.path.isdir(file_name):
                continue
            try:
                os.remove(file_name)
                print(f"Deleted file: {file_name}")
            except Exception as e:
                print(f"Error deleting file {file_name}: {e}")
    # if __name__ == "__main__":
    #     interface = "wlp2s0"  # Replace with your WiFi interface
    #     main(interface)
