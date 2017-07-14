import subprocess
import os
import shutil

if os.path.isfile("./db.sqlite3"):
	os.remove("./db.sqlite3")
	
if os.path.isdir("./db.sqlite3"):	
	shutil.rmtree("./gettrafficlights/migrations")	

subprocess.Popen(["python", "manage.py", "makemigrations", "gettrafficlights" ]).communicate()
subprocess.Popen(["python", "manage.py", "makemigrations", "--empty", "gettrafficlights" ]).communicate()
subprocess.Popen(["python", "manage.py", "migrate" ]).communicate()
subprocess.Popen(["python", "manage.py", "loaddata", "./gettrafficlights/fixtures/database.json" ]).communicate()

check_user = raw_input("Load Streets in Fixtures? (Y/N) ")
if check_user == 'Y':
	subprocess.Popen(["python", ".\DBStreetFiller.py" ]).communicate()


check_user = raw_input("Include Extracted Streets in the Database? (Y/N) ")
if check_user == 'Y':
	subprocess.Popen(["python", "manage.py", "loaddata", "./gettrafficlights/fixtures/streets.json" ]).communicate()
