import json
import os
import subprocess

# Command class containing all the information about a command
class Command:
    def __init__(
        self,
        name,
        command,
        args,
        directory,
        environment,
        ip_whitelist,
        ip_blacklist,
        token,
        description,
        webhook
    ):
        self.name = name
        self.command = command
        self.args = args
        self.directory = directory
        self.environment = environment
        self.ip_whitelist = ip_whitelist
        self.ip_blacklist = ip_blacklist
        self.token = token
        self.description = description
        self.webhook = webhook
    
    def authorize(self, ip, token):
        if self.ip_whitelist and ip not in self.ip_whitelist:
            return False
        if self.ip_blacklist and ip in self.ip_blacklist:
            return False
        if self.token and token != self.token:
            return False
        return True
    def execute(self):
        if self.directory:
            os.chdir(self.directory)
        if self.environment:
            for key, value in self.environment.items():
                os.environ[key] = value

        command = self.command
        if self.args:
            command += ' ' + ' '.join(self.args)
        print("Executing command " + self.name + " with command '" + command+"':")
        try:
            exec = subprocess.run(command, shell=True, capture_output=True)
            print(" + Command output: " + exec.stdout.decode('utf-8'))
            print(" - Command error: " + exec.stderr.decode('utf-8'))
            self.call_webhook()
            return (exec.returncode, exec.stdout.decode('utf-8'), exec.stderr.decode('utf-8'))
        except Exception as e:
            print(" + Command failed: " + str(e))
            self.call_webhook()
            return (1, None, None)
    def call_webhook(self):
        import requests
        if self.webhook:
            print(" + Calling webhook: " + self.webhook)
            try:
                requests.get(self.webhook)
            except Exception as e:
                print(" - Webhook failed: " + str(e))



        
    def __str__(self):  
        return f'Command(name={self.name}, command={self.command}, args={self.args}, directory={self.directory}, environment={self.environment}, ip_whitelist={self.ip_whitelist}, ip_blacklist={self.ip_blacklist}, token={self.token}, description={self.description})'
        

# Parser class is used to parse the commands file
class Parser:
    def parse(self, commands_file):
        with open(commands_file) as f:
            data = json.load(f)
        commands = []
        for command in data['commands']:
            commands.append(self.parse_command(command))

        print("Parsed " + str(len(commands)) + " commands from " + commands_file + ":")
        for command in commands:
            print(" + "+command.name + ": '" + command.command + "'")

        return commands
    def parse_command(self, command):

        if 'name' not in command:
            raise Exception('Command name not specified')
        if 'command' not in command:
            raise Exception('Command command not specified')
    

        name = command['name']
        command2execute = command['command']
        args = command['args'] if 'args' in command else []
        directory = command['directory'] if 'directory' in command else None
        environment = command['environment'] if 'environment' in command else None
        ip_whitelist = command['ip_whitelist'] if 'ip_whitelist' in command else None
        ip_blacklist = command['ip_blacklist'] if 'ip_blacklist' in command else None
        token = command['token'] if 'token' in command else None
        description = command['description'] if 'description' in command else None
        webhook = command['webhook'] if 'webhook' in command else None
        return Command(name=name, command=command2execute, args=args, directory=directory, environment=environment, ip_whitelist=ip_whitelist, ip_blacklist=ip_blacklist, token=token, description=description, webhook=webhook)