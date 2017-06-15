import subprocess
subprocess.Popen(["python", "manage.py", "makemigrations", "--empty", "gettrafficlights" ]).communicate()
subprocess.Popen(["python", "manage.py", "migrate" ]).communicate()
subprocess.Popen(["python", "manage.py", "loaddata", "./gettrafficlights/fixtures/data.json" ]).communicate()