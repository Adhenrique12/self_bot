from handlers.tools import import_modules as ip

from handlers.plugins import ALL_MODULES as USER_MODULES

from handlers import client

client = client.client


def task1():
    with client:
        client.start()
        ip.import_modules(USER_MODULES, client)
        print("User Bot Marques started.")
        client.run_until_disconnected()


if __name__ == "__main__":
    print("Starting...")

    try:
        task1()
    except KeyboardInterrupt:
        print("Client terminated.")
