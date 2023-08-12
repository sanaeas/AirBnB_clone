#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the AirBnB clone project
    """

    prompt = "(hbnb) "

    classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print('')
        return True

    def emptyline(self):
        """Do nothing when receiving an empty line."""
        pass

    def do_create(self, arg):
        """Create a new instance of the specified class and save it"""
        if not arg:
            print('** class name missing **')
        elif arg not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
        else:
            new_inst = eval(arg)()
            print(new_inst.id)
            new_inst.save()

    def do_show(self, arg):
        """Display the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            inst_key = "{}.{}".format(args[0], args[1].strip('"'))
            if inst_key in storage.all():
                print(storage.all()[inst_key])
            else:
                print('** no instance found **')

    def do_destroy(self, arg):
        """Delete an instance from storage"""
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            inst_key = "{}.{}".format(args[0], args[1].strip('"'))
            if inst_key in storage.all():
                del storage.all()[inst_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Display string representations of all instances"""
        args = arg.split()
        insts_ls = []
        if len(args) == 0:
            for instance in storage.all().values():
                insts_ls.append(str(instance))
        elif args[0] in HBNBCommand.classes:
            for instance in storage.all().values():
                if instance.__class__.__name__ == args[0]:
                    insts_ls.append(str(instance))
        else:
            print('** class doesn\'t exist **')
            return
        print(insts_ls)

    def do_update(self, arg):
        """Update an instance attribute and save changes to storage"""
        args = shlex.split(arg)
        if len(args) == 0:
            print('** class name missing **')
            return
        if args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        instance_key = "{}.{}".format(args[0], args[1].strip('"'))
        if instance_key not in storage.all():
            print('** no instance found **')
            return
        if len(args) == 2:
            print('** attribute name missing **')
            return
        if len(args) == 3:
            print('** value missing **')
            return
        instance = storage.all()[instance_key]
        setattr(instance, args[2], args[3])
        instance.save()

    def do_count(self, arg):
        """Count the number of instances of a class"""
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
        else:
            class_name = args[0]
            count = 0
            for instance in storage.all().values():
                if instance.__class__.__name__ == class_name:
                    count += 1
            print(count)

    def precmd(self, arg):
        commands = ['all', 'count', 'show', 'destroy', 'update']
        if '.' in arg and '(' in arg and ')' in arg:
            cls_cmd = arg.split('.')
            cmd_args = cls_cmd[1].split('(')
            cmd_args[1] = cmd_args[1].replace("'", '"')
            args = cmd_args[1].split(')')

            cls_name = cls_cmd[0]
            cmd_name = cmd_args[0]

            if cmd_name in commands:
                arg = f"{cmd_name} {cls_name} {args[0].replace(',', '')}"
        return arg


if __name__ == '__main__':
    HBNBCommand().cmdloop()
