#!/usr/bin/python3
"""
console module
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
"""
class HBNBCommand
"""


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
            if args[0] not in storage.all_cls():
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

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)
        """
        if not arg or arg == " ":
            print("** class name missing **")
        else:
            args = arg.split(" ")
            ky = "{}.{}".format(args[0], args[1])
            if args[0] not in self.lst:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif ky not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                if args[3][0] == '"' and args[3][-1] == '"':
                    args[3] = args[3][1:-1]
            for key, val in storage.all().items():
                if ky == key:
                    setattr(storage.all()[key], args[2], args[3])
                    storage.all()[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
