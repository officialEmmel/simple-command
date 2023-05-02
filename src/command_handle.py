from flask import jsonify, request
# handle class is used to find and execute commands
class Handle:
    def __init__(self, commands):
        self.commands = commands
    def find(self, name):
        for command in self.commands:
            if command.name == name:
                return command
        return None
    def execute(self, name):
        ip = request.remote_addr
        token = request.args.get('token')
        if not name:
            return jsonify({'error':'No command name provided'}), 400
        command = self.find(name)
        if not command:
            return jsonify({'error':'Command not found'}), 404
        if not command.authorize(ip, token):
            return jsonify({'error':'Not authorized'}), 403
        res = command.execute()
        
        if res[1] == None and res[2]== None:
            return jsonify({'error':'Command failed to execute'}), 500
        return jsonify({'returncode':res[0], 'stdout':res[1], 'stderr':res[2]}), 200
        
