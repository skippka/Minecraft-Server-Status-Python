from mcstatus import JavaServer

def get_server_info(ip):
    server = JavaServer.lookup(ip)
    try:
        status = server.status()
        print(f"Information about server {ip}:")
        print(f"Online: {status.players.online} player(s)")
        print(f"MOTD: {status.motd}")
        print(f"Server version: {status.version.name}")
        print(f"Server is running: {status.latency} ms latency")
        print(f"Server icon: {status.icon}")
    except Exception as e:
        print(f"Failed to get information about the server {ip}. Error: {e}")

if __name__ == "__main__":
    ip = input("Enter the Minecraft server IP: ")
    get_server_info(ip)
