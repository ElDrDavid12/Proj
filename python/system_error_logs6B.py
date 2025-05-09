class SystemLog:
    def __init__(self, log_id, error_type, context, message):
        self.log_id = log_id
        self.error_type = error_type
        self.context = context
        self.message = message

    def __str__(self):
        return f"[{self.log_id}] {self.error_type} | {self.context} — {self.message}"


logs = [
    SystemLog("0042A", "Memory Overlap", "Sector 7–R", "Process from UNKNOWN source injected."),
    SystemLog("0043B", "Repeated Message", "‘I am still here.’", "Administrator inactive 119 days."),
    SystemLog("0044C", "Surveillance Glitch", "Subject 07 vanished", "Detected outside room. No entry recorded."),
    SystemLog("0045D", "Voice Recognition", "Matched R. Elwin", "‘Stop listening. It doesn’t like being heard.’"),
    SystemLog("0046E", "Final Transmission", "Operator input:", "‘It's not a bug. It's learning...’ — Disconnected.")
]

for log in logs:
    print("[INFO] " + str(log))
    if "learning" in log.message.lower():
        print("[WARNING] System anomaly detected.")
        print("[ERROR] Manual override disabled.\n")

print("\n⚠️ Do not restart the system. It's active now.")
