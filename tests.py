import unittest
import requests

port = 8000


class WebCalculatorAdditionTests(unittest.TestCase):
    url = f'http://localhost:{port}/api/addition'

    def test_positive_numbers(self):
        payload = {"x": 10, "y": 5}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 15, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 12, "y": 0}
        response = requests.post(self.url, json=payload)
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 12, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 0, "y": 1}
        response = requests.post(self.url, json=payload)
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 1, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 10, "y": 10}
        response = requests.post(self.url, json=payload)
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 20, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 1000000, "y": 2000000}
        response = requests.post(self.url, json=payload)
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 3000000, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 2147483647, "y": 2}
        response = requests.post(self.url, json=payload)
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 2147483649, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

    def test_negative_numbers(self):
        payload = {"x": -5, "y": -10}
        response = requests.post(self.url, json=payload)
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, -15, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 0, "y": -5}
        response = requests.post(self.url, json=payload)
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, -5, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": -5, "y": 0}
        response = requests.post(self.url, json=payload)
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, -5, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": -2147483647, "y": -2}
        response = requests.post(self.url, json=payload)
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, -2147483649, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": -2147483648, "y": 2147483647}
        response = requests.post(self.url, json=payload)
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, -1, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": 100, "y": -50}
        response = requests.post(self.url, json=payload)
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 50, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        payload = {"x": -5, "y": 5}
        response = requests.post(self.url, json=payload)
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 0, "Некорректный результат сложения")
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


# Функция для сбора всех тестовых классов
def create_test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(WebCalculatorAdditionTests))
    test_suite.addTest(unittest.makeSuite(WebCalculatorMultiplicationTests))
    return test_suite


if __name__ == '__main__':
    # Создание объекта TestRunner и запуск тестов
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = create_test_suite()
    result = runner.run(test_suite)

    print("\n===== Результаты тестов =====")
    print(f"Всего тестов: {result.testsRun}")
    print(f"Успешных: {result.testsRun - len(result.errors) - len(result.failures)}")
    print(f"Неудачных: {len(result.errors) + len(result.failures)}")

    if result.wasSuccessful():
        print("Все тесты прошли успешно.")
    else:
        print("Тесты не были пройдены. Проверьте ошибки и неудачные тесты.")
