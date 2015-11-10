#!/usr/bin/env python

import pexpect
from pexpect import pxssh
from logger import Print

class SSH(Print):
	config = {'hostname':'', 'username':'', 'password':''}
	session = None
	max_tries = 10

	def __init__(self, config):
		self.setSession(config)

	def setSession(self, config):
		self.config['hostname'] = config['hostname']
		self.config['username'] = config['username']
		self.config['password'] = config['password']
		self.connect()

	def connect(self):
		data = self.config
		unconnected = True
		tries = 0
		while unconnected and tries <= self.max_tries:
			if tries == self.max_tries:
				self.warn("Maximum allowed tries are about to get over!")

			try:
				session = pxssh.pxssh()
				self.info("Logging into " + data['hostname'] + "...")
				if not session.login (data['hostname'], data['username'], data['password']):
					self.error("SSH login failed.")
					print str(session)
					print
					self.warn("Unable to connect. Retrying...")
					tries = tries + 1
				else:
					self.info("Connected via SSH.")
					unconnected = False
					#return session
					self.session = session
			except Exception:
				self.warn("Unable to connect. Retrying...")
				tries = tries + 1
				unconnected = True

	def disconnect(self):
		sess = self.session
		sess.logout()
		self.info("Logged out!")

	def getHostname(self):
		return self.config['hostname']

	def getUsername(self):
		return self.config['username']

	def getSession(self):
		return self.session