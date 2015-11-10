#!/usr/bin/env python

from linux import Linux

class PSQL(Linux):
	dbconfig = {'hostname':'', 'username':'', 'password':'', 'port':'5432'}
	backup_dir = None

	def __init__(self, config):
		self.dbconfig['hostname'] = config['hostname']
		self.dbconfig['username'] = config['username']
		self.dbconfig['password'] = config['password']
		self.dbconfig['port'] = config['port']

	def dumpDBs(self, databases, timestamp, backup_dir=''):
		self.info("Preparing to dump databases..")
		session = self.session
		if backup_dir is '':
			backup_dir = "~/backup/" + timestamp
		self.backup_dir = backup_dir
		self.mkdir(backup_dir)
		self.cd(backup_dir)

		for db in databases:
			backup_file = db + "_" + timestamp
			self.info("Backing up DB: '" + db + "' in backup_file: '" + backup_file + "'..")
			cmd = "pg_dump -i -U " + self.dbconfig['username'] + " -h " + self.dbconfig['hostname'] + " -p " + self.dbconfig['port'] + " " + db + " > " + backup_file
			self.command(cmd)
			session.sendline(cmd)
			session.expect('Password:')
			session.sendline(self.dbconfig['password'])
			session.prompt()
			#print session.before
		self.success("DB Dump completed successfully!")

	def buildSQLCommand(self, query):
		cmd = 'psql -W -h '+self.dbconfig['hostname']+' -p '+self.dbconfig['port']+' -U '+self.dbconfig['username']+' -c "'+query+'"'
		self.info(cmd)
		return cmd

	def dropDBs(self, databases):
		session = self.session
		self.info("Dropping existing databases..")
		for db in databases:
			self.info("Disonnecting active clients..")
			query = "UPDATE pg_database SET datallowconn = 'false' WHERE datname = '"+db+"'"
			cmd = self.buildSQLCommand(query)
			session.sendline(cmd)
			session.expect('Password for user '+ self.dbconfig['username'] +':')
			session.sendline(self.dbconfig['password'])
			session.prompt()
			print session.before

			self.info("Terminating PIDs of active clients...")
			query = "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '"+db+"'"
			cmd = self.buildSQLCommand(query)
			session.sendline(cmd)
			session.expect('Password for user '+ self.dbconfig['username'] +':')
			session.sendline(self.dbconfig['password'])
			session.prompt()
			print session.before

			self.info("Dropping DB: '" + db + "'..")
			query = "DROP DATABASE "+db
			cmd = self.buildSQLCommand(query)
			session.sendline(cmd)
			session.expect('Password for user '+ self.dbconfig['username'] +':')
			session.sendline(self.dbconfig['password'])
			session.prompt()
			print session.before
		self.success("DBs Drop completed successfully!")	

	def createDBs(self, databases):
		session = self.session
		for db in databases:
			self.info("Creating DB: '" + db + "'..")
			query = "CREATE DATABASE "+db
			cmd = self.buildSQLCommand(query)
			session.sendline(cmd)
			session.expect('Password for user '+ self.dbconfig['username'] +':')
			session.sendline(self.dbconfig['password'])
			session.prompt()
			print session.before
		self.success("DBs created successfully!")	

	def restoreDBs(self, databases, timestamp, file_path=''):
		# TO DO
		self.info("Function yet to define!")
		pass

	def listDBs(self):
		session = self.session
		self.info("Listing DBs..")
		query = "SELECT datname FROM pg_database WHERE datistemplate = false"
		cmd = self.buildSQLCommand(query)
		session.sendline(cmd)
		session.expect('Password for user '+ self.dbconfig['username'] +':')
		session.sendline(self.dbconfig['password'])
		session.prompt()
		print session.before

	# def truncateAllTablesinDB(self, databases)
	# TO DO


# pg_dump -i -U postgres -h localhost -p 5432 target > script_backup_target
# cat script_backup_target | psql -h localhost -d test1 -U postgres -W

