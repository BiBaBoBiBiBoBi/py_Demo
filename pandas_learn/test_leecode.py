from leecode_solution import combine_two_tables   # 把你的函数放在 solution.py 里
import pandas as pd
import pytest


class TestCombineTwoTables:
    @pytest.fixture(scope="class")
    def person(self) -> pd.DataFrame:
        """预置 person 表"""
        return pd.DataFrame(
            {
                "personId": [1, 2],
                "firstName": ["Alice", "Bob"],
                "lastName": ["Smith", "Johnson"],
            }
        )

    @pytest.fixture(scope="class")
    def address(self) -> pd.DataFrame:
        """预置 address 表（含一条无用记录）"""
        return pd.DataFrame(
            {
                "addressId": [101, 102, 103],
                "personId": [1, 999, 2],   # 999 是孤儿
                "city": ["New York", "Ghost", "Los Angeles"],
                "state": ["NY", "GH", "CA"],
            }
        )

    def test_combine_normal(self, person, address):
        """正常 left join：Alice 有地址，Bob 也有地址"""
        result = combine_two_tables(person, address)

        expected = pd.DataFrame(
            {
                "firstName": ["Alice", "Bob"],
                "lastName": ["Smith", "Johnson"],
                "city": ["New York", "Los Angeles"],
                "state": ["NY", "CA"],
            }
        )
        pd.testing.assert_frame_equal(result, expected)

    def test_combine_missing_address(self, person, address):
        """人为构造缺失地址的场景"""
        # 把 Bob 的地址删掉
        address_missing = address[address.personId != 2]
        result = combine_two_tables(person, address_missing)

        expected = pd.DataFrame(
            {
                "firstName": ["Alice", "Bob"],
                "lastName": ["Smith", "Johnson"],
                "city": ["New York", None],
                "state": ["NY", None],
            }
        )
        pd.testing.assert_frame_equal(result, expected)