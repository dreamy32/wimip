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
curl -sSL https://raw.githubusercontent.com/YOUR_USERNAME/wimip/main/install.sh | bash
```

Or manually:

```bash
git clone https://github.com/YOUR_USERNAME/wimip.git
cd wimip
sudo ./install.sh
```

### Package Managers

#### Debian/Ubuntu (APT)

```bash
# Coming soon
```

#### Fedora/RHEL/CentOS (DNF/YUM)

```bash
# Coming soon
```

### Manual Installation

1. Download the script:
   ```bash
   wget https://raw.githubusercontent.com/YOUR_USERNAME/wimip/main/wimip
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

```bash
sudo rm /usr/local/bin/wimip
```

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Created by YOUR_NAME
