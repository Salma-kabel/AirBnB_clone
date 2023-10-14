#!/usr/bin/python3
"""create a program that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """console for the project"""
    prompt = '(hbnb) '
    file = None

    classes = {'BaseModel': BaseModel, 'User': User,
            'State': State, 'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        exit()

    def emptyline(self):
        """Doesn't execute anything"""
        pass

    def do_create(self, class_name):
        """ Creates a new instance of a class saves it
        (to the JSON file) and prints the id\n"""
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        else:
            cls = classes[class_name]
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, arguments):
        """Prints the string representation of an instance
            based on the class name and id\n"""
        if not args:
            print("** class name missing **")
            return
        args = arguments.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return
        else:
            obj = args[0] + "." + args[1]
            if obj not in storage.all():
                print("** no instance found **")
                return
            else:
                print(storage.all()[obj])

    def do_destroy(self, arguments):
        """Deletes an instance based on the class name and id\n"""
        if not arguments:
            print("** class name missing **")
            return
        args = arguments.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return
        else:
            obj = args[0] + "." + args[1]
            if obj not in storage.all():
                print("** no instance found **")
                return
            else:
                del storage.all()[obj]
                storage.save()

    def do_all(self, arguments):
        """Prints all string representation of all instances
            based or not on the class name\n"""
        args = arguments.split()
        list_of_str = []
        if not args:
            for key in storage.all():
                list_of_str.append(str(storage.all()[key].__str__()))
        else:
            for key in storage.all():
                if isinstance(storage.all()[key], classes[args[0]]):
                    list_of_str.append(str(storage.all()[key].__str__()))
            print(list_of_str)

    def do_update(self, arguments):
        """ Updates an instance based on the class name and id\n"""
        args = arguments.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing ** ")
            return
        obj = args[0] + "." + args[1]
        if obj not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = storage.all()[obj]
        attribute_type = type(getattr(instance, args[2]))
        setattr(instance, args[2], attribute_type(args[3]))
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()