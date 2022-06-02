import java.util.Locale;
import java.util.Map;

class ResistorColor {

    private static final Map<String, Integer> RESISTANCE = Map.ofEntries(
            Map.entry("black", 0),
            Map.entry("brown", 1),
            Map.entry("red", 2),
            Map.entry("orange", 3),
            Map.entry("yellow", 4),
            Map.entry("green", 5),
            Map.entry("blue", 6),
            Map.entry("violet", 7),
            Map.entry("grey", 8),
            Map.entry("white", 9)
    );

    int colorCode(String color) {
        if (!RESISTANCE.containsKey(color.toLowerCase(Locale.ROOT))) {
            throw new IllegalArgumentException("Unknown color code - " + color);
        }
        return RESISTANCE.get(color.toLowerCase(Locale.ROOT));
    }

    String[] colors() {
        return RESISTANCE.entrySet().stream()
                .sorted(Map.Entry.comparingByValue())
                .map(Map.Entry::getKey)
                .toArray(String[]::new);
    }
}
