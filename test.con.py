#!/usr/bin/python3
"""
console module
"""

import cmd
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
"""
class HBNBCommand
"""


def parse(line: str):
    """
    function to split argumets
    """
    arg_list = shlex.split(line)
    return arg_list, len(arg_list)


class HBNBCommand(cmd.Cmd):
    """ declaring methods
    """
    prompt = "(hbnb) "
    lst = ['BaseModel', 'User']

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handle the end of file condition"""
        return True

    def emptyline(self):
        """ an empty line"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints
        the id
        """
        if not arg or arg == " ":
            print("** class name missing **")
        elif arg not in self.lst:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation
        of an instance based on the class
        name and id
        """
        if not arg or arg == " ":
            print("** class name missing **")
        else:
            args = arg.split(' ')
            if args[0] not in self.lst:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Prints the string representation
        of an instance based on the class
        name and id
        """
        if not arg or arg == " ":
            print("** class name missing **")
        else:
            args = arg.split(' ')
            if args[0] not in self.lst:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """
        Prints all string representation
        of all instances based or not on the class name.
        """
        if arg == "":
            lst = []
            for key, val in storage.all().items():
                lst.append(str(val))
                print(lst)
        else:
            args = arg.split(' ')
            if args[0] not in self.lst:
                print("** class doesn't exist **")
            else:
                lst = []
                for key, val in storage.all().items():
                    if type(val).__name__ == args[0]:
                        lst.append(str(val))
                print(lst)

    def do_update(self, args):
        """ update <class name> <id> <attribute name> "<attribute value>"
            Updates an instance based on the class name and id using attr
        """
        args_cd, n = parse(args)
        obj_instance = storage.all()

        if n == 0:
            print("** class name missing **")
        elif n > 0 and args_cd[0] not in self.lst:
            print("** class doesn't exist **")
        elif n == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_cd[0], args_cd[1]) not in obj_instance:
            print("** no instance found **")
        elif n == 2:
            print("** attribute name missing **")
        elif n == 3:
            try:
                type(eval[args_cd[2]]) != dict
            except NameError:
                print("** value missing **")
        elif n == 4:
            obj = obj_instance["{}.{}".format(args_cd[0], args_cd[1])]
            if args_cd[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[args_cd[2]])
                obj.__dict__[args_cd[2]] = val_type(args_cd[3])
            else:
                obj.__dict__[args_cd[2]] = args_cd[3]
        elif type(eval(args_cd[2])) == dict:
            obj = obj_instance["{}.{}".format(args_cd[0], args_cd[1])]
            for k, val in eval(args_cd[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k] in {str, int, float})):
                    val_type = type(obj.__class__.__dict__[k])
                    obj.__dict[k] = val_type(val)
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
