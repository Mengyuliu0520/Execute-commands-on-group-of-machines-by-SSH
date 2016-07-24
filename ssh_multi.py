import paramiko
import sys
import threading


def ssh2(ip,username,passwd,cmd):
	"[int, str, str, str]"
	"This function was used to connect to the target ip and
	 execute the commands in the list cmd one by one"
	try: 
		ssh = paramiko.SSHClient() 
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
		ssh.connect(ip,22,username,passwd,timeout=5)
		for m in cmd: 
			stdin,stdout,stderr = ssh.exec_command(m)
			stdin.write("Y")
			# print out the contents in stdout and stderr
        		for std in stdout.readlines():
      				print std
			for stde in stderr.readlines():
  				print stde
		ssh.close()
	# make an exception and print the info of it
	except :
		info=sys.exc_info()  
    		print info[0],":",info[1]
		print '%s\tError\n'%(ip)
# There are some cmd list for default, you can uncomment it as you want		      
# cmd = ['sudo apt-get install vim -y','sudo apt-get install openjdk-7-jre openjdk-7-jdk -y']
# cmd = ['sudo tar -zxf ~/hadoop.master.tar.gz -C /usr/local','sudo chown -R hadoop /usr/local/hadoop']
cmd = ['sudo -k poweroff']
# since I have a group of machines with continued IP address
# I need a loop to execute commands on each machine
for k in range(121,136):
	# you can initialize your own username and passwd here
	# username = "hadoop"
	# passwd = "hadoop"
	threads = [1, 2, 3, 4] 
	# this print just for notation
	print "Begin......"
	ip = '172.16.36.'+str(k)
	# use an multiple threads here(default 4)
	a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd)) 
	a.start() 
