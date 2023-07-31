import unittest
import subprocess
import requests
import time

from config import port


class WebAppManagementTests(unittest.TestCase):

    url = f'http://localhost:{port}/api/addition'

    def test_start_server(self):
        result = subprocess.run(['webcalculator.exe', 'start', '127.0.0.1', '8000'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось запустить сервер")

        time.sleep(2)

        result = subprocess.run(['webcalculator.exe', 'start', '127.0.0.1', '8000'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось запустить сервер")

        time.sleep(2)

        payload = {"x": 1, "y": 1}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 2, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        result_stop = subprocess.run(['webcalculator.exe', 'stop'], capture_output=True, text=True)
        self.assertEqual(result_stop.returncode, 0, "Не удалось остановить сервер")

    def test_stop_server(self):
        result = subprocess.run(['webcalculator.exe', 'stop'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось остановить сервер")

        result = subprocess.run(['webcalculator.exe', 'stop'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось остановить сервер")

        try:
            response = requests.post(self.url, json={"x": 1, "y": 1})
            self.fail("Запрос был выполнен успешно, хотя сервер должен был быть остановлен")
        except requests.exceptions.ConnectionError as e:
            pass

    def test_restart_server(self):
        result = subprocess.run(['webcalculator.exe', 'start', '127.0.0.1', '8000'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось запустить сервер")
        time.sleep(3)

        result = subprocess.run(['webcalculator.exe', 'restart'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось перезапустить сервер")

        time.sleep(3)

        payload = {"x": 1, "y": 1}
        response = requests.post(self.url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 2, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        result_stop = subprocess.run(['webcalculator.exe', 'stop'], capture_output=True, text=True)
        self.assertEqual(result_stop.returncode, 0, "Не удалось остановить сервер")

    def test_show_logs(self):
        result = subprocess.run(['webcalculator.exe', 'start', '127.0.0.1', '8000'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось запустить сервер")

        result = subprocess.run(['webcalculator.exe', 'show_log'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось отобразить логи сервера")

        result_stop = subprocess.run(['webcalculator.exe', 'stop'], capture_output=True, text=True)
        self.assertEqual(result_stop.returncode, 0, "Не удалось остановить сервер")

        result = subprocess.run(['webcalculator.exe', 'show_log'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось отобразить логи сервера")

    def test_help(self):
        result = subprocess.run(['webcalculator.exe', 'start', '127.0.0.1', '8000'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось запустить сервер")

        result = subprocess.run(['webcalculator.exe', '-h'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось получить ответ")

        result = subprocess.run(['webcalculator.exe', '--help'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось получить ответ")

        result_stop = subprocess.run(['webcalculator.exe', 'stop'], capture_output=True, text=True)
        self.assertEqual(result_stop.returncode, 0, "Не удалось остановить сервер")

        result = subprocess.run(['webcalculator.exe', '--help'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось получить ответ")

        result = subprocess.run(['webcalculator.exe', '-h'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось получить ответ")

    def test_change_port(self):
        result = subprocess.run(['webcalculator.exe', 'stop'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось остановить сервер")

        result = subprocess.run(['webcalculator.exe', 'start', '127.0.0.2', '8001'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось запустить сервер")

        time.sleep(2)

        new_url = f'http://127.0.0.2:8001/api/addition'

        payload = {"x": 1, "y": 1}
        response = requests.post(new_url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 2, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

    def test_fail_start(self):
        result = subprocess.run(['webcalculator.exe', 'stop'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось остановить сервер")

        try:
            result = subprocess.run(['webcalculator.exe', 'start', '0', '0'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 4294967295, "Сервер запустился, хотя не должен")
        except subprocess.CalledProcessError as e:
            self.assertEqual(e.returncode, 2, "Сервер выдал ошибку")

        try:
            result = subprocess.run(['webcalculator.exe', 'start', '127.9'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 4294967295, "Сервер запустился, хотя не должен")
        except subprocess.CalledProcessError as e:
            self.assertEqual(e.returncode, 2, "Сервер выдал ошибку")

    def test_default_value_port(self):
        result = subprocess.run(['webcalculator.exe', 'stop'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось остановить сервер")

        result = subprocess.run(['webcalculator.exe', 'start', '127.0.0.2'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось запустить сервер")

        time.sleep(2)

        new_url = f'http://127.0.0.2:17678/api/addition'

        payload = {"x": 1, "y": 1}
        response = requests.post(new_url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 2, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        result = subprocess.run(['webcalculator.exe', 'stop'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось остановить сервер")

    def test_default_value_localhost_port(self):
        result = subprocess.run(['webcalculator.exe', 'stop'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось остановить сервер")

        result = subprocess.run(['webcalculator.exe', 'start'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось запустить сервер")

        time.sleep(2)

        new_url = f'http://localhost:17678/api/addition'

        payload = {"x": 1, "y": 1}
        response = requests.post(new_url, json=payload)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        response_data = response.json()
        self.assertTrue("statusCode" in response_data, "Отсутствует ключ 'statusCode' в ответе")
        self.assertTrue("result" in response_data, "Отсутствует ключ 'result' в ответе")
        result = response_data["result"]
        self.assertEqual(result, 2, "Некорректный результат сложения")
        self.assertEqual(response_data["statusCode"], 0, "Неверный код ошибки")

        result = subprocess.run(['webcalculator.exe', 'stop'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Не удалось остановить сервер")
