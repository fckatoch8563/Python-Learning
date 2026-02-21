def find_most_repetitive(L1):
    """Find the most repetitive element in a list using a plain dictionary."""
    if not L1:
        return None, 0, {}

    freq = {}
    for item in L1:
        freq[item] = freq.get(item, 0) + 1

    # Pick the element with the highest count
    most_repetitive, max_count = max(freq.items(), key=lambda kv: kv[1])

    return most_repetitive, max_count, freq


def _run_tests():
    """Minimal sanity checks."""
    assert find_most_repetitive([]) == (None, 0, {})
    assert find_most_repetitive([1, 1, 2])[:2] == (1, 2)
    print("Tests passed")


if __name__ == "__main__":
    _run_tests()

    # Test with the given list
    L1 = [1, 2, 2, 3, 2, 3, 4, 5]

    element, frequency, frequencies = find_most_repetitive(L1)

    print(f"List: {L1}")
    print(f"\nElement frequencies:")
    for elem in sorted(frequencies):
        count = frequencies[elem]
        print(f"  {elem} appears {count} time(s)")

    print(f"\nMost repetitive element: {element}")
    print(f"Frequency: {frequency} times")
