"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    splited = [i for i in coordinate]
    return (splited[0], splited[1])



def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair. :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    tupleA = 0
    if not isinstance(azara_record[1], tuple):
        tupleA  = convert_coordinate(azara_record[1])
    else:
        tupleA  = azara_record[1]

    tupleB  = 0
    if not isinstance(rui_record[1], tuple):
        tupleB = convert_coordinate(rui_record[1])[1]
    else:
        tupleB = rui_record[1]

    return tupleA == tupleB



def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    else:
        return 'not a match'


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    result = ""

    for tup in combined_record_group:
        line = '('
        for index, val in enumerate(tup):
            if index == 1:
                continue

            if index != 3:
                line = line + "'" + str(val) + "'"
            else:
                line = line + str(val)

            if index < len(tup) - 1:
                line = line + ", "
            else:
                line = line + ")\n"

        result = result + line
        # fugk BethanyG
    return result
