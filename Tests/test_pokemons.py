import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '0f9d44e19d0bf4b9d7c60113c4237d45'

def test_status_code():
	response = requests.get(f'{host}/trainers', params = {'trainer_id': 3493 })
	assert response.status_code == 200, f'''status_code ответа метода get trainers не равен (!=) 200,
	  текст ошибки: {response.text}'''
	

def test_part_of_body():
	response = requests.get(f'{host}/trainers', params = {'trainer_id': 3493 })
	assert "trainer_name" in response.json(), f'''Ответ метода GET trainers не вернул поле  '''
	assert response.json()["trainer_name"] == 'Денис', f'''Метод вернул неверное имя тренера'''