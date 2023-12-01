import os


def compare_essid_across_files(essid, file_list):
    stronger_signals = {}

    for file in file_list:
        with open(file, "r") as current_file:
            for line in current_file:
                if line.startswith("BSSIDs"):
                    continue  # Skip header
                parts = line.strip().split(", ")
                bssid = parts[0].split(":")[1].strip()

                # Extract signal strength and remove " dBm"
                signal_strength_str = parts[2].split(
                    ":")[1].strip().replace(" dBm", "")

                # Handle cases where signal strength is not a valid integer
                try:
                    signal_strength = int(signal_strength_str)
                except ValueError:
                    signal_strength = None

                current_essid = parts[1].split(":")[1].strip()

                if current_essid == essid and signal_strength is not None:
                    if bssid not in stronger_signals or signal_strength > stronger_signals[bssid][1]:
                        stronger_signals[bssid] = (file, signal_strength)

    return stronger_signals


# Example usage:
essid_to_compare = "Guacamole"
file_list = [file for file in os.listdir() if file.endswith(".txt")]
print(file_list)
result = compare_essid_across_files(essid_to_compare, file_list)

if result:
    print(f"Stronger signals for ESSID '{essid_to_compare}':")
    for bssid, (file, strength) in result.items():
        print(f"BSSID: {bssid}, Signal Strength in {file}: {strength} dBm")
else:
    print(f"No common ESSID '{essid_to_compare}' found in the files.")
