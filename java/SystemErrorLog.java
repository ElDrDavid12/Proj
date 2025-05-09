public class SystemErrorLog {

    public static void main(String[] args) {
        SystemLog[] logs = new SystemLog[] {
            new SystemLog("0042A", "Memory Overlap", "Sector 7–R", "Process injected from UNKNOWN source."),
            new SystemLog("0043B", "Message Repeated", "“I am still here.”", "Matches administrator speech (inactive 119 days)."),
            new SystemLog("0044C", "Visual Feed Error", "Subject vanished", "Appeared outside room. Doors locked."),
            new SystemLog("0045D", "Voice Pattern Detected", "R. Elwin", "Technician marked deceased. Audio: 'Stop listening. It doesn’t like being heard.'"),
            new SystemLog("0046E", "Final Log", "Operator typed:", "‘It's not a bug. It's learning...’ then signed off.")
        };

        for (SystemLog log : logs) {
            if (log.getMessage().contains("learning")) {
                System.out.println("[CRITICAL] " + log);
            } else {
                System.out.println("[INFO] " + log);
            }
        }

        System.out.println("\nWARNING: Do not reboot system. Observation has already begun.");
    }
}

class SystemLog {
    String id;
    String error;
    String context;
    String message;

    public SystemLog(String id, String error, String context, String message) {
        this.id = id;
        this.error = error;
        this.context = context;
        this.message = message;
    }

    public String getMessage() {
        return message;
    }

    public String toString() {
        return "[" + id + "] " + error + " | " + context + " — " + message;
    }
}
