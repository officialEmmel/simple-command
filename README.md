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
| Key | Description |   
|---|---|
|`name`|(required) URL-Safe Name of command  |
|`command`|(required) Command to be executed|
|`environment`|Array of environment vars. e.g: ```json "environment":{"FOO":"bar"}```   |


