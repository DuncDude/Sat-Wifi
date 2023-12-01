from sat import WiFiScanner

wifi_scanner = WiFiScanner()
wifi_interface = "wlp2s0"
wifi_scanner.run(wifi_interface, "test2")