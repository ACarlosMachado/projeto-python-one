from src.counter import count_ocurrences


def test_counter():
    count_python = count_ocurrences("src/jobs.csv", "Python")
    assert count_python == 1639
