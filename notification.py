import pyinotify

# Inotify event handler class
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CLOSE_WRITE(self, event):
        handle_snort_alert(event.pathname)

# Set up inotify to watch the IDS log directory
def monitor_ids_logs():
    try:
        wm = pyinotify.WatchManager()
        notifier = pyinotify.Notifier(wm, EventHandler())
        wm.add_watch(IDS_LOG_DIR, pyinotify.IN_CLOSE_WRITE)
        print("Monitoring Snort IDS logs...")
        notifier.loop()
    except Exception as e:
        print(f"Error monitoring IDS logs: {e}")