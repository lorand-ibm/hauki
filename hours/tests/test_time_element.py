import datetime

from hours.enums import State
from hours.models import TimeElement, combine_and_apply_override


def test_combine_and_apply_override_full_day_override():
    te1 = TimeElement(
        start_time=datetime.time(hour=8, minute=0),
        end_time=datetime.time(hour=16, minute=0),
        resource_state=State.OPEN,
        override=False,
        full_day=False,
    )

    te2 = TimeElement(
        start_time=None,
        end_time=None,
        resource_state=State.CLOSED,
        override=True,
        full_day=True,
    )

    assert combine_and_apply_override([te1, te2]) == [te2]


def test_combine_and_apply_override_combine_two_same():
    te1 = TimeElement(
        start_time=datetime.time(hour=8, minute=0),
        end_time=datetime.time(hour=12, minute=0),
        resource_state=State.OPEN,
        override=False,
        full_day=False,
    )

    te2 = TimeElement(
        start_time=datetime.time(hour=10, minute=0),
        end_time=datetime.time(hour=16, minute=0),
        resource_state=State.OPEN,
        override=False,
        full_day=False,
    )

    assert combine_and_apply_override([te1, te2]) == [
        TimeElement(
            start_time=datetime.time(hour=8, minute=0),
            end_time=datetime.time(hour=16, minute=0),
            resource_state=State.OPEN,
            override=False,
            full_day=False,
        )
    ]


def test_combine_and_apply_override_two_separate():
    te1 = TimeElement(
        start_time=datetime.time(hour=8, minute=0),
        end_time=datetime.time(hour=12, minute=0),
        resource_state=State.OPEN,
        override=False,
        full_day=False,
    )

    te2 = TimeElement(
        start_time=datetime.time(hour=13, minute=0),
        end_time=datetime.time(hour=16, minute=0),
        resource_state=State.OPEN,
        override=False,
        full_day=False,
    )

    assert combine_and_apply_override([te1, te2]) == [te1, te2]


def test_combine_and_apply_override_one_overriding():
    te1 = TimeElement(
        start_time=datetime.time(hour=8, minute=0),
        end_time=datetime.time(hour=16, minute=0),
        resource_state=State.OPEN,
        override=False,
        full_day=False,
    )

    te2 = TimeElement(
        start_time=datetime.time(hour=12, minute=0),
        end_time=datetime.time(hour=14, minute=0),
        resource_state=State.CLOSED,
        override=True,
        full_day=False,
    )

    assert combine_and_apply_override([te1, te2]) == [
        TimeElement(
            start_time=datetime.time(hour=12, minute=0),
            end_time=datetime.time(hour=14, minute=0),
            resource_state=State.CLOSED,
            override=True,
            full_day=False,
        ),
    ]


def test_combine_and_apply_override_multiple_overriding():
    te1 = TimeElement(
        start_time=datetime.time(hour=8, minute=0),
        end_time=datetime.time(hour=16, minute=0),
        resource_state=State.OPEN,
        override=False,
        full_day=False,
    )

    te2 = TimeElement(
        start_time=datetime.time(hour=9, minute=0),
        end_time=datetime.time(hour=11, minute=0),
        resource_state=State.CLOSED,
        override=True,
        full_day=False,
    )

    te3 = TimeElement(
        start_time=datetime.time(hour=13, minute=0),
        end_time=datetime.time(hour=15, minute=0),
        resource_state=State.CLOSED,
        override=True,
        full_day=False,
    )

    assert combine_and_apply_override([te1, te2, te3]) == [te2, te3]


# def test_combine_and_apply_override_multiple_overriding_overlapping():
#     te1 = TimeElement(
#         start_time=datetime.time(hour=8, minute=0),
#         end_time=datetime.time(hour=16, minute=0),
#         resource_state=State.OPEN,
#         override=False,
#         full_day=False,
#     )
#
#     te2 = TimeElement(
#         start_time=datetime.time(hour=12, minute=0),
#         end_time=datetime.time(hour=14, minute=0),
#         resource_state=State.CLOSED,
#         override=True,
#         full_day=False,
#     )
#
#     te3 = TimeElement(
#         start_time=datetime.time(hour=13, minute=0),
#         end_time=datetime.time(hour=15, minute=0),
#         resource_state=State.CLOSED,
#         override=True,
#         full_day=False,
#     )
#
#     assert combine_and_apply_override([te1, te2, te3]) == [
#         TimeElement(
#             start_time=datetime.time(hour=12, minute=0),
#             end_time=datetime.time(hour=15, minute=0),
#             resource_state=State.CLOSED,
#             override=True,
#             full_day=False,
#         ),
#     ]
