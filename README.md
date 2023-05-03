# simple-command
A very simple HTTP Server that allows command execution on host. 

<h4 style="color:red">WARNING: USE IN LOCAL AND TRUSTED NETWORKS ONLY. Making your machine controllable via HTTP in an untrusted environment is stupid. </h4>

## Idea
This is an optimized version of a script i made to contol my windows pc with homeassistant. (e.g scheduled shutdowns or someting smlr)

## Features
- Authentication
    - token
    - IP-Whitelist
    - IP-Blacklist
- set custom env vars
- commands with args
- webhook on execution
- returns output of command 
- modules

## Usage
### Example
Basic usage for an instance runnig on port 8081:
```main.py -p 8081 -i 0.0.0.0 -c commands.json```

### Arguments
```
-h, --help            show this help message and exit
  -p PORT, --port PORT  Port to run the server on
  -i IP, --ip IP        Host to run the server on
  -c COMMANDS, --commands COMMANDS
                        Path to the commands file
  -m MODULE, --module MODULE
                        Name of module followed by its arguments. E.g. "module1 arg1 arg2"
  -t, --tray            Show tray icon (Desktop only obviously)
  -H, --hidden          Hide console window instantly (Windows only)
```

### Commands.json
| Key | Description | Example |
|---|---|---|
|`name`|(required) URL-Safe Name of command  | `"name":"test-command"|
|`command`|(required) Command to be executed| `"command":"echo $FOO"|
|`environment`|Array of environment vars.| `"environment":{"FOO":"bar"}`|
|`directory`|Directory the command will be executed in|`"directory":"/tmp"`|
|`token`|Token the user must authenticate in order ro execute the command. Tip: generate a token with the `token`-module |`"token":"abc123"`|
|`ip_whitelist`|Array of IPs that can execute the command|`"ip_whitelist":["10.0.123.65"]`|
|`ip_blacklist`|Array of IPs that cant access the command|`"ip_blacklist":["10.0.246.187"]`|
|`description`|Small description of the commmand|`"description":"this is a description"`|
|`webhook`|Webhook that gets called on every execution|`"webhook":"http://localhost:8080"`|

### Modules
