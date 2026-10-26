import http.client
import os
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    
    def assert_ok(self, path, expected):
        url = f"{BASE_URL}{path}"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la peticion API a {url}")
        self.assertEqual(response.read().decode(), expected, f"Resultado incorrecto en {url}")

    def assert_bad_request(self, path):
        url = f"{BASE_URL}{path}"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, f"Se esperaba 400 en {url}")

    
    def test_api_hello(self):
        self.assert_ok("/", "Hello from The Calculator!\n")

   
    def test_api_add(self):
        self.assert_ok("/calc/add/2/2", "4")
        self.assert_ok("/calc/add/-2/3", "1")
        self.assert_ok("/calc/add/1.5/2", "3.5")

    def test_api_add_bad_request(self):
        self.assert_bad_request("/calc/add/a/2")
        self.assert_bad_request("/calc/add/2/b")

    
    def test_api_substract(self):
        self.assert_ok("/calc/substract/5/2", "3")
        self.assert_ok("/calc/substract/2/5", "-3")

    def test_api_substract_bad_request(self):
        self.assert_bad_request("/calc/substract/a/2")

    
    def test_api_multiply(self):
        self.assert_ok("/calc/multiply/2/3", "6")
        self.assert_ok("/calc/multiply/-2/3", "-6")

    def test_api_multiply_bad_request(self):
        self.assert_bad_request("/calc/multiply/x/3")

    
    def test_api_divide(self):
        self.assert_ok("/calc/divide/6/2", "3.0")
        self.assert_ok("/calc/divide/3/2", "1.5")

    def test_api_divide_by_zero(self):
        self.assert_bad_request("/calc/divide/1/0")

    def test_api_divide_bad_request(self):
        self.assert_bad_request("/calc/divide/a/2")

    
    def test_api_power(self):
        self.assert_ok("/calc/power/2/3", "8")
        self.assert_ok("/calc/power/2/-1", "0.5")

    def test_api_power_bad_request(self):
        self.assert_bad_request("/calc/power/0/-1")
        self.assert_bad_request("/calc/power/a/2")

    
    def test_api_sqrt(self):
        self.assert_ok("/calc/sqrt/16", "4.0")
        self.assert_ok("/calc/sqrt/2.25", "1.5")

    def test_api_sqrt_bad_request(self):
        self.assert_bad_request("/calc/sqrt/-1")
        self.assert_bad_request("/calc/sqrt/abc")

    
    def test_api_log10(self):
        self.assert_ok("/calc/log10/100", "2.0")
        self.assert_ok("/calc/log10/1", "0.0")

    def test_api_log10_bad_request(self):
        self.assert_bad_request("/calc/log10/0")
        self.assert_bad_request("/calc/log10/-10")
        self.assert_bad_request("/calc/log10/abc")