from chap2.sort import selection_sort

def test_selection_sort():
    a = [13, 15, 78, 68, 91, 6, 71, 20, 98, 8]
    sorted_a = [6, 8, 13, 15, 20, 68, 71, 78, 91, 98]
    actual = selection_sort(a)
    assert actual == sorted_a
