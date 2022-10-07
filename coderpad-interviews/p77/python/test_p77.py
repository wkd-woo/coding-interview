from p77 import solution, solution2


def test_p77_solution():
    intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
    assert solution(intervals) == [(1, 3), (4, 10), (20, 25)]

    intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)]
    assert solution(intervals) == [(1, 3), (4, 10), (20, 27)]

    intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
    assert solution2(intervals) == [(1, 3), (4, 10), (20, 25)]

    intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)]
    assert solution2(intervals) == [(1, 3), (4, 10), (20, 27)]


test_p77_solution()
