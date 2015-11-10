#!/usr/bin/env python

import pexpect
import logging
import time
from pexpect import pxssh
from ssh import SSH

class Linux(SSH):

	def __init__(self, config):
		self.setSession(config)

	def mkdir(self, path):
		session = self.session
		cmd = "mkdir -p " + path
		self.command(cmd)
		session.sendline(cmd)
		session.prompt()

	def cd(self, path):
		session = self.session
		cmd = "cd " + path
		self.command(cmd)
		session.sendline(cmd)
		session.prompt()

	def ls(self, path=''):
		if path is '':
			path = '.'
		session = self.session
		cmd = "ls -l " + path
		self.command(cmd)
		session.sendline(cmd)
		session.prompt()
		self.info(session.before)

	def pwd(self):
		session = self.session
		cmd = "pwd"
		self.command(cmd)
		session.sendline(cmd)
		session.prompt()
		self.info(session.before)

	def rm_Rf(self, path):
		if path is not '':
			session = self.session
			cmd = "ls -l " + path
			self.command(cmd)
			session.sendline(cmd)
			session.prompt()
			self.info(session.before)
