#!/usr/bin/python3
"""Command-line interpreter"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter"""
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review",
            }

    def default(self, arg):
        """Called on an input line when the command prefix is not recognized.
        If this method is not overridden, it prints an error message and
        returns.

        Args:
            arg (str): command line arguments
        """
        args = arg.split('.')
        if len(args) > 1 and args[0] in HBNBCommand.__classes:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                print(len([v for k, v in models.storage.all().items()
                          if k.split('.')[0] == args[0]]))
            elif args[1][:5] == "show(" and args[1][-1] == ')':
                self.do_show(f"{args[0]} {args[1][6:-2]}")
            elif args[1][:8] == "destroy(" and args[1][-1] == ')':
                self.do_destroy(f"{args[0]} {args[1][9:-2]}")
            elif args[1][:7] == "update(" and args[1][-1] == ')':
                if "{" in args[1] or "}" in args[1]:
                    args[1] = args[1].replace('{', '').replace('}', '')
                new_args = args[1][8:-1].split(', ')

                temp_arg = []
                for arg in new_args[1:]:
                    if ":" in arg:
                        temp_arg.append(arg.replace(':', ','))
                if len(temp_arg) == 0:
                    temp_arg.append(f"{new_args[1]}, {new_args[2]}")

                for arg in temp_arg:
                    new_args = [new_args[0]] + arg.split(', ')
                    args = [args[0]] + new_args
                    args = [arg.replace('"', '') for arg in args]
                    args = [arg.replace("'", '') for arg in args]
                    if len(args) < 1:
                        print("** instance id missing **")
                    elif len(args) < 2:
                        print("** attribute name missing **")
                    elif len(args) < 3:
                        print("** value missing **")
                    else:
                        key = f"{args[0]}.{args[1]}"
                        if key in models.storage.all():
                            obj = models.storage.all()[key]
                            self.do_update(
                                    f"{args[0]} {args[1]} {args[2]} {args[3]}")
                        else:
                            print("** no instance found **")

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
                try:
                    setattr(obj, args[2], eval(args[3]))
                except NameError:
                    setattr(obj, args[2], args[3])
                finally:
                    models.storage.save()
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """Retrieve the number of instances of a class.

        Usage: count <class>

        Args:
            arg (str): command line arguments
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(len([v for k, v in models.storage.all().items()
                      if k.split('.')[0] == args[0]]))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
