import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_name = event.src_path
            print(f"New file created: {file_name}")

            
            subprocess.Popen(['python', 'd.py', file_name])


if __name__ == "__main__":
    folder_to_watch = r'C:\Users\onkar\Desktop\New folder\upload'  # Replace with the folder you want to monitor
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
