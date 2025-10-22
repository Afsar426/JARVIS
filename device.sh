#!/usr/bin/env bash
set -euo pipefail

# device.sh - macOS / Linux replacement for the Windows device.bat
# Usage: ./device.sh

echo "Checking for adb..."
if ! command -v adb >/dev/null 2>&1; then
  echo "adb not found. Install it with Homebrew: brew install android-platform-tools"
  exit 1
fi

echo "Restarting adb server..."
adb kill-server || true
adb start-server

echo "Ensure your Android device is connected via USB and USB debugging is enabled. Press Enter to continue..."
read -r

echo "Setting device to TCP/IP on port 5555..."
adb tcpip 5555
sleep 3

# Try to fetch the device IP address from common wireless interfaces
ipfull=""
for iface in wlan0 wlan1 rmnet_data0; do
  ipfull=$(adb shell ip -f inet addr show "$iface" 2>/dev/null | awk '/inet /{print $2}' | tr -d '\r')
  if [ -n "$ipfull" ]; then
    break
  fi
done

if [ -z "$ipfull" ]; then
  echo "Could not read the device IP from common interfaces. Run 'adb shell ip addr' to debug." >&2
  exit 1
fi

# strip CIDR
ip=${ipfull%%/*}

echo "Connecting to device at $ip:5555..."
adb connect "$ip:5555"

echo "Done. If connection fails, verify device Wi-Fi IP and that both host and device are on the same network."
