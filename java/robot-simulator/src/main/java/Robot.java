import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;

public class Robot {

    private GridPosition position;
    private Orientation orientation;
    private static final List<Orientation> orientationList = new ArrayList<>(Arrays.asList(Orientation.values()));
    private static int orientationIndex;

    public Robot(GridPosition position, Orientation orientation) {
        this.position = position;
        this.orientation = orientation;
        orientationIndex = orientationList.indexOf(orientation);
    }

    public Orientation getOrientation() {
        return orientation;
    }

    public GridPosition getGridPosition() {
        return position;
    }

    public void turnRight() {
        orientationIndex += 1;
        if (orientationIndex > orientationList.size() - 1) {
            orientationIndex = 0;
        }

        orientation = orientationList.get(orientationIndex);
    }

    public void turnLeft() {
        orientationIndex -= 1;
        if (orientationIndex < 0) {
            orientationIndex = orientationList.size() - 1;
        }

        orientation = orientationList.get(orientationIndex);
    }

    public void advance() {
        int x = position.x;
        int y = position.y;

        switch (orientation) {
            case NORTH:
                y += 1;
                break;
            case EAST:
                x += 1;
                break;
            case SOUTH:
                y -= 1;
                break;
            case WEST:
                x -= 1;
                break;
        }

        position = new GridPosition(x, y);
    }

    public void simulate(String controlStream) {
        controlStream.toUpperCase(Locale.ROOT)
                .chars()
                .mapToObj(i -> (char) i)
                .forEach(c -> {
                    if (c == 'R') {
                        this.turnRight();
                    } else if (c == 'L') {
                        this.turnLeft();
                    } else if (c == 'A') {
                        this.advance();
                    }
                });
    }

}