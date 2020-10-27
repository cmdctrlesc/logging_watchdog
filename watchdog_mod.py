from importlib import import_module
from importlib import reload

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
import main_mod

patterns = "*"
ignore_patterns = ""
ignore_directories = False
case_sensitive = True
my_event_handler = PatternMatchingEventHandler(
    patterns, ignore_patterns, ignore_directories, case_sensitive
)


def on_modified(event):
    global main_mod
    print(f"{event.src_path} has been modified")
    main_mod = reload(main_mod)

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
