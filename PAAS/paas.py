#!/usr/bin/python
import commands,cgitb,cgi,time,os 
cgitb.enable()

print "content-type:text/html"
print ""

data=cgi.FieldStorage()
s=data.getvalue('s')
ip=tuple(commands.getoutput('hostname -I').split(" ")[:-1])
if s == "python":
	a=commands.getoutput('sudo docker run -itd sat_python')
	b=commands.getoutput('sudo docker exec {} hostname -i'.format(a))
	print "<script>"
	print "alert('click here to Load')"
	print "</script>"
	print "<meta HTTP-EQUIV='refresh' content='0;url=https://{}:4200'>".format(b)
elif s == "mysql":
	a=commands.getoutput('sudo docker run -itd mariadb')
	b=commands.getoutput('sudo docker exec {} hostname -i'.format(a))
	print "<script>"
	print "alert('click here to Load')"
	print "</script>"
	print "<meta HTTP-EQUIV='refresh' content='0;url=https://{}:4200'>".format(b)
elif s == "r":
	print "<script>"
	print "alert('click here to Load')"
	print "</script>"
	print "<meta HTTP-EQUIV='refresh' content='0;url=https://{}:4201'>".format(ip[0])

else:
	print "<script>"
	print "alert('click here to Load')"
	print "</script>"
	print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/iframe.html'>".format(ip[0])
	
