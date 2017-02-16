import requests

class Connection:

	def __init__(self, url, proxy = None):
		self.resource = self.__install(url, proxy)

		if not self.is_alive():
			self.resource = None


	def __install(self, url, proxy):
		try:
			resource = requests.get(url) if proxy is None else requests.get(url, proxies=proxy)
		except:
			resource = None
		finally:
			return resource



	def is_alive(self):
		if self.resource is not None:
			if self.resource.status_code == requests.codes.ok:
				return True
		
		return False
