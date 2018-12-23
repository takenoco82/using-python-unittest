import unittest
from unittest.mock import patch, call

from nose.plugins.attrib import attr
from parameterized import param, parameterized

from server.logic import fizzbuzz


@attr(size='small')
class TestFizzBuzz(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand(
        [
            param("value_1", input=1, expected="1"),
            param("value_2", input=2, expected="2"),
            param("value_3", input=3, expected="Fizz"),
            param("value_4", input=4, expected="4"),
            param("value_5", input=5, expected="Buzz"),
            param("value_6", input=6, expected="Fizz"),
            param("value_10", input=10, expected="Buzz"),
            param("value_15", input=15, expected="FizzBuzz"),
            param("value_30", input=30, expected="FizzBuzz"),
        ]
    )
    def test_fizzbuzz_normal(self, _, input, expected):
        actual = fizzbuzz.fizzbuzz(input)
        self.assertEqual(actual, expected)

    # 固定値でいいなら return_value を使う。ここでは 常に '1' を返す
    @patch('server.logic.fizzbuzz.fizzbuzz', return_value='1')
    # mockを使う場合、テストメソッドに引数を追加する
    # unittest.mock.patch デコレータを使うと、そのメソッド内だけ置き換えることができる
    def test_mock_patch_return_value(self, mock):
        actual = list(fizzbuzz.fizzbuzz_gen(3))
        # ホントは ['1', '2', 'Fizz'] だけど、常に'1'を返すようになっているので ['1', '1', '1']
        self.assertListEqual(actual, ['1', '1', '1'])

    # side_effect にリストを指定すると呼ばれた順に応じて値を変えることができる
    @patch('server.logic.fizzbuzz.fizzbuzz', side_effect=['1', '2', '3'])
    def test_mock_patch_side_effect(self, mock):
        actual = list(fizzbuzz.fizzbuzz_gen(3))
        self.assertListEqual(actual, ['1', '2', '3'])

    # called を使うと呼ばれたかどうか、 call_count を使うと呼ばれた回数がわかる
    @patch('server.logic.fizzbuzz.fizzbuzz', return_value='1')
    def test_mock_call_count(self, mock):
        list(fizzbuzz.fizzbuzz_gen(3))
        self.assertEqual(mock.called, True)
        self.assertEqual(mock.call_count, 3)

    # assert_has_calls を使うと読んだ回数と引数を検証できる
    @patch('server.logic.fizzbuzz.fizzbuzz', return_value='1')
    def test_fizzbuzz_gen_patch(self, mock):
        list(fizzbuzz.fizzbuzz_gen(3))
        # call_args_list で設定した引数がわかる
        print('mock.call_args_list={}'.format(mock.call_args_list))
        # 検証したい引数を unittest.mock.call の引数に設定する
        # ここでは fizzbuzz.fizzbuzz() を3回呼び出して、それぞれ 1, 2, 3 の引数を渡している
        mock.assert_has_calls([call(1), call(2), call(3)])

    @parameterized.expand([
        param(
            "value_1",
            input=1,
            expected=['1']),
        param(
            "value_15",
            input=15,
            expected=[
                '1', '2', 'Fizz', '4', 'Buzz',
                'Fizz', '7', '8', 'Fizz', 'Buzz',
                '11', 'Fizz', '13', '14', 'FizzBuzz']),
    ])
    def test_fizzbuzz_gen_normal(self, _, input, expected):
        actual = list(fizzbuzz.fizzbuzz_gen(input))
        self.assertListEqual(actual, expected)

    @parameterized.expand([
        param(
            "value_0",
            input=0,
            expected={
                'exception': ValueError,
                'message': "`0` is invalid value. must be larger than `0`."
            }),
        param(
            "value_minus",
            input=-1,
            expected={
                'exception': ValueError,
                'message': "`-1` is invalid value. must be larger than `0`."
            }),
        param(
            "value_none",
            input=None,
            expected={
                'exception': TypeError,
                'message': "`None` is invalid value. must be type `int`."
            }),
        param(
            "type_string",
            input='aha',
            expected={
                'exception': TypeError,
                'message': "`aha` is invalid value. must be type `int`."
            }),
        param(
            "type_float",
            input=1.3,
            expected={
                'exception': TypeError,
                'message': "`1.3` is invalid value. must be type `int`."
            }),
        param(
            "type_list",
            input=[1, 2],
            expected={
                'exception': TypeError,
                'message': "`[1, 2]` is invalid value. must be type `int`."
            }),
    ])
    def test_fizzbuzz_gen_exception(self, _, input, expected):
        try:
            list(fizzbuzz.fizzbuzz_gen(input))
            self.fail('NG')
        except Exception as e:
            self.assertEqual(type(e), expected['exception'])
            self.assertEqual(e.args[0], expected['message'])

    @parameterized.expand([
        param(
            "value_15",
            input=15,
            expected=[
                '1', '2', 'Fizz', '4', 'Buzz',
                'Fizz', '7', '8', 'Fizz', 'Buzz',
                '11', 'Fizz', '13', '14', 'FizzBuzz']),
    ])
    def test_fizzbuzz_list(self, _, input, expected):
        actual = fizzbuzz.fizzbuzz_list(input)
        self.assertListEqual(actual, expected)
