import requests

def consulta():
	response = requests.get('http://127.0.0.1/pessoa/')
	print(response.status_code)
	print(response.json())
	for pessoa in response.json():
		print(pessoa['id'], pessoa['nome'], pessoa['idade'])

def insere():
	nome = 'Rafael'
	idade = 31
	pessoa = {"nome": nome, "idade": idade}
	response = requests.post('http://127.0.0.1/pessoa/', json=pessoa)
	print(response.status_code)
	print(response.json())

consulta()
#insere()