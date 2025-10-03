# wimip - What Is My IP

A simple command-line tool to display your public IP address, local IP address, and geographic location.

## Features

- Display public IP address
- Display local IP address
- Display geographic location (city and region)
- Color-coded output with aligned formatting
- Lightweight and fast

## Installation

### Quick Install (Linux)

```bash
curl -sSL https://raw.githubusercontent.com/dreamy32/wimip/main/install.sh | sudo bash
```

Or manually:

```bash
git clone https://github.com/dreamy32/wimip.git
cd wimip
sudo ./install.sh
```

### Package Managers

#### Debian/Ubuntu (APT)

```bash
# Coming soon
```

#### Fedora/RHEL/CentOS/Rocky Linux (DNF/YUM)

Download and install the RPM package from the [latest release](https://github.com/dreamy32/wimip/releases/latest):

```bash
# Download the RPM
wget https://github.com/dreamy32/wimip/releases/download/v1.0.1/wimip-1.0.1-1.fc42.noarch.rpm

# Install
sudo dnf install ./wimip-1.0.1-1.fc42.noarch.rpm
```

Or using `rpm`:
```bash
sudo rpm -ivh wimip-1.0.1-1.fc42.noarch.rpm
```

**Note:** Despite the `.fc42` naming, this is a pure bash script package (noarch) and works on all Fedora, RHEL, CentOS, AlmaLinux, and Rocky Linux versions.

### Manual Installation

1. Download the script:
   ```bash
   wget https://raw.githubusercontent.com/dreamy32/wimip/main/wimip
   ```

2. Make it executable:
   ```bash
   chmod +x wimip
   ```

3. Move to a directory in your PATH:
   ```bash
   sudo mv wimip /usr/local/bin/
   ```

## Usage

Simply run:

```bash
wimip
```

Example output:
```
Public IP  : 142.115.172.83
Local IP   : 192.168.2.61
Location   : Blainville, Quebec
```

## Requirements

- `curl` - for fetching public IP and location data
- `hostname` - for getting local IP address
- `awk` - for text processing

These tools are typically pre-installed on most Linux distributions.

## Dependencies

- Uses `ifconfig.me` for public IP lookup
- Uses `ipinfo.io` for geographic location data

## Uninstall

**If installed via RPM:**
```bash
sudo dnf remove wimip
# or
sudo rpm -e wimip
```

**If installed via install.sh:**
```bash
sudo rm /usr/local/bin/wimip
```

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Created by David Berube
