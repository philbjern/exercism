public class LogLevels {
    
    public static String message(String logLine) {
        String message = logLine.substring(logLine.indexOf(":") + 1);
        return message.trim();
    }

    public static String logLevel(String logLine) {
        return logLine.substring(1, logLine.indexOf("]")).toLowerCase();
    }

    public static String reformat(String logLine) {
        return message(logLine) + " (" + logLevel(logLine) + ")";
    }
}
