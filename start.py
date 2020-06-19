from command_line import CommandLine
from command_line.exception import CommandLineException


def main():
    """
        Example of using:

        "Command line state" started!
        Enter command line: add
        state: {'state': 'command', 'command': 'add'}

        Enter command line: add param
        state: {'state': 'command with params', 'command': 'add', 'command_params': 'param'}

        Enter command line: add param -c
        state: {'state': 'command with params and key', 'command': 'add', 'command_params': 'param', 'key': '-c'}

        Enter command line: add param -a key_param
        state: {'state': 'command with params and key with params', 'command': 'add', 'command_params': 'param', 'key': '-a', 'key_params': 'key_param'}

        Enter command line:
        state: {'state': 'empty state'}

        Enter command line: exit
        End.
    """
    print('"Command line state" started!')
    program = CommandLine()

    while True:
        line = input('Enter command line: ')
        if line == 'exit':
            print('End.')
            break
        try:
            program.parse_command_line(line)
            print(f'state: {program.get_state()}')
        except CommandLineException as e:
            print(f'error: {e}')
        print()


if __name__ == '__main__':
    main()
