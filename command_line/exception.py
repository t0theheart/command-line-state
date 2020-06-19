

class CommandLineException(Exception):
    pass


command_line_is_not_valid = CommandLineException('command line is not valid.')
