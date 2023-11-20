#!/usr/bin/python3
"""module for cmd funtion"""
import cmd
import shlex
import re
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


def parse(line: str):
    """
    function to split argumets
    """
    arg_list = shlex.split(line)
    return arg_list, len(arg_list)


class HBNBCommand(cmd.Cmd):
    """ Defines the Command interpreter
    Attributes (str): The command prompt
    """
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def do_EOF(self, line):
        """ EOF command to exit the program """
        print("")
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ Print an empty line"""
        pass

    def do_create(self, args):
        """ Usage: create <class>
            crates a new calss instance and print its id
        """
        command_args, args_len = parse(args)

        if args_len == 0:
            print("** class name missing **")
        elif command_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            in_base = eval(command_args[0])().id
            print(in_base)
            storage.save()

    def do_show(self, args):
        """ Usage: show <class> <id>
        Print string representation of a class instanceof an  id
        """
        obj_instance = storage.all()
        show_args, show_len = parse(args)

        if show_len == 0:
            print("** class name missing **")
        elif show_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif show_len == 1:
            print("** instance id missing **")
        elif "{}.{}".format(show_args[0], show_args[1]) not in obj_instance:
            print("** no instance found **")
        else:
            print(obj_instance["{}.{}".format(show_args[0], show_args[1])])

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

    def do_all(self, args):
        """ Usage: all <class> or all
            Prints all string representation of all instances
            based or not on the class name
        """
        args_cd, n = parse(args);

        if n > 0 and args_cd[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(args_cd) > 0 and args_cd[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif n == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, args):
        """ update <class name> <id> <attribute name> "<attribute value>"
            Updates an instance based on the class name and id using attr
        """
        args_cd, n = parse(args)
        obj_instance = storage.all()

        if n == 0:
            print("** class name missing **")
        elif n > 0 and args_cd[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif n == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_cd[0], args_cd[1]) not in obj_instance:
            print("** no instance found **")
        elif n == 2:
            print("** attribute name missing **")
        elif n == 3:
            try:
                type(eval(args_cd[2])) != dict
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

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl, n = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
