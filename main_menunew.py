import os
while(1):
	print("\t\t\tWelcome to the automation menu !!")
	print("\t\t\t---------------------------------")
	print(""" 
	\n
	press 1: to perform docker actions
	press 2: to perform hadoop actions
	press 3: to see your ip
	press 4: to exit
	""")
	selected= input ("enter your choice : " )
	if int(selected) == 1:
		print("\t\t\tWelcome to docker menu !!")
		print("\t\t\t-------------------------")
		print(""" 
		\n
		press 1: to start the docker
		press 2: to see the status of the docker 
		press 3: to permanently enable the docker 
		Press 4: to pull the image from dockerhub 
		Press 5: to list docker images 
		press 6: to see the process status of docker	
		press 7: to see the information about the docker 
		press 8: to stop the docker   
		""")
		ch= input ("enter your choice : " )
		if int(ch) == 1:
			os.system("systemctl start docker ")
		elif int(ch) == 2:
			os.system("systemctl status docker ")
		elif int(ch) == 3:
			os.system("systemctl enable docker ")
		elif int(ch) == 4:
			image = input("what image you want:")
			os.system("docker pull {} ".format(image))
		elif int(ch) == 5:
			os.system("docker images -a ")
		elif int(ch) == 6:
			os.system("docker ps ")
		elif int(ch) == 7:
			os.system("docker info ")
		elif int(ch) == 8:
			os.system("systemctl stop docker ")
		else:
			print("not supported")

	elif int(selected)==2:

		print("You can do following:")
		print("Press1: to install Oracle java")
		print("Press2: to install hadoop")
		print("Press3: to configure master on your system")
		print("Press4: to configure slave on your system")
		print("Press5: to format storage when your system is configured as master")
		print("Press6: format your storage when you are slavenode")
		print("Press7: to configure your system as client")
		print("Press8: to check who is connected to Master")
		print("Press9: show data present in cluster")
		print("Press10: Upload file in cluster")
		print("Press11: Upload file with given block size")
		print("Press12: Reads file present in Cluster") 
		print("Press13: Create file")
		print("Press14:  Create folder")
		print("Press15:  Remove folder")
		print("Press16:  Remove file")
		option = input("Do you have ssh installed in your system(Y/N)?")
		if option=='N':
			print("Not possible to do operations,please install ssh in your system using 'rpm -i openssh-7.8p1-4.el8.x86_64' and after then you can proceed further")
		else:
			choice=input("Enter your choice")
			if int(choice)==1:
				ip=int(input("Enter your system ip"))
				password=input("Enter password")
				os.system("echo {password}>ssh.txt")
				os.system("scp jdk-8u171-linux-x64.rpm {ip}:/")
				os.system("sshpass -f ssh.txt ssh root@{ip}")
				os.system("rpm -i jdk-8u171-linux-x64.rpm")
			elif int(choice)==2:

				ip=int(input("Enter your system ip"))

				password=input("Enter password")

				os.system("echo {password}>ssh.txt")

				os.system("scp hadoop-1.2.1-1.x86_64.rpm {ip}:/")

				os.system("scp openssh-7.8p1-4.el8.x86_64.rpm {ip}:/")

				os.system("sshpass -f ssh.txt ssh root@{ip}")

				os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm")

			elif int(choice)==3:

				ip=int(input("Enter your system ip"))

				os.system("rpm -i jdk-8u171-linux-x64.rpm")

				os.system("cd /")

				os.system("mkdir /master")

				os.system("cd /etc/hadoop")

				os.system("sed -i '/<configuration>/a <property> <name> dfs.name.dir</name> <value> /master </value> </property>' hdfs-site.xml")

				os.system("sed -i '/<configuration>/a <property> <name> fs.default.name</name> <value> hdfs://{ip}:10 </value> </property>' core-site.xml")

				os.system("systemctl stop firewalld")

				print('Port Number of Master is 10')

			elif int(choice)==4:

				masterip=input("Enter master ip")

				portnumber=input('Enter port number to contact master')

				os.system("cd /")

				os.system("mkdir /slavenode")

				os.system("cd /etc/hadoop")

				os.system("sed '/<configuration>/a <property> <name> dfs.data.dir</name> <value> /slavenode </value> </property>' hdfs-site.xml")

				os.system("sed '/<configuration>/a <property> <name> fs.default.name</name> <value> hdfs://{masterip}:{portnumber} </value> </property>' core-site.xml")

			elif int(choice)==5:

				os.system("hadoop namenode -format")

			elif int(choice)==6:

				os.system("hadoop datanode -format")

			elif int(choice)==7:

				masterip=input("Enter master ip")

				portnumber=input('Enter port number to contact master')

				os.system("sed '/<configuration>/a <property> <name> fs.default.name</name> <value> hdfs://{masterip}:{portnumber} </value> </property>' core-site.xml")

			elif int(choice)==8:

				os.system(" hadoop fs ls /")

			elif int(choice)==9:

				filename=input("Enter your filename")

				os.system("hadoop fs -put {filename}")

			elif int(choice)==10:

				filename=input("Enter your filename")

				os.system("hadoop fs -rm /{filename}")
			elif int(choice)==11:
				block_size=int(input("Enter block size"))
				filename=input("Enter your filename")

				os.system("hadoop fs -D dfs.block.size={block_size} -put {filename}")

			elif int(choice)==12:

				filename=input("Enter filename")

				os.system("hadoop fs -cat /{filename}")

			elif int(choice)==13:

				filename=input("Enter filename which you want to create")

				os.system("hadoop fs -touchz {filename}")

			elif int(choice)==14:

				folder=input("Enter folder which you want to create")

				os.system("hadoop fs -mkdir /{folder}")

			elif int(choice)==15:

				folder=input("Enter folder you want to delete")

				os.system("hadoop fs -rmr /{folder}")
 
			elif int(choice)==16:

				filename=input("Enter file which you want to delete")

				os.system("hadoop fs -rm /{filename}")

			else:
				print("not supported")
	elif int(selected)==3:
		os.system("ifconfig enp0s3")
	elif int(selected)==4:
		exit(1)
	else:
		print('Wrong Choice')