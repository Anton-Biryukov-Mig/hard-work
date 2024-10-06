from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def id_state_date() -> List[Dict[str, Any]]:
    return [
        {"id": 5, "state": "EXECUTED", "date": "2021-07-03"},
        {"id": 6, "state": "CANCELED", "date": "2021-09-08"},
        {"id": 7, "state": "EXECUTED", "date": "2019-01-02"},
        {"id": 8, "state": "CANCELED", "date": "2014-07-01"},
    ]


@pytest.mark.parametrize(
    "state, expected_output",
    [
        pytest.param(
            "EXECUTED",
            [
                {"state": "EXECUTED", "date": "2021-07-03"},
                {"state": "EXECUTED", "date": "2019-01-02"},
            ],
            id="filter by executed state",
        ),
        pytest.param(
            "PENDING",
            [],
            id="filter by pending state",
        ),
        pytest.param(
            "INVALID",
            [],
            id="filter by invalid state",
        ),
    ],
)
def test_filter_by_state(
    id_state_date: List[Dict[str, Any]], state: str, expected_output: List[Dict[str, Any]]
) -> None:
    """Тест функции filter_by_state"""
    assert filter_by_state(id_state_date, state) == expected_output


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    return [
        {"state": "EXECUTED", "date": "2024-05-20T18:00:00.000"},
        {"state": "EXECUTED", "date": "2023-12-31T15:30:00.000"},
        {"state": "PENDING", "date": "2022-08-15T10:45:00.000"},
    ]


@pytest.mark.parametrize(
    "reverse, expected_output",
    [
        (
            True,
            [
                {"state": "EXECUTED", "date": "2024-05-20T18:00:00.000"},
                {"state": "EXECUTED", "date": "2023-12-31T15:30:00.000"},
                {"state": "PENDING", "date": "2022-08-15T10:45:00.000"},
            ],
        ),
        (
            False,
            [
                {"state": "PENDING", "date": "2022-08-15T10:45:00.000"},
                {"state": "EXECUTED", "date": "2023-12-31T15:30:00.000"},
                {"state": "EXECUTED", "date": "2024-05-20T18:00:00.000"},
            ],
        ),
    ],
)
def test_sort_by_date(sample_data: List[Dict[str, Any]], reverse: bool, expected_output: List[Dict[str, Any]]) -> None:
    """Тест функции sort_by_date"""
    assert sort_by_date(sample_data, reverse=reverse) == expected_output
