from importlib import import_module
from importlib import reload
import os
import sys

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time


dirs = os.listdir()
imported_modules = []
current_module = __file__

for dir in dirs:
    dir_name = str(dir)
    if dir_name.endswith(".py"):
        module_name = dir_name[:-3]
        if module_name == current_module[:-3]:
            pass
        else:
            imported_module = import_module(module_name)
            globals()[module_name] = imported_module
            imported_modules.append(imported_module)

patterns = ["*/log_mod.py"]
ignore_patterns = ""
ignore_directories = False
case_sensitive = True
my_event_handler = PatternMatchingEventHandler(
    patterns, ignore_patterns, ignore_directories, case_sensitive
)


def on_modified(event):
    print(f"{event.src_path} has been modified")
    for mod in imported_modules:
        mod = reload(mod)
        print(f"{mod.__name__} has been reloaded")


my_event_handler.on_modified = on_modified

path = "."
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
