import os

from modules.make_files import get_path
from modules import validator

print("------------------------------ Code Generator ------------------------------------------")
print("Developer....: Pedro Augusto Barbosa Aparecido")
print("Update date..: 21/03/2021 -------- ")
print("")


def initial_choose():
    print("Choose the option: ")
    print("")

    print("[0] - Initial file C")
    print("[1] - Initial file C++")
    print("[2] - Initial file C#")
    print("[3] - Initial file Python")
    print("[4] - Initial file Java")
    print("[5] - Initial file ArduinoScript")
    print("[6] - Initial file SiteFile")
    print("")

    choose = input("> ")

    if choose == "0":
        path = input("Type the path of file: ")
        file_name = input("Type the file name: ")
        if validator.validation_file_name(file_name, '.c'):
            get_path(path=path, file_name=file_name, file_type='c')
        else:
            print("Process error")
            exit(0)
    elif choose == "1":
        path = input("Type the path of file: ")
        file_name = input("Type the file name, but not type extension: ")
        if validator.validation_file_name(file_name, '.cpp'):
            get_path(path=path, file_name=file_name, file_type='cpp')
        else:
            print("Process error")
            exit(0)
    elif choose == "2":
        path = input("Type the path of file: ")
        file_name = input("Type the file name, but not type extension: ")
        if validator.validation_file_name(file_name, '.cs'):
            get_path(path=path, file_name=file_name, file_type='cs')
        else:
            print("Process error")
            exit(0)
    elif choose == "3":
        path = input("Type the path of file: ")
        file_name = input("Type the file name, but not type extension: ")
        if validator.validation_file_name(file_name, '.py'):
            get_path(path=path, file_name=file_name, file_type='py')
        else:
            print("Process error")
            exit(0)
    elif choose == "4":
        path = input("Type the path of file: ")
        file_name = input("Type the file name, but not type extension: ")
        if validator.validation_file_name(file_name, '.java'):
            get_path(path=path, file_name=file_name, file_type='java')
        else:
            print("Process error")
            exit(0)
    elif choose == "5":
        path = input("Type the path of file: ")
        file_name = input("Type the file name, but not type extension: ")
        if validator.validation_file_name(file_name, '.ino'):
            get_path(path=path, file_name=file_name, file_type='ino')
        else:
            print("Process error")
            exit(0)
    elif choose == "6":
        path = input("Type the path of file: ")
        file_name = input("Type the file name, but not type extension: ")
        # if validator.validation_file_name(file_name, '.cpp'):
        get_path(path=path, file_name=file_name, file_type='none type')
        # else:
        #     print("Process error")
        #     exit(0)
    else:
        print("Value typed invalid, you want to choose again? [s/n]")
        i = input("> ").lower()

        if i == 's':
            os.system('cls')
            initial_choose()
        else:
            print("Exiting the code")
            exit(0)


initial_choose()
