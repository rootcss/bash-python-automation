#!/usr/bin/env python

# import files here eg, SSH, Print, Linux, PSQL as per the requirement
from logger import Print

if __name__ == '__main__':
	logger = Print("SUCCESS")
	logger.printLogLevel()


# How to use:
#
# #1:
	# obj = Linux({'hostname':'localhost', 'username':'rootcss', 'password':'password'})
	# obj.ls()
	# obj.disconnect()
# #2:
	# dbs = ['api_test', 'api_development', 'analytics']
	# timestamp = time.strftime("%d-%m-%Y-%H-%M-%S")
	# psql = PSQL({'hostname':'localhost', 'username':'postgres', 'password':'postgres', 'port':'5432'})
	# psql.setSession({'hostname':'localhost', 'username':'jarvis', 'password':'password'})
	# psql.createDBs(['shekhar', 'singh'])
	# psql.listDBs()
	# psql.dropDBs(['shekhar', 'singh'])
	# psql.listDBs()
	# psql.ls()
	# psql.pwd()
	# psql.disconnect()
	#
	# OR
	#
	# psql = PSQL({'hostname':'localhost', 'username':'postgres', 'password':'postgres', 'port':'5432'})
	# psql.setSession({'hostname':'localhost', 'username':'rootcss', 'password':'password'})
	# psql.info(psql.getHostname())
	# psql.restoreDBs('', '', '')
	# psql.disconnect()
# #3:
	# server = SSH({'hostname':'localhost', 'username':'rootcss', 'password':'password'})
	# server.info(server.getHostname())
	# server.disconnect()
# #4:
	# logger = Print("SUCCESS")
	# logger.printLogLevel()
	# logger.warn("dsfsdf")
	# logger.info("info")
	# logger.error("error")
	# logger.command("command")
	# logger.success("success")
	# print "______"
	# logger.setLogLevel("ERROR")
	# logger.printLogLevel()
	# logger.warn("dsfsdf")
	# logger.info("info")
	# logger.error("error")
	# logger.command("command")
	# logger.success("success")

