#!/usr/bin/python3
"""Command-line interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the command module"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit command"""
        return True

    def emptyline(self):
        """An empty line command"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_help(self, arg):
        """Show help for commands."""
        if arg:
            if hasattr(self, 'do_' + arg):
                func = getattr(self, 'do_' + arg)
                print(f"{func.__doc__}\n")
        else:
            super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
