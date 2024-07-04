
# Inside lib/testing/lib_test.py or similar
import pytest
from lib.list_comprehension import return_evens

class TestReturnEvens:
    def test_return_empty_list_if_odds(self):
        num_list = range(1, 10, 2)
        assert return_evens(num_list) == []

if __name__ == "__main__":
    pytest.main()
