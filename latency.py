import subprocess
import re

amazon_regions = {'North Virginia(us-east-1)':'23.23.255.255','Ohio(us-east-2)       ':'52.14.64.0','North California(us-west-1)':'50.18.56.1',
'Oregon(us-west-2)       ':'35.160.63.253','GovCloud(us-gov-west-1)':'52.222.9.163','Canada(ca-central-1)       ':'52.60.50.0',
'Ireland(eu-west-1)       ':'34.248.60.213','Frankfurt(eu-central-1)      ':'35.156.63.252','London(eu-west-2)       ':'52.56.34.0',
'Tokyo(ap-northeast-1)       ':'13.112.63.251','Seoul(ap-northeast-2)       ':'52.78.63.252','Singapore(ap-southeast-1)':'46.51.216.14',
'Sydney(ap-southeast-2)':'13.54.63.252','Mumbai(ap-south-1)       ':'35.154.63.252','Sao Paulo(sa-east-1)       ':'52.67.255.254'}
latency_amazon_regions = {}
for key,value in amazon_regions.items():
	"""print (key, 'corresponds to', amazon_regions[key])"""
	ping = subprocess.Popen(["ping", "-n", "3", amazon_regions[key]], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	out, error = ping.communicate()
	"""print (str(out))"""
	latency = re.search(r'Average = ([0-9]+)ms',str(out))
	avg = latency.group(1)
	latency_amazon_regions[int(avg)] = key

"""print(error)"""
print ('\t'+'Latency(ms)'+'\t'+' Region'+'\t\t\t\t\t'+' IP used')
for time in sorted(latency_amazon_regions):
	print('\t',time,'\t\t',latency_amazon_regions[time],'\t\t',amazon_regions[latency_amazon_regions[time]])
