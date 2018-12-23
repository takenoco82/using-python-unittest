import unittest

from nose.plugins.attrib import attr

from server import controller


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
