import json
import os

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
        timeout,
    ) -> None:
        self.name = name
        self.command = command
        self.args = args
        self.directory = directory
        self.environment = environment
        self.ip_whitelist = ip_whitelist
        self.ip_blacklist = ip_blacklist
        self.token = token
        self.description = description
        self.timeout = timeout
    
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
            os.environ.update(self.environment)

        command = self.command
        if self.args:
            command += ' ' + ' '.join(self.args)
        return os.system(command)
    


# Parser class is used to parse the commands file
class Parser:
    def parse(self, commands_file):
        with open(commands_file) as f:
            data = json.load(f)
        commands = []
        for command in data['commands']:
            commands.append(self.parse_command(command))
        return commands
    def parse_command(self, command):
        if 'name' not in command:
            raise Exception('Command name not specified')
        if 'command' not in command:
            raise Exception('Command command not specified')

        name = command['name']
        command = command['command']
        args = command['args'] if 'args' in command else []
        directory = command['directory'] if 'directory' in command else None
        environment = command['environment'] if 'environment' in command else None
        ip_whitelist = command['ip_whitelist'] if 'ip_whitelist' in command else None
        ip_blacklist = command['ip_blacklist'] if 'ip_blacklist' in command else None
        token = command['token'] if 'token' in command else None
        description = command['description'] if 'description' in command else None
        timeout = command['timeout'] if 'timeout' in command else None
        return Command(name, command, args, directory, environment, ip_whitelist, ip_blacklist, token, description, timeout)