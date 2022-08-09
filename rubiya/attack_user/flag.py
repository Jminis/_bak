import requests
import re

def my_request(flag):
	url = f"http://b.rubiya.kr/auth.php?flag={flag}"
	cookie = {"PHPSESSID":"16fdkdng2fugnhdppfi509in92"}
	response = requests.get(url,cookies=cookie)
	return response

def submit():
	with open("result","r") as fp:
		data = fp.read()
		for flag in re.finditer("FLAG",data):
			response = my_request(data[flag.start():flag.start()+38])
			print(response.text)

		fp.close()

if __name__ == "__main__":
	submit()

