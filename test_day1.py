from day1 import dial

def test_passes_through_zero():
    mock_input_data = [
        "R12",
        "L563",
        "R43",
        "L2",
        "L410"
    ]

    _, result2 = dial(mock_input_data)
    assert result2 == 11

def test_passes_through_zero_example():
    mock_input_data = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82"
    ]

    _, result2 = dial(mock_input_data)
    assert result2 == 6