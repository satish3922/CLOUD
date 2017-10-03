#!/usr/bin/python
import os,commands,time,cgitb,cgi,random
cgitb.enable()

print "content-type:text/html"
print ""
a=random.randint(1,1000)
data=cgi.FieldStorage()
s=data.getvalue('s')
b=tuple(commands.getoutput('hostname -I').split(' ')[:-1])
os.chdir('/var/www/html')
path="{}{}.sh".format(s,a)
create='sudo touch {}'.format(path)
commands.getoutput(create)
commands.getoutput('sudo chmod 777 {}{}.sh'.format(s,a))
name="{}{}.sh".format(s,a)
f=open(name,'a')
f.write("#!/usr/bin/bash\n")
f.write("sudo ssh -Y saas@{} {}\n".format(b[0],s))
f.close()
tar="sudo tar -cf {}{}.tar {}".format(s,a,path)
commands.getoutput(tar)
commands.getoutput('sudo rm -rf {}'.format(path))
print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/{}{}.tar' target='_self'/>".format(b[0],s,a)
