#!/usr/bin/env python

import subprocess, json

output = subprocess.check_output("gh repo list --fork -L 43 --json name", shell=True)
repos = json.loads(output)

for repo in repos:
    subprocess.run(f"gh repo delete --confirm {repo['name']}", shell=True)
