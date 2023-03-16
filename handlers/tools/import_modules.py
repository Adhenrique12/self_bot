import importlib


def import_modules(modules, client):
    IMPORTED = {}
    for module_name in modules:
        imported_module = importlib.import_module(f"handlers.plugins." + module_name)
        if not hasattr(imported_module, "__mod_name__"):
            imported_module.__mod_name__ = imported_module.__name__
        if not imported_module.__mod_name__.lower() in IMPORTED:
            IMPORTED[imported_module.__mod_name__.lower()] = imported_module
        else:
            raise Exception(
                "Can't have two modules with the same name! Please change one"
            )
            
        client.add_event_handler(imported_module.cmd)   