# SimpleCommand

from server import Server
from command_parse import Parser, Command
from command_handle import Handle
import argparse

# some args
parser = argparse.ArgumentParser(description='Simple Command 1.0')
parser.add_argument('-p', '--port', type=int, default=5000, help='Port to run the server on')
parser.add_argument('-i', '--ip', type=str, default='127.0.0.1', help='Host to run the server on')
parser.add_argument('-c', '--commands', type=str, default='commands.json', help='Path to the commands file')
parser.add_argument('-m', '--module', type=str, default='', help='Name of module followed by its arguments (separated by commas). E.g. "module1 arg1=hello arg2=world, module2')
parser.add_argument('-t', '--tray', action='store_true', help='Show tray icon (Desktop only obviously)')
parser.add_argument('-H', '--hidden', action='store_true', help='Hide console window instantly (Windows only)')



args = parser.parse_args()

if args.module:
    module = args.module
    name = module.split(' ')[0]
    args = module.split(' ')[1:]
    args = ','.join(args)
    try:
        exec(f'import modules.{name}')
        exec(f'modules.{name}.main({args})')
    except Exception as e:
        print(f'Failed to import module {name}: {e}')
    exit()


print("Simple Command 1.0")
print("USE IN TRUSTED NETWORKS ONLY - DO NOT EXPOSE TO THE INTERNET OR UNTRUSTED NETWORKS\n")


# create handler class and give it the parsed commands
handler = Handle(Parser().parse(args.commands))

# create a server instance
server = Server(args.port, args.host, handler.execute)

# run the server
server.run()