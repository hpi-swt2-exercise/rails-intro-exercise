from __future__ import print_function
import logging, os, requests, sys

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)

repo_env_var = 'GITHUB_REPOSITORY'
repo = os.environ.get(repo_env_var)
logging.debug("repo: '{repo}'".format(repo=repo))
if not repo:
	logging.error("Could not fetch env var {var}".format(var=repo_env_var))
url = "https://github.com/{repo}/issues".format(repo=repo)

try:
	logging.info("Pinging GitHub issues: {url}".format(url=url))
	r = requests.head(url)
	if r.status_code != 200:
		logging.warning("Issues not enabled (or repo is private)! ({code})".format(code=r.status_code))
		sys.exit(1)
except requests.ConnectionError:
	logging.error("Failed to connect to {url}".format(url=url))
	sys.exit(1)

print("All good! Issues of '{repo}' seem enabled.".format(repo=repo))
