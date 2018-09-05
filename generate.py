#!/usr/bin/env python3

# Generates a profile with random attributes for each name in the netidfile.
# Outputs a json file to stdout

import sys
import json
import random
import os
import passhash

netidfile = "netids.txt"

editors = ["vim", "emacs", "nano", "notepad++"]
structures = ["rbtree", "treap", "bst", "fibonacci heap", "list", "vector", "array"]
tabsorspaces = ["tabs", "spaces"]
shells = ["csh", "bash", "zsh", "tcsh", "ksh"]
os = ["mac", "windows", "linux"]
cowsay = ["telebears", "moose", "koala", "dragon"]


profiles = {}
netids = [line.rstrip() for line in open(netidfile)]
n = len(netids)

for netid in netids:
	new = {}
	new["editor"] = editors[random.randint(0, len(editors)-1)]
	new["tabsorspaces"] = tabsorspaces[random.randint(0, len(tabsorspaces)-1)]
	new["structure"] = structures[random.randint(0, len(structures)-1)]
	new["shell"] = shells[random.randint(0, len(shells)-1)]
	new["password"] = passhash.hash(netid)
	new["messages"] = []
	new["friends"] = []
	new["requests"] = []
	new["os"] = os[random.randint(0, len(os)-1)]
	new["cowsay"] = cowsay[random.randint(0, len(cowsay)-1)]
	profiles[netid] = new

for netid in netids:
	for _ in range(random.randint(0, 20)):
		newfriend = netids[random.randint(0, n-1)]
		if newfriend != netid and newfriend not in profiles[netid]["friends"]:
			profiles[netid]["friends"].append(newfriend)
			profiles[newfriend]["friends"].append(netid)

data = {}
data["profiles"] = profiles

print(json.dumps(data, sort_keys=True, indent=4))
