#!/bin/bash
# wimip installation script

set -e

INSTALL_DIR="/usr/local/bin"
SCRIPT_NAME="wimip"

echo "Installing wimip..."

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "This script requires sudo privileges."
    echo "Please run: sudo ./install.sh"
    exit 1
fi

# Check dependencies
echo "Checking dependencies..."
MISSING_DEPS=""

command -v curl >/dev/null 2>&1 || MISSING_DEPS="$MISSING_DEPS curl"
command -v hostname >/dev/null 2>&1 || MISSING_DEPS="$MISSING_DEPS hostname"
command -v awk >/dev/null 2>&1 || MISSING_DEPS="$MISSING_DEPS awk"

if [ -n "$MISSING_DEPS" ]; then
    echo "Error: Missing required dependencies:$MISSING_DEPS"
    echo "Please install them and try again."
    exit 1
fi

# Copy the script
echo "Installing $SCRIPT_NAME to $INSTALL_DIR..."
cp "$SCRIPT_NAME" "$INSTALL_DIR/$SCRIPT_NAME"
chmod +x "$INSTALL_DIR/$SCRIPT_NAME"

echo "✓ Installation complete!"
echo "You can now run: $SCRIPT_NAME"
