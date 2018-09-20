# import requests
# import urllib.request

# s = requests.Session()
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	
# urllib.request.urlretrieve("http://szcdn1.raagalahari.com/feb2018/posters/priya-augustin-blue-saree/priya-augustin-blue-saree74.jpg", "local-filename.jpg")

from io import BytesIO
import os
import shutil
import requests
import re
from threading import Thread
from time import sleep

def download(url):
	s = requests.Session()
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	r = s.get(url, headers=headers)
	return r




def threaded_function(url, folder, upper):
	print(url)
	print(folder)
	print(upper)

	if not os.path.exists(folder):
	    os.makedirs(folder)
	for i in range(1, upper+1):
		data = download(url+str(i)+'.jpg')
		with open('./'+folder+'/'+folder+'-'+str(i) + '.jpg', 'wb') as out_file:
			shutil.copyfileobj(BytesIO(data.content), out_file)
		print("["+folder+"] : "+str(i) +"/"+ str(upper)+" Image Downloaded")
	print("["+folder+"] : All Completed")



if __name__ == "__main__":
    thread1 = Thread(target = threaded_function, args = ("http://starzone.raagalahari.com/jan2016/photosessions/monica-thompson-actress-hot-stills-ragalahari/monica-thompson-actress-hot-stills-ragalahari", "monica-thompson-actress-hot-stills", 128))
    thread2 = Thread(target = threaded_function, args = ("http://szcdn1.raagalahari.com/jan2018/photosessions/rachana-smith-langa-voni/rachana-smith-langa-voni", "rachana-smith-langa-voni", 200))
    thread3 = Thread(target = threaded_function, args = ("http://szcdn1.raagalahari.com/mar2016/photosessions/actress-neelam-bhanushali/actress-neelam-bhanushali", "actress-neelam-bhanushali", 196))
    thread4 = Thread(target = threaded_function, args = ("http://szcdn1.raagalahari.com/oct2016/starzone/ashwini-kotikokkadu-audio/ashwini-kotikokkadu-audio", "ashwini-kotikokkadu-audio", 69))
    thread5 = Thread(target = threaded_function, args = ("http://szcdn1.raagalahari.com/oct2016/starzone/ash-wini/ash-wini", "ash-wini", 1005))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()


    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    print ("thread finished...exiting")