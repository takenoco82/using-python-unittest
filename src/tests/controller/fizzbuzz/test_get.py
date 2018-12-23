import unittest
from unittest.mock import patch
from parameterized import parameterized, param

from nose.plugins.attrib import attr

from server import controller


@attr(size='small')
class Test_get_fizzbuzz(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = '/v1/fizzbuzz/{n}'

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = controller.app.test_client()

    def tearDown(self):
        pass

    # patchは指定したモジュールパスが示すオブジェクトを差し替える
    # ここでは server/controller/fizzbuzz/get.py で import された fizzbuzz_list を差し替えたいので
    #   正: server.controller.fizzbuzz.get.fizzbuzz_list
    #   誤: server.logic.fizzbuzz.fizzbuzz_list
    @patch('server.controller.fizzbuzz.get.fizzbuzz_list', return_value=['1', '2'])
    def test_2xx(self, mock):
        # リクエスト
        url = self.url.format(n=3)
        response = self.app.get(url)

        # 検証
        self.assertEqual(response.status_code, 200)
        response_body = response.get_json()
        self.assertEqual(mock.called, True)
        self.assertListEqual(response_body['fizzbuzz'], ['1', '2'])

    @parameterized.expand([
        param(
            "value_error",
            input={
                'side_effect': ValueError('message ValueError')
            },
            expected={
                'status': 400,
                'body': {
                    'error': 'message ValueError'
                }
            }),
        param(
            "type_error",
            input={
                'side_effect': TypeError('message TypeError')
            },
            expected={
                'status': 400,
                'body': {
                    'error': 'message TypeError'
                }
            }),
    ])
    def test_4xx(self, _, input, expected):
        with patch('server.controller.fizzbuzz.get.fizzbuzz_list',
                   side_effect=input['side_effect']):
            # リクエスト
            url = self.url.format(n=3)  # mockを使うので引数は何でも良い
            response = self.app.get(url)

            # 検証
            self.assertEqual(response.status_code, expected['status'])
            response_body = response.get_json()
            self.assertDictEqual(response_body, expected['body'])


@attr(size='medium')
class Test_get_fizzbuzz_medium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = controller.app.test_client()
        cls.url = '/v1/fizzbuzz/{n}'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_2xx(self):
        # リクエスト
        url = self.url.format(n=3)
        response = self.app.get(url)

        # 検証
        self.assertEqual(response.status_code, 200)
        response_body = response.get_json()
        self.assertListEqual(response_body['fizzbuzz'], ['1', '2', 'Fizz'])

    def test_4xx(self):
        # リクエスト
        url = self.url.format(n=0)
        response = self.app.get(url)

        # 検証
        self.assertEqual(response.status_code, 400)
        response_body = response.get_json()
        self.assertEqual(response_body['error'], '`0` is invalid value. must be larger than `0`.')
