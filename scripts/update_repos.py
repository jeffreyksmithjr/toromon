#!/usr/bin/env python

import subprocess
import urllib2

def push(ui, repo, **kwargs):
	try:
		response = urllib2.urlopen('http://opendns.com', timeout=1)

		hg_proc = subprocess.call('hg push main', shell=True)
		gh_proc = subprocess.call('hg push mirror')
	except:
		print 'No internet, so not pushing to the servers'

