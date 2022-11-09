from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    get_jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    key_in_english = {'title': '', 'salary': 0, 'type': 0}
    for job in get_jobs:
        assert job.keys() == key_in_english.keys()
