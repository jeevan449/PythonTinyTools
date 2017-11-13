import subprocess


fromaddr='test@gmail.com'
toaddr='testing@gmail.com'
subject="Testing..."
body="hi there "

cmd= 'echo '+body+' | mail -s '+subject+' -r '+fromaddr+' '+toaddr
print cmd
send=subprocess.call(cmd,shell=True)
print send
