import sqlite3
import matplotlib.pyplot as plot
import numpy as np

with sqlite3.connect("info.sqlite3") as db: 
    cursor = db.cursor()

def ports():
    cursor.execute('SELECT DISTINCT IP, Port FROM portScan ORDER BY IP, Port ASC;')
    openPorts=cursor.fetchall()
    
    height=[]
    bars=[]

    for port in openPorts:
        if port[1]==None:
            height.append(0)
        else:
            height.append(port[1])
        bars.append(port[0])
    plot.scatter(bars, height)
    plot.xlabel("IP Address")
    plot.ylabel("Open Ports")
    plot.title('Open Ports by IP')
    plot.show()

def DNSrequests(filterByIP=False):
    cursor.execute('SELECT queryName,COUNT( * ) FROM DNS WHERE Type = "request" GROUP BY queryName ORDER BY COUNT( * ) DESC;')
    DNSrequests=cursor.fetchall()
    height=[]
    bars=[]
    for request in DNSrequests:
        height.append(request[1])
        bars.append(request[0])
    plot.title("Graph Showing Domain Visits")
    y_pos=np.arange(len(bars))
    plot.bar(y_pos,height)
    plot.ylabel('Number of Requests', fontweight='bold',  fontsize='16')
    plot.xticks(y_pos,bars)
    plot.xlabel('Domains', fontweight='bold',  fontsize='16')
    plot.show()
    
