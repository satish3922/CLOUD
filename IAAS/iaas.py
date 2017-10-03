#!/usr/bin/python
import cgi,commands,cgitb,time,random,os

cgitb.enable()
print "content-type:text/html"
print ""

data=cgi.FieldStorage()
os=data.getvalue('os')
ram=data.getvalue('ram')
cpu=data.getvalue('cpu')
vnc=random.randint(5900,58000)
web=random.randint(6080,58000)

b=tuple(commands.getoutput('hostname -I').split(' ')[:-1])

#off="sudo qrencode -s 16*16 -o {}_{}.png 'http://192.168.2.21:{}'".format(os,vnc,web)
#move="sudo mv /var/www/cgi-bin/None.png /var/www/html/QRCode"
#commands.getoutput(off)
#commands.getoutput(move)

vm="sudo virt-install --name {} --ram {} --vcpu {} --disk none --cdrom /var/lib/libvirt/images/{}.iso --graphics vnc,listen={},port={} --noautoconsole".format(os,ram,cpu,os,b[0],vnc)

web1="sudo websockify  --web=/usr/share/novnc {} {}:{} -D".format(web,b[0],vnc)
print commands.getoutput(vm)
print commands.getoutput(web1)

#print "<a href='/QRCode/{}_{}.png' target='_blank'>".format(os,vnc)

print "<meta HTTP-EQUIV='refresh' content='0; url=http://{}/novnc/vnc_auto.html?ip={}&port={}'/>".format(b[0],b[0],web)

