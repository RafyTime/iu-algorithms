from collections.abc import Callable


def two_way_partition(trays: list[str], is_fruit: Callable[[str], bool]) -> list[str]:
    i = 0
    for j in range(len(trays)):
        if is_fruit(trays[j]):
            trays[i], trays[j] = trays[j], trays[i]
            i += 1
    return trays


def three_way_partition(
    trays: list[str],
    is_organic_vegetable: Callable[[str], bool],
    is_fruit: Callable[[str], bool],
) -> list[str]:
    left, mid, right = 0, 0, len(trays) - 1
    while mid <= right:
        if is_organic_vegetable(trays[mid]):
            trays[left], trays[mid] = trays[mid], trays[left]
            left += 1
            mid += 1
        elif is_fruit(trays[mid]):
            trays[mid], trays[right] = trays[right], trays[mid]
            right -= 1
        else:
            mid += 1
    return trays


if __name__ == "__main__":
    FRUITS = {"apple", "banana", "mango"}
    items: list[str] = ["apple", "carrot", "banana", "kale", "mango", "potato"]
    print(two_way_partition(items[:], lambda t: t in FRUITS))

    ORGANIC = {"organic_kale", "organic_carrot"}
    VEG = {"organic_kale", "organic_carrot", "carrot", "kale", "potato"}
    trays = [
        "apple",
        "organic_kale",
        "carrot",
        "banana",
        "organic_carrot",
        "potato",
        "mango",
    ]
    print(
        three_way_partition(
            trays[:],
            lambda t: t in ORGANIC,
            lambda t: t not in VEG,
        )
    )
