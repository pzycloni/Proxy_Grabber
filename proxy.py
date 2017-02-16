import re
import requests
from connector import Connection

class Proxy:

	def __init__(self, urls):
		self.urls = urls


	def __connection(self, url, proxy = None):
		if proxy is not None:
			return Connection(url, proxy)
		return Connection(url)


	def __original(self, ips):
		return list(set(ips))


	def __parse(self, page):
		expression = '([0-9]{2,3}.[0-9]{2,3}.[0-9]{2,3}.[0-9]{2,3}:[0-9]{2,4})'
		ips = re.findall(expression, page)
		return self.__original(ips)


	def get(self, proxy = None):
		for url in self.urls:
			connection = self.__connection(url, proxy)
			if connection.is_alive():
				self.ips = self.__parse(connection.resource.text)
				self.count = len(self.ips)

				return {'count': self.count,'proxies': self.ips}

			return {'resourse': None, 'count': 0}


	def save(self, filename):
		with open(filename, 'w') as txt:	
			print('\n'.join([ip for ip in self.ips]), file=txt)

	def load(self, filename):
		self.ips = list()

		with open(filename, 'r') as txt:
			for line in txt:
				self.ips.append(line.rstrip())

		return self.ips


	def show(self):
		print('\n'.join([ip for ip in self.ips]))


if __name__ == '__main__':

	#	set urls
	url = ['http://proxyprivat.com/freeproxies']

	#	connection
	proxyprivat = Proxy(url)

	#	get json object
	answer = proxyprivat.get()

	#	set urls
	url = ['https://hide.me/ru/proxy']

	#	connection 
	hide = Proxy(url)
	
	#	pop one of proxies
	proxy = answer['proxies'].pop()

	# get json object
	answer = hide.get(proxy)
