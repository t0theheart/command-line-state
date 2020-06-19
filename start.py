from command_line import CommandLine
from command_line.exception import CommandLineException


def main():
    print('"Command line state" started!')
    program = CommandLine()

    while True:
        line = input('Enter command line: ')
        try:
            program.parse_command_line(line)
            print(program.get_state())
        except CommandLineException as e:
            print(f'ERROR: {e}')
        print()


if __name__ == '__main__':
    main()
