import subprocess

from config import port

url = f'http://localhost:{port}/api/addition'


def start_server():
    subprocess.run(['webcalculator.exe', 'stop'], capture_output=True, text=True)
    subprocess.run(['webcalculator.exe', 'start', '127.0.0.1', f'{port}'], capture_output=True, text=True)
