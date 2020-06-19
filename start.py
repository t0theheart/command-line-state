from command_line import CommandLine


def main():
    print('"Command line state" started!')

    program = CommandLine()
    print(program.get_state())
    #while True:
    #line = input('Enter command line: ')

    line = 'add'
    program.parse_command_line(line)
    print(program.get_state())

    line = 'add "dff_dfdsf_12312"'
    program.parse_command_line(line)
    print(program.get_state())

    line = 'add "dff_dfdsf_12312" -n'
    program.parse_command_line(line)
    print(program.get_state())

    line = 'add "dff_dfdsf_12312" -n sdf'
    program.parse_command_line(line)
    print(program.get_state())


if __name__ == '__main__':
    main()
