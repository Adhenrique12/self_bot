from handlers.tools import load_plugins as lp
from handlers.plugins import ALL_MODULES as USER_MODULES
from telethon import TelegramClient
import toml


toml_config = toml.load("config.toml")
client = TelegramClient(
    "bot", toml_config["user_api"]["id"], toml_config["user_api"]["hash"])


def main():
    with client:
        client.start()
        lp.load_plugins(USER_MODULES, client)
        print("User Bot Marques started.")
        client.run_until_disconnected()


if __name__ == "__main__":
    print("Starting...")

    try:
        main()
    except KeyboardInterrupt:
        print("Client terminated.")
