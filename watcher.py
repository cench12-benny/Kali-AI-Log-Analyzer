import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

print("========================================")
print("LAUNCHING KALI AUTOMATED BACKGROUND WATCHER")
print("========================================")

current_folder = os.path.dirname(os.path.abspath(__file__))
target_csv_name = "network_logs.csv"
engine_script_path = os.path.join(current_folder, "live_cyber_engine.py")

class LogFileWatcherHandler(FileSystemEventHandler):
    """Watches for modifications to our specific Excel CSV file."""
    def __init__(self):
        self.last_triggered = 0

    def on_modified(self, event):
        # Only trigger if the modified file matches our spreadsheet dataset name
        if os.path.basename(event.src_path) == target_csv_name:
            current_time = time.time()
            # 2-second cooldown to stop Windows from running the script twice on one save
            if current_time - self.last_triggered > 2:
                self.last_triggered = current_time
                print(f"\n[!] DATA CHANGE DETECTED: {target_csv_name} has been updated!")
                print("[!] Automatically spinning up AI active defense pipeline...\n")
                
                # This line launches your main cyber engine automatically!
                subprocess.run(["py", engine_script_path])
                print("\n[+] Watcher standing by. Monitoring background system files...")

if __name__ == "__main__":
    event_handler = LogFileWatcherHandler()
    observer = Observer()
    
    # Start tracking your project folder paths
    observer.schedule(event_handler, path=current_folder, recursive=False)
    observer.start()
    
    print(f"[+] SUCCESS: Guard dog active. Watching for changes to {target_csv_name}...")
    print("[+] Keep this window running in the background while you work.")
    print("========================================")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[-] Shutting down background monitor cleanly.")
        observer.stop()
    observer.join()
