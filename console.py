#!/usr/bin/python3
"""Command-line interpreter"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter"""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
    }

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.

        Usage: create <class>

        Args:
            arg (str): command line arguments
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = eval(arg)()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id.

        Usage: show <class> <id>

        Args:
            arg (str): command line arguments
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).

        Usage: destroy <class> <id>

        Args:
            arg (str): command line arguments
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.

        Usage: all <class> or all

        Args:
            arg (str): command line arguments
        """
        args = arg.split()
        if not arg:
            print([str(v) for v in models.storage.all().values()])
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in models.storage.all().items()
                   if k.split('.')[0] == args[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file).

        Usage: update <class> <id> <attribute name> "<attribute value>"

        Note:
            All other arguments should not be used
                (Ex: $ update <class> <id> <attribute1> <"value"> <attribute2>
                <"value"> = $ update <class> <id> <attribute1> <"value">
            id, created_at and updated_at cant’ be updated)

        Args:
            arg (str): command line arguments
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in models.storage.all():
                obj = models.storage.all()[key]
                setattr(obj, args[2], eval(args[3]))
                models.storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
