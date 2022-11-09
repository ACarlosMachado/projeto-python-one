from src.sorting import sort_by
import pytest


@pytest.fixture
def list_jobs():
    return [
        {'title': 'a', 'min_salary': 1000, 'max_salary': 8500,
            'date_posted': '2000-01-05'},
        {'title': 'b', 'min_salary': 2000, 'max_salary': 85000,
            'date_posted': '2010-01-05'},
        {'title': 'c', 'min_salary': 500, 'max_salary': 37500,
            'date_posted': '2020-01-05'}
    ]


def test_sort_by_criteria(list_jobs):
    sort_by(list_jobs, 'min_salary')
    assert list_jobs == [
        {'title': 'c', 'min_salary': 500, 'max_salary': 37500,
            'date_posted': '2020-01-05'},
        {'title': 'a', 'min_salary': 1000, 'max_salary': 8500,
            'date_posted': '2000-01-05'},
        {'title': 'b', 'min_salary': 2000, 'max_salary': 85000,
            'date_posted': '2010-01-05'}
        ]
    sort_by(list_jobs, 'max_salary')
    assert list_jobs == [
        {'title': 'b', 'min_salary': 2000, 'max_salary': 85000,
            'date_posted': '2010-01-05'},
        {'title': 'c', 'min_salary': 500, 'max_salary': 37500,
            'date_posted': '2020-01-05'},
        {'title': 'a', 'min_salary': 1000, 'max_salary': 8500,
            'date_posted': '2000-01-05'}
        ]
    sort_by(list_jobs, 'date_posted')
    assert list_jobs == [
        {'title': 'c', 'min_salary': 500, 'max_salary': 37500,
            'date_posted': '2020-01-05'},
        {'title': 'b', 'min_salary': 2000, 'max_salary': 85000,
            'date_posted': '2010-01-05'},
        {'title': 'a', 'min_salary': 1000, 'max_salary': 8500,
            'date_posted': '2000-01-05'}
        ]
