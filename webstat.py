#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urllib2
import json
PORT_NUMBER = 10087


def get():
    #replace ??? to your veid and api_key
    u = 'http://api.kiwivm.it7.net/v1/getServiceInfo?veid=???&api_key=???'
    try:
	response = urllib2.urlopen(u)  
	html = response.read()
	js = json.loads(html)
	x = js['data_counter']
	y = js['plan_monthly_data']
	p = x*1.0/ (1024*1024*1024)
	return '%f GB used, about %f %% percent'%(p,(x*100.0)/y)
    except:
	pass
    return 'Error. Please retry'

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(get())
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close
