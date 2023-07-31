import unittest
import requests
from config import port


class WebCalculatorMultiplicationTests(unittest.TestCase):
    url = f'http://localhost:{port}/api/multiplication'

    def test_positive_numbers(self):
        payload = {"x": 5, "y": 5}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 25, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 1234567, "y": 98765}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 121932009755, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 2147483647, "y": 1}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 2147483647, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 100000, "y": 100000}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 10000000000, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

    def test_negative_numbers(self):
        payload = {"x": -5, "y": 5}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, -25, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": -2147483648, "y": 1}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, -2147483648, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 5, "y": -2147483648}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, -10737418240, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 2147483647, "y": -2147483648}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, -4611686016279904256, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 5, "y": -1}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, -5, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": -5, "y": -1}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 5, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

    def test_zero_number(self):
        payload = {"x": 25, "y": 0}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 0, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 0, "y": 5000}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 0, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 0, "y": 0}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 0, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 0, "y": -2147483648}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 0, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 0, "y": 2147483647}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 0, "Некорректный результат умножения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

    def test_missing_keys_in_request_body(self):
        payload = {"x": 10}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertEqual(response_data["statusCode"], 2, "Неверный код ошибки")
        self.assertTrue("statusMessage" in response_data, "Отсутствует ключ 'statusMessage' в ответе")

    def test_non_integer_value_in_request(self):
        payload = {"x": 10, "y": 5.1}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertEqual(response_data["statusCode"], 3, "Неверный код ошибки")
        self.assertTrue("statusMessage" in response_data, "Отсутствует ключ 'statusMessage' в ответе")

    def test_value_exceeds_limit(self):
        payload = {"x": 2147483649, "y": 5}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertEqual(response_data["statusCode"], 4, "Неверный код ошибки")
        self.assertTrue("statusMessage" in response_data, "Отсутствует ключ 'statusMessage' в ответе")

    def test_invalid_json_format(self):
        payload = "invalid_format"
        response = requests.post(self.url, data=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertEqual(response_data["statusCode"], 5, "Неверный код ошибки")
        self.assertTrue("statusMessage" in response_data, "Отсутствует ключ 'statusMessage' в ответе")

        payload = {"a": 10, "b": 5}
        response = requests.post(self.url, data=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertEqual(response_data["statusCode"], 5, "Неверный код ошибки")
        self.assertTrue("statusMessage" in response_data, "Отсутствует ключ 'statusMessage' в ответе")

        payload = {"x": 'f1', "y": 'ff'}
        response = requests.post(self.url, data=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertEqual(response_data["statusCode"], 5, "Неверный код ошибки")
        self.assertTrue("statusMessage" in response_data, "Отсутствует ключ 'statusMessage' в ответе")
