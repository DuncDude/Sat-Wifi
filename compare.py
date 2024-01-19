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

def print_average_signal_strength(file_list):
    essid_signals = {}

    for file in file_list:
        with open(file, "r") as current_file:
            for line in current_file:
                if line.startswith("BSSIDs"):
                    continue  # Skip header
                parts = line.strip().split(", ")
                essid = parts[1].split(":")[1].strip()

                # Extract signal strength and remove " dBm"
                signal_strength_str = parts[2].split(
                    ":")[1].strip().replace(" dBm", "")

                # Handle cases where signal strength is not a valid integer
                try:
                    signal_strength = int(signal_strength_str)
                except ValueError:
                    signal_strength = None

                if essid not in essid_signals:
                    essid_signals[essid] = []

                if signal_strength is not None:
                    essid_signals[essid].append(signal_strength)

    # Calculate average signal strength for each ESSID
    average_signals = {
        essid: sum(signal_list) / len(signal_list)
        for essid, signal_list in essid_signals.items()
    }

    # Print average signal strength in descending order
    sorted_averages = sorted(average_signals.items(), key=lambda x: x[1], reverse=True)
    print("Average Signal Strength by ESSID (Descending Order):")
    for essid, average_strength in sorted_averages:
        print(f"ESSID: {essid}, Average Strength: {average_strength:.2f} dBm")


# Example usage:
essid_to_compare = "Guacamole"
file_list = [file for file in os.listdir() if file.endswith(".txt")]
print(file_list)
result = compare_essid_across_files(essid_to_compare, file_list)

if result:
    print(f"Stronger signals for ESSID '{essid_to_compare}':")
    for bssid, (file, strength) in result.items():
        print(f"BSSID: {bssid}, Signal Strength in {file}: {strength} dBm")
    print("\n")
    print_average_signal_strength(file_list)
else:
    print(f"No common ESSID '{essid_to_compare}' found in the files.")
