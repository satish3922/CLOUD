#!/usr/bin/python
import commands,cgitb,cgi,os
cgitb.enable()
print "content-type:text/html"
print ""
data=cgi.FieldStorage()
dn=data.getvalue('dn')
ds=data.getvalue('ds')
a="Drive named {} is created of size {}M".format(dn,ds)
b=tuple(commands.getoutput('hostname -I').split(' ')[:-1])
commands.getoutput('sudo lvcreate --name {} --size {}M volgrp'.format(dn,ds))
commands.getoutput('sudo mkfs.xfs /dev/volgrp/{}'.format(dn))
commands.getoutput('sudo mkdir /mnt/{}'.format(dn))
commands.getoutput('sudo mount /dev/volgrp/{} /mnt/{}'.format(dn,dn))
nfs="/mnt/{} *(rw,no_root_squash)\n".format(dn)
f=open('/etc/exports','a')
f.write(nfs)
f.close()
commands.getoutput('sudo exportfs -r')


os.chdir('/var/www/html')
path="{}.sh".format(dn)
create='sudo touch {}'.format(path)
permission="mount {}:/mnt/{} /mnt/{}\n".format(b[0],dn,dn)
commands.getoutput(create)
commands.getoutput('sudo chmod 777 {}'.format(path))
f=open(path,'w')
f.write("#!/usr/bin/bash\n")
f.write("sudo mkdir -p /mnt/{}\n".format(dn))
f.write(permission)
f.close()
tar="sudo tar -cf {}.tar {}".format(dn,path)
commands.getoutput(tar)
print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/{}.tar'/>".format(b[0],dn)

