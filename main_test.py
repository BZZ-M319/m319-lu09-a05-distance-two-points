import main
from main import calculate_distance
import pytest
def test_calculate_distance():
    assert calculate_distance(0, 0, 3, 4) == 5
    assert calculate_distance(600000, 200000, 680000, 250000) == pytest.approx(94339.81132056603, 0.01)


# Use monkeypatch to simulate user input for the main function
def test_main(monkeypatch, capsys):
    # Simulate user inputs
    monkeypatch.setattr('builtins.input', lambda _: '600000')
    monkeypatch.setattr('builtins.input', lambda _: '200000')
    monkeypatch.setattr('builtins.input', lambda _: '680000')
    monkeypatch.setattr('builtins.input', lambda _: '250000')

    # Now we would call the main function
    main.main()

    # Capture the output
    captured = capsys.readouterr()

    # Check if the output is as expected
    assert "Die Distanz zwischen den beiden Punkten beträgt:" in captured.out
