import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Say {

    public String say(long number) {
        String numberString = String.valueOf(number);
        StringBuilder output = new StringBuilder();

        List<String> digitsWords = IntStream.range(0, numberString.length())
                .mapToObj(i -> {
                    return getDigitWord(numberString.charAt(i));
                }).toList();

        List<String> thousandsList = new ArrayList<>();

        StringBuilder thousand = new StringBuilder();
        for (int i = numberString.length() - 1; i >= 0; i--) {
            thousand.append(numberString.charAt(numberString.length() - i - 1));
            if (i % 3 == 0) {
                String result = thousand.toString();
                if (result.equalsIgnoreCase("000")) {
                    thousandsList.add("0");
                } else {
                    thousandsList.add(result);
                }
                thousand = new StringBuilder();
            }
        }

        System.out.println(thousandsList);

        return output.toString();
    }

    public String getDigitWord(char c) {
        return switch (c) {
            case '0' -> "zero";
            case '1' -> "one";
            case '2' -> "two";
            case '3' -> "three";
            case '4' -> "four";
            case '5' -> "five";
            case '6' -> "six";
            case '7' -> "seven";
            case '8' -> "eight";
            case '9' -> "nine";
            default -> null;
        };
    }

}
