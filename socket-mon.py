#!/usr/bin/env python

import psutil
from operator import itemgetter
from itertools import groupby
import collections

def main():
	
	print ("PID", "Program name", "laddr", "raddr", "Status")
	process_names = {}
	rows=[]
	pids = []
	
	for proc in psutil.process_iter():
		try:
			process_names[proc.pid] = proc.name()
		except psutil.Error:
			pass
			
	for connection in psutil.net_connections(kind='inet'):
		laddr = "%s:%s" % (connection.laddr)
		raddr = ""
        
		if connection.raddr and connection.pid:
			pids.append(connection.pid)
			raddr = "%s:%s" % (connection.raddr)
			row = [connection.pid, process_names[connection.pid], laddr, raddr, connection.status]
			rows.append(row)
			sorted_rows = sorted(rows, key=itemgetter(0))

	c=collections.Counter(pids)
	
	sorted_pid = sorted(c.items(),key=itemgetter(1),reverse=True)
	
	for pid in sorted_pid:
		for row in sorted_rows:
			if pid[0] == row[0]:
				print (row[0], row[1], row[2], row[3], row[4])
	
if __name__ == '__main__':
	main()
