'''
Created on Jun 2, 2015

@author: qiulei
'''

import urllib.request

x = urllib.request.urlopen('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=5000&key=AIzaSyBxODBMe80kjYwRjNUTY6FymkJ7eHFhWs8')
print(x.read().decode('utf-8'))