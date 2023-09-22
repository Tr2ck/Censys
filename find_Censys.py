# -*- coding:UTF-8 -*-

#脚本主要作用，通过Censys api 查询域名相应的证书  达到收集子域名作用
#
#
import sys
import json
import requests
import re
import time



API_URL = "https://www.censys.io/api/v1"
UID = ""
SECRET = ""
page = 1
PAGES = 1

domain = 'domain.com'

reload(sys)

sys.setdefaultencoding('utf8')


def getIp(page):
	global PAGES
	iplist = []
	data = {
		"query":domain,
		"page":page,
		"fields":["parsed.subject_dn"]
	}
	try:
		res = requests.post(API_URL + "/search/certificates", data=json.dumps(data),auth=(UID, SECRET))
	except:
		pass
	try:
		result = res.json()
		PAGES  = result['metadata']['pages']
		#print result
	except:
		pass
	for x in result["results"]:
		iplist.append(x["parsed.subject_dn"])
		#print x["parsed.subject_dn"]
	return iplist




if __name__ == '__main__':
	print 'start.......'
	with open(domain+'.txt','a') as f:
		while page <= PAGES:
			iplist = (getIp(page))
			page += 1
			time.sleep(1)
			#print iplist
			for i in iplist:
				f.write(i+'\n')
			#f.write(str(iplist)+'\n')
