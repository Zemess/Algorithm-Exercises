"""
pytest test suite for Topic 1 (Arrays): insert_at / delete_at

Run with:
    pytest test_01a_insert_delete.py -v
"""

from _helpers import load_module

_mod = load_module("01a_insert_delete.py")
insert_at = _mod.insert_at
delete_at = _mod.delete_at


class TestInsertAt:

    def test_insert_middle(self):
        a = [10, 20, 30, 40]
        insert_at(a, 1, 99)
        assert a == [10, 99, 20, 30, 40]

    def test_insert_start(self):
        a = [10, 20, 30, 40]
        insert_at(a, 0, 5)
        assert a == [5, 10, 20, 30, 40]

    def test_insert_end(self):
        a = [10, 20, 30, 40]
        insert_at(a, 4, 99)
        assert a == [10, 20, 30, 40, 99]


class TestDeleteAt:

    def test_delete_middle(self):
        a = [10, 20, 30, 40]
        removed = delete_at(a, 2)
        assert removed == 30
        assert a == [10, 20, 40]

    def test_delete_start(self):
        a = [10, 20, 30, 40]
        removed = delete_at(a, 0)
        assert removed == 10
        assert a == [20, 30, 40]

    def test_delete_last_index(self):
        a = [10, 20, 30, 40]
        removed = delete_at(a, 3)
        assert removed == 40
        assert a == [10, 20, 30]
