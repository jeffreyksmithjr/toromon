#!/usr/bin/env python

import subprocess
import urllib2

def push(ui, repo, **kwargs):
	try:
		response = urllib2.urlopen('http://opendns.com', timeout=1)

		s3_proc = subprocess.call('make s3_upload', shell=True, cwd='/users/Jeff/blog/')
		hg_proc = subprocess.call('hg push ssh://hg@bitbucket.org/jeffreyksmithjr/blog', shell=True)
	except:
		print 'No internet, so not pushing to the servers'