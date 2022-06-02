import java.util.Map;
import java.util.stream.Stream;

public class Blackjack {

    private final Map<String, Integer> CARDS = Map.ofEntries(
            Map.entry("ace", 11),
            Map.entry("two", 2),
            Map.entry("three", 3),
            Map.entry("four", 4),
            Map.entry("five", 5),
            Map.entry("six", 6),
            Map.entry("seven", 7),
            Map.entry("eight", 8),
            Map.entry("nine", 9),
            Map.entry("ten", 10),
            Map.entry("jack", 10),
            Map.entry("queen", 10),
            Map.entry("king", 10)
    );

    private static final int BLACKJACK = 21;

    private static final String STAND = "S";
    private static final String HIT = "H";
    private static final String SPLIT = "P";
    private static final String AUTOMATICALLY_WIN = "W";

    public int parseCard(String card) {
        if (!CARDS.containsKey(card)) {
            throw new IllegalArgumentException(String.format("Unknown card '%s'", card));
        }
        return CARDS.get(card);
    }

    public boolean isBlackjack(String card1, String card2) {
        return Stream.of(card1, card2)
                .mapToInt(this::parseCard)
                .sum() == BLACKJACK;
    }

    public String largeHand(boolean isBlackjack, int dealerScore) {
//        if (isBlackjack) {
//            if (dealerScore < 10) {
//                return AUTOMATICALLY_WIN;
//            } else {
//                return STAND;
//            }
//        } else {
//            return SPLIT;
//        }

        if (!isBlackjack) {
            return SPLIT;
        }

        if (dealerScore < 10) {
            return AUTOMATICALLY_WIN;
        }

        return STAND;
    }

    public String smallHand(int handScore, int dealerScore) {
//        if (handScore >= 17) {
//            return STAND;
//        } else if (handScore >= 12) {
//            if (dealerScore >= 7) {
//                return HIT;
//            } else {
//                return STAND;
//            }
//        } else {
//            return HIT;
//        }

        if (handScore >= 17) {
            return STAND;
        }

        if (handScore <= 11) {
            return HIT;
        }

        return dealerScore >= 7 ? HIT : STAND;
    }

    // FirstTurn returns the semi-optimal decision for the first turn, given the cards of the player and the dealer.
    // This function is already implemented and does not need to be edited. It pulls the other functions together in a
    // complete decision tree for the first turn.
    public String firstTurn(String card1, String card2, String dealerCard) {
        int handScore = parseCard(card1) + parseCard(card2);
        int dealerScore = parseCard(dealerCard);

        if (20 < handScore) {
            return largeHand(isBlackjack(card1, card2), dealerScore);
        } else {
            return smallHand(handScore, dealerScore);
        }
    }
}
