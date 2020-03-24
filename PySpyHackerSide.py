from os import system
import sqlite3

def banner():
    print("____________________________________________________\n\nError 404 are proud to present PySpy!\n")
    print("                         %\n                      %%%%%%#\n                   (%%%%  ,%%%%.\n                 %%%%%%%%%%%%%%%%% ")
    print("              %%%%%%%%&*   /%%%%%%%%,\n           .%%%%%                .%%%%%\n         %%%%%    ,%%%%%%%%%%%%      %%%%(")
    print("      ,%%%%,   .%%%%%       .%%%%%/    (%%%%\n    %%%%%    %%%%%     %%       #%%%%     %%%%%\n /%%%%.%%%%%%%%.     %%%*          %%%%#    *%%%%.")
    print(",%%%%    *%%%%.     *%%%%%(,/%      %%%%%%.  *%%%%\n   %%%%%    %%%%&     %%%%%%%    #%%%%  %%%%%%%%\n     ,%%%%.   .%%%%%          .%%%%/    (%%%%")
    print("        %%%%%    .%%%%%%%%%%%%%%%     %%%%(\n          .%%%%%       *(((*       %%%%%\n             #%%%%%%          .%%%%%%*\n                %%%%%%%%%%%%%%%%%%%")
    print("                  (%%%%    ,%%%%.\n                     %%%%%%%%%\n                       /%%%.\n\nNetwork Enumeration Results\n____________________________________________________\n")

def menu():
    banner()
    print("PySpied with my little eye something begining with:")
    print("1. Most Resolved Domains")
    print("2. Overall Network Ports")
    print("3. Summary Info by IP")
    print("4. Update Database")
    print("5. Exit")
    option=input("Please choose an option: ")
    if option=="1": DNSrequests()
    elif option=="2":   ports()
    elif option=="3":   displayAllInfo()
    elif option=="4":   fetchDB()
    elif option=="5":   exit("Goodbye")
    else:
        print("Invalid Option - Try Again!")

def checkExsistance():
    """Check's if info.sqlite3 has been previously downloaded"""
    try:
        with open("info.sqlite3"):
            print("Found database in folder")
        update=input("Would you like to update it? [Y/N] ")
        if update=="y" or update=="Y":
            if not fetchDB():
                print("Unable to update using old file!")
    except IOError:
        print("Database not found...\nAttempting to fetch from server...")
        if not fetchDB():
            exit("Cannot reach database :(\nTry downloading manually")

def fetchDB():
    """Retrieves database from Azure Server via HTTPS, returns true if successfull"""
    getDB=system("curl https://error404coventry.hopto.org/info.sqlite3 --output info.sqlite3")
    print(getDB)
    if getDB==0:
        print("Successfully Retrieved Database")
        return True
    print("Unable to retrieve Database")
    return False

def fetchAllIPs():
    "Returns IP from Database"
    cursor.execute("SELECT IP FROM ARP UNION SELECT DISTINCT IP FROM DNS UNION SELECT DISTINCT IP_Source FROM HTTP WHERE IP_Source NOT NULL UNION SELECT DISTINCT IP FROM portScan;")
    allTargets=cursor.fetchall()
    print("Discovered IPs:")
    for each in allTargets:
        print(" - ",each[0])
    ip=input("Enter an IP for more information: ")
    for each in allTargets:
        if ip==each[0]:
            return ip
    print("Couldn't find that IP - try again!\n")
    return fetchAllIPs()

def fetchARP(ip):
    sql=str('SELECT MAC, Vendor, LastSeen FROM ARP WHERE IP ="{}"'.format(ip))
    cursor.execute(sql)
    arpInfo=cursor.fetchone()
    return arpInfo

def fetchDNS(ip):
    sql=('SELECT queryName,COUNT( * ) FROM DNS WHERE IP = "{}" AND Type = "request" GROUP BY queryName ORDER BY COUNT( * ) DESC;'.format(ip))
    cursor.execute(sql)
    dnsInfo=cursor.fetchall()
    return dnsInfo

def fetchHTTPpost(ip):
    sql=('SELECT fullURL,data FROM HTTP WHERE requestType LIKE "POST%" AND IP_Source="{}";'.format(ip))
    cursor.execute(sql)
    postInfo=cursor.fetchall()
    return postInfo

def fetchAgent(ip):
    sql=('SELECT userAgent FROM HTTP WHERE IP_Source="{}"'.format(ip))
    cursor.execute(sql)
    userAgent=cursor.fetchone()
    return userAgent

def openPorts(ip):
    sql=('SELECT DISTINCT Port FROM portScan where IP = "{}" ORDER BY Port ASC'.format(ip))
    cursor.execute(sql)
    openPorts=cursor.fetchall()
    allPorts="  "
    for port in openPorts:
        if port[0]==None:
            allPorts+=str("Ping, ")
        else:
            allPorts+=str(str(port[0])+", ")
    print(allPorts[:-2])

def displayAllInfo():
    ip=fetchAllIPs()

    arpInfo=fetchARP(ip)
    dnsInfo=fetchDNS(ip)
    postInfo=fetchHTTPpost(ip)
    userAgent=fetchAgent(ip)

    if arpInfo==None:   
        arpInfo=("No Data","No Data","No Data")
    if userAgent==None:
        userAgent="No Data"


    print("\nInformation for IP:",ip)
    print("MAC Address:",arpInfo[0])
    print("Device Creator:",arpInfo[1])
    print("User Agent:",userAgent[0])
    print("Information correct at:",arpInfo[2])

    print("\nDNS Requests Made (Domain | Times Visited):")
    for each in dnsInfo:
        print(each[0],each[1])
    
    print("\nHTTP Post Requests")
    for each in postInfo:
        print("URL: ",each[0])
        print("Data Sent:")
        print(each[1])

    print("\nOpen Ports:")
    openPorts(ip)

banner()
checkExsistance()
from graphs import *
with sqlite3.connect("info.sqlite3") as db: 
    cursor = db.cursor()

while(True):
    try:
        menu()
    except KeyboardInterrupt:
        menu()
        pass
