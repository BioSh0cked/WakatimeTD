import os
import time
import subprocess
import platform
import json
import re

try:
	from urllib2 import Request, urlopen, HTTPError
except ImportError:
	from urllib.request import Request, urlopen
	from urllib.error import HTTPError


GITHUB_PREFIX = 'https://github.com/wakatime/wakatime-cli/releases/download'
GITHUB_LATEST_URL = 'https://api.github.com/repos/wakatime/wakatime-cli/releases/latest'
is_win = platform.system() == 'Windows'


class WakaExt:
	def __init__(self, ownerComp) -> None:
		self.owner = ownerComp
		self.last_heartbeat = 0
		self.idle_timeout = 60
		self.api_key = self.Get_key()
		self.cli_path = self.Get_cli()

	def Get_latest_client_version(self):
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
	def Get_key(self):
		global api_url
		global config
		config = os.path.expanduser("~/.wakatime.cfg")
		if os.path.exists(config):
			with open(config, "r") as f:
					for line in f:
						if line.startswith('api_url'):
							api_url = line.split('=')[1].strip()
						if line.startswith("api_key"):
							return line.split("=")[1].strip()

					run(
						"op('{}').op('KeyDialog').par.Open.pulse()".format(self.owner.path),
						delayFrames=1
					)

	def Get_cli(self):
		global WAKATIME_CLI_PATH

		WAKATIME_CLI_PATH = os.path.join("~/.wakatime/wakatime-cli")

		if not os.path.exists(WAKATIME_CLI_PATH):
			waka_cli = 'wakatime-cli-{osname}-{arch}{ext}'.format(
				osname=platform.system().lower(),
				arch=platform.machine() or platform.processor(),
				ext='.exe' if is_win else '',
			)
			WAKATIME_CLI_PATH = os.path.join("~/.wakatime/", waka_cli)
		return WAKATIME_CLI_PATH

	def ReplaceApiFromDialog(self, enteredText):
		if os.path.exists(config) and self.api_key is None:
			self.api_key = enteredText
			with open(config, "a") as f:
				f.write("\napi_key = " + enteredText)

	def Send_heartbeat(self, entity):
		if not self.api_key or not WAKATIME_CLI_PATH:
			return

		if time.time() - self.last_heartbeat < 60:
			return
		project_name = re.sub(r'\.\d+(?=\.toe$)', '', project.name)
		_entity = re.sub(r'\.\d+(?=\.toe$)', '', entity)
		try:

			cmd = [
				'--key', self.api_key,
				'--entity', _entity,
				'--project', project_name,
				'--plugin', 'tdwakatime/0.0.1']
			if api_url is not None:
				cmd.extend(['--api-url', api_url])

			subprocess.Popen(
				[os.path.expanduser(self.cli_path)] + cmd
			)
			self.last_heartbeat = time.time()
		except Exception as e:
			print("Heartbeat error:", e)