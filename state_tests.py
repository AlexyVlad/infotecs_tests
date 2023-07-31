import unittest
import requests
from config import port
from start_server import start_server


class WebServerStateTests(unittest.TestCase):
    url = f'http://localhost:{port}/api/state'

    def test_server_state(self):
        start_server() #Тут запускается сервер для дальнейшего тестирования
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200, "Неверный код ответа сервера")
        self.assertTrue("state" in response.json(), "Отсутствует ключ 'state' в ответе")
        state_value = response.json()["state"]

        # Проверяем кодировку ответа 'OK'
        if 'OK' in state_value:
            self.assertEqual(response.encoding, 'utf-8', "Неверная кодировка ответа")
        else:
            self.assertEqual(response.encoding, 'cp1251', "Неверная кодировка ответа")
        self.assertEqual(state_value, "ОК", "Некорректное состояние сервера")

