
#!/usr/bin/env python

import psutil
from operator import itemgetter

def main():
	space = "  %-10s %-30s %-30s %-30s %s"
	print(space %("PID", "Program name", "Local address", "Remote address", "Status" ))
	process_names = {}
	rows= []
	
	for proc in psutil.process_iter():
		try:
			process_names[proc.pid] = proc.name()
		except psutil.Error:
			pass
			
	for connection in psutil.net_connections(kind='inet'):
		laddr = "%s:%s" % (connection.laddr)
		raddr = ""
        
		if connection.raddr:
			raddr = "%s:%s" % (connection.raddr)
			row = [connection.pid, process_names[connection.pid], laddr, raddr, connection.status]
			rows.append(row)
			sorted_rows = sorted(rows, key=itemgetter(0))
			
	for row in sorted_rows:
		print space %(row[0], row[1], row[2], row[3], row[4] )

if __name__ == '__main__':
    main()