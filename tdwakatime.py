import os
import threading
import time
import subprocess
import platform
import json

try:
	from urllib2 import Request, urlopen, HTTPError
except ImportError:
	from urllib.request import Request, urlopen
	from urllib.error import HTTPError

GITHUB_PREFIX = 'https://github.com/wakatime/wakatime-cli/releases/download'
GITHUB_LATEST_URL = 'https://api.github.com/repos/wakatime/wakatime-cli/releases/latest'
is_win = platform.system() == 'Windows'

class Wakatime:
	def __init__(self, ownerComp):
		self.owner = ownerComp
		self.last_cook = 0
		self.last_heartbeat = 0
		self.idle_timeout = 60
		self.api_key = self.get_key()
		self.cli_path = self.get_cli()
		if not hasattr(project, 'Plugin_Initialized'):
			project.addCallback(self.Event)
			project.Plugin_initialized = True
		print("Wakatime plugin initialized")

	def Event(self, event):
		if event['name'] in ['onValueChange', 'onCreate', 'onProjectPostSave']:
			self.last_cook = time.time()
			self.send_heartbeat(event)
	def get_latest_client_version():
		latest_version = "0"
		config = os.path.expanduser("~/.wakatime/wakatime-internal.cfg")
		if config:
			with open(config, "r") as f:
				for line in f:
					if line.startswith("cli_version"):
						ver=line.split("=")[1].strip()
		try:
			contents = Request(GITHUB_LATEST_URL)
			data = json.loads(contents.decode('utf-8'))
			latest_version = data['tag_name']
		except:
			pass
		if not config or ver < latest_version:
				Request(url='{prefix}/{ver}/wakatime-cli-{osname}-{arch}.zip'.format(
					prefix=GITHUB_PREFIX,
					ver=ver,
					osname=platform.system().lower(),
					arch=platform.machine() or platform.processor(),
				))
	def get_key():
		global API_KEY
		config = os.path.expanduser("~/.wakatime.cfg")
		if os.path.exists(config):
			with open(config, "r") as f:
					for line in f:
						if line.startswith("api_key"):
								return line.split("=")[1].strip()
	def get_cli():
		global WAKATIME_CLI_PATH

		WAKATIME_CLI_PATH = os.path.join("~/.wakatime/wakatime-cli")

		if not WAKATIME_CLI_PATH:
			waka_cli = 'wakatime-cli-{osname}-{arch}{ext}'.format(
				osname=platform.system().lower(),
				arch=platform.machine() or platform.processor(),
				ext='.exe' if is_win else '',
			)
			WAKATIME_CLI_PATH = os.path.join("~/.wakatime/", waka_cli)
		return WAKATIME_CLI_PATH

	API_KEY = get_key()
	WAKATIME_CLI_PATH = get_cli()

	def heartbeat(self, entity=None):
		if not API_KEY or not WAKATIME_CLI_PATH:
			return

		if time.time() - self.last_heartbeat < 60:
			return
		entity = project.path
		project_name = os.path.basename(entity)

		try:
			subprocess.Popen([
				self.cli_path,
				'--key', self.api_key,
				'--entity', entity,
				'--project', project_name,
				'--plugin', 'tdwakatime/0.0.1'
			])
			self.last_heartbeat = time.time()
		except Exception as e:
			print("Heartbeat error:", e)