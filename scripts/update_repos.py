#!/usr/bin/env python

import subprocess
import urllib2

def push(ui, repo, **kwargs):
	try:
		response = urllib2.urlopen('http://opendns.com', timeout=1)

		# update BitBucket
		hg_proc = subprocess.call('hg push main', shell=True)
		# move bookmark forward for Git
		bm_proc = subprocess.call('hg bookmark -f master', shell=True)
		# update GitHub
		gh_proc = subprocess.call('hg push mirror', shell=True)
	except:
		print 'No internet, so not pushing to the servers'
