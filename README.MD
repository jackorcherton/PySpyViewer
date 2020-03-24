PySpy Viewer
-------------------------
This program is designed to be used on the hacker's machine to present the information that has been collected in a more usful format.
This program will run on Windows & Linux.

Main Features
-------------------------
1. Download database from the PySpy Server that you set up (this is done through HTTPS so all data is encrypted).
2. Saves the database to your current directory (By default it is in your main user area)
3. Allows you to produce graphs for:
	- All Open ports on the net - gives you an idea what ports are open 
	- Most popular DNS queries - potential sites that you can spoof
4. Results per IP, will display the following for each target:
	-IP Address
	-MAC Address
	-Device Creator - can use vendor specific exploits
	-User Agent - can give you information such as browser, browser version & operating system
	-Last time it was scanned
	-DNS Queries & Number of times it was searched (most popular at the top)
	-Ports Open - used to target specific services
	-HTTP Post - captures any data sent (sometimes can capture usernames & passwords)

NOTE
-------------------------
The program will currently only download a database from a demo website. To change this you need to open the code
and go to line 50, which reads: getDB=system("curl https://error404coventry.hopto.org/info.sqlite3 --output info.sqlite3")
You will need to change the 'https://error404coventry.hopto.org/' part to match your web domain or static IP

Dependancies
-------------------------
Python 3.8+ (should work with any interpreter in the 3.x branch)
Matplotlib (Type 'python3 -m pip install Matplotlib' - sometimes you need to remove the '3' - required for the database graph producer on the hacker's machine)
Server to download database (or a file named info.sqlite3 placed in the same directory as the code

Recomended Additional Software
-------------------------
On the hacker's machine we recommend that you get a SQLite 3 Database Viewer, so you are able to open/view the downloaded database.
We recommend SQLiteStudio - Linux, MAC & Windows Compatible - https://github.com/pawelsalawa/sqlitestudio/releases

Legal
-------------------------
PLEASE NOTE - this code is only for educational purposes - and does work on a network. Due to what these tools do, please do not run them on any network that you do not have permision too - we accept no liability.