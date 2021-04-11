import requests
def send_data(dulieu):
	url = 'https://5802244b27db.ngrok.io'
	myobj = {'cau':dulieu}

	x = requests.post(url, data = myobj)

	print(x.text)
	return x.text