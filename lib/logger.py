#!/usr/bin/env python

class Print:
	level = 'ALL'
	def __init__(self, loglevel=''):
		if loglevel != '':
			self.level = loglevel
		print "[LOGGER] Log level is " + self.level

	def info(self, data):
		if self.level is 'DEBUG' or self.level is 'ALL':
			print "[INFO] " + data

	def command(self, data):
		if self.level is 'COMMAND' or self.level is 'ALL':
			print "[COMMAND] " + data

	def warn(self, data):
		if self.level is 'ALL' or self.level is 'WARNING':
			print "[WARNING] " + data

	def error(self, data):
		if self.level is 'ALL' or self.level is 'ERROR':
			print "[ERROR] " + data

	def success(self, data):
		if self.level is 'ALL' or self.level is 'SUCCESS':
			print "[SUCCESS] " + data

	def printLogLevel(self):
		print "[LOGGER] Log level: " + self.level

	def setLogLevel(self, loglevel):
		self.level = loglevel
		print "[LOGGER] Log level is " + self.level 