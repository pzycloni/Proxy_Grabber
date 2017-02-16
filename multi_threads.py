from proxy import Proxy
from connector import Connection
import threading
import requests

class GrabberImg:
	def __init__(self, proxies, url):
		self.proxies = proxies
		self.url = url


	def run(self):
		for ip in self.proxies:
			request = Connection(self.url, ip)
			if request.status_code == requests.codes.ok:
				print(ip, 'ok')
			else: print(ip, 'failed')

url_pic_1 = 'https://www.goodfon.ru/download/manarola-italiya-liguriyskoe-1552/1366x768/'
url_pic_2 = 'https://www.goodfon.ru/download/ghost-in-the-shell-paramount/1366x768/'
url = ['http://proxyprivat.com/freeproxies']

proxy = Proxy(url)
proxies = proxy.get()
proxy.save('proxies.txt')
proxies = proxy.load('proxies.txt')
print(proxies)


#thirst = GrabberImg(proxies, url_pic_1)
#second = GrabberImg(proxies, url_pic_2)

#t1 = threading.Thread(target=thirst.run)
#t2 = threading.Thread(target=second.run)

#t1.start()
#t2.start()
