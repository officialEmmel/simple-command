# SimpleCommand

from server import Server
from command_parse import Parser, Command
from command_handle import Handle
import argparse

# some args
parser = argparse.ArgumentParser(description='Simple Command 1.0')
parser.add_argument('-p', '--port', type=int, default=5000, help='Port to run the server on')
parser.add_argument('-H', '--host', type=str, default='127.0.0.1', help='Host to run the server on')
parser.add_argument('-c', '--commands', type=str, default='commands.json', help='Path to the commands file')
args = parser.parse_args()

# create handler class and give it the parsed commands
handler = Handle(Parser().parse(args.commands))

# create a server instance
server = Server(args.port, args.host, handler.execute)

# run the server
server.run()