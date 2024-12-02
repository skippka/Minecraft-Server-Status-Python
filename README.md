
# Minecraft Server Status Python

This Python script allows you to check the status of a Minecraft server. It provides detailed information about the server, such as the number of online players, MOTD (Message of the Day), version, and latency.

## Features

- Displays the number of online players.
- Shows the Message of the Day (MOTD) from the server.
- Provides the server version.
- Reports the server's latency (ping).

## Requirements

- Python 3.x
- `mcstatus` library

## Installation

To use this script, you'll need to install the necessary dependencies.

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/skippka/minecraft-server-status.git
   ```

2. Navigate to the project folder:

   ```bash
   cd minecraft-server-status
   ```

3. Install the required Python package:

   ```bash
   pip install mcstatus
   ```

## Usage

1. Run the script:

   ```bash
   python server_status.py
   ```

2. When prompted, enter the IP address of the Minecraft server you want to check. You can enter just the IP (e.g., `play.hypixel.net`) or include the port (e.g., `127.0.0.1:25565`).

3. The script will display the following information:
   - The number of online players.
   - The Message of the Day (MOTD).
   - The server version.
   - The server's latency (ping).

### Example:

```bash
Enter the Minecraft server IP: play.hypixel.net
Information about server play.hypixel.net:
Online: 2000 player(s)
MOTD: Welcome to Hypixel Network!
Server version: 1.16.5
Server is running: 50 ms latency
```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. All contributions are welcome!

### Steps to contribute:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your branch (`git push origin feature-branch`).
6. Create a pull request.

## Issues

If you encounter any problems, feel free to open an issue on the GitHub repository. Be sure to provide a clear description of the problem and any relevant details so that we can assist you more effectively.
