import requests
def request(uid,upw):
	url = f'http://suninatas.com/challenge/web22/web22.asp?id={uid}&pw={upw}'
	response = requests.get(url)
	return response


for i in range(33,128):
	uid = chr(i)
	upw = '1'
	response = request(uid,upw)
	if 'False' in response.text:
		#print(upw,response.text)
		print(chr(i),end=' / ')

print('\n')
