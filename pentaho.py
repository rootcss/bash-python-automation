#!/usr/bin/env python

import sys
import time
from lib.psql import PSQL

dbs = ['target']
timestamp = time.strftime("%d-%m-%Y-%H-%M-%S")
# Instantiate PSQL configurations
psql = PSQL({'hostname':'127.0.0.1', 'username':'postgres', 'password':'postgres', 'port':'5432'})
# Create SSH session
psql.setSession({'hostname':'127.0.0.1', 'username':'rootcss', 'password':'password'})

try:
	action = sys.argv[1]
except Exception:
	psql.error("Please provide the necessary arguments:\n1. dump_drop_create\n2. take_db_backup\n3. list_dbs")
	raise Exception('Argument was not provided!')

psql.info("DB selected: "+str(dbs))
psql.info("Operation selected: "+action)

if action == 'dump_drop_create':
	psql.dumpDBs(dbs, timestamp)
	psql.dropDBs(dbs)
	psql.createDBs(dbs)
	psql.success("All operations completed successfully!")
elif action == 'take_db_backup':
	psql.dumpDBs(dbs, timestamp)
	psql.success("Database backed up.")
elif action == 'list_dbs':
	psql.listDBs()
	psql.success("Database listed!")
else:
	psql.error("Please provide the necessary arguments:\n1. dump_drop_create\n2. take_db_backup\n3. list_dbs")
	raise Exception('Argument was not provided!')

psql.disconnect()
