import os
import urllib.request

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

# Create directory to store downloaded data
os.makedirs("data", exist_ok=True)
# add URL array to download.
urls = ['102711', '106360', '106494']

def downloader(url):
	try:
		response = urllib.request.urlopen("baseUrl" + url)
    # naming downloaded files.
		f = open("data/"+url+".json","w+")
		string = response.read().decode('utf-8')
		f.write(string)
		f.close()
		msg = "Downloaded: " + url
	except:
    # Failed url stored in a string
		f = open("faild.txt","a")
		string = url
		f.write(string+'\n')
		f.close()
		msg = "Faild: " + url
	return msg

def main(urls, counter):
	"""
	Create a thread pool and download specified urls,
	max_workers = number of concurrent connections, change accordingly.
	"""
	with ThreadPoolExecutor(max_workers=10) as executor:
		futures = [executor.submit(downloader, url) for url in urls]
		for future in as_completed(futures):
			counter += 1
			print(future.result() + " || counter = " + str(counter))

if __name__ == '__main__':
	counter = 0
	main(urls, counter)
