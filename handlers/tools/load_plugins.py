import importlib
from telethon import TelegramClient


def load_plugins(plugins: list[str], client: TelegramClient):
    """
    Loads all plugins into the client's event handling
    """
    IMPORTED = {}
    for module_name in plugins:
        imported_module = importlib.import_module(
            f"handlers.plugins." + module_name)

        if not hasattr(imported_module, "__mod_name__"):
            imported_module.__mod_name__ = imported_module.__name__

        if not imported_module.__mod_name__.lower() in IMPORTED:
            IMPORTED[imported_module.__mod_name__.lower()] = imported_module
        else:
            raise Exception(
                "Can't have two plugins with the same name, please change one of them."
            )

        client.add_event_handler(imported_module.cmd)
