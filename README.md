# WakaTimeTD
[WakatimeTD](https://github.com/BioSh0cked/WakatimeTD) is a .tox plugin for TouchDesigner to allow for WakaTime time tracking.

## Installation
1. Clone the repository or download the latest release
```git clone https://github.com/BioSh0cked/WakatimeTD```
2. Drag-and-drop the .tox file into your TouchDesigner Project.
3. In the common parameter section on the .tox base enable 'Enable External .tox'
4. If prompted, enter your api key and confirm.
![TouchDesigner Component](https://flavortown.hackclub.com/rails/active_storage/representations/proxy/eyJfcmFpbHMiOnsiZGF0YSI6OTUyOTQsInB1ciI6ImJsb2JfaWQifX0=--e739badab2a89cba0411b595df3b0c0426bd5eb5/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJ3ZWJwIiwicmVzaXplX3RvX2xpbWl0IjpbODAwLDgwMF0sInNhdmVyIjp7InN0cmlwIjp0cnVlLCJxdWFsaXR5Ijo3NX19LCJwdXIiOiJ2YXJpYXRpb24ifX0=--b31f00576a4e60a9662bd00307d0a77b5bfc6d7e/pasted-2026-01-31T01-10-59-514Z.png)

## Troubleshooting (ALT+T)
[Errno2] Missing file or paths: This error can appear when WakatimeTD fails to install wakatime, restarting with elevated permissions may fix this.
[CLI download failure] Error downloading wakatimeCLI: Github or internet outage may cause this error to appear on first boot or updates, simply re-init or reset the plugin when outages are corrected to fix this error.
[Project Unknown] Time is set to unknown project or newproject.toe: Save the file with a name or place it in a directory initialized in a git repository.
[Any other] error: Copy the log and send it to me so I can fix it please :)

## Demo:
![DemoTD](https://github.com/BioSh0cked/WakatimeTD/blob/main/DemoTD.gif)
