import requests

def _post(cmd: str) -> bool:
	url = 'http://host1.dreamhack.games:16167/'
	params = {
		'cmd':cmd
	}
	response = requests.post(url,data=params)
	return response

if __name__ == "__main__":

	pay = 'ls'
	res = _post(pay)
	print(res)

