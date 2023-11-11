#!/usr/bin/python3
"""
console module
"""

import cmd

"""
class HBNBCommand
"""


class HBNBCommand(cmd.Cmd):
    """ declaring methods
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handle the end of file condition"""
        return True

    def emptyline(self):
        """ an empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
