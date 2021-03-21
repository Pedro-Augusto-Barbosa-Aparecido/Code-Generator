def c_creator(file):
    """

    #include <stdio.h>

    int main() {

        printf("Hello Word");

        return 0;

    }

    :param file:
    :return:
    """
    file = open(file, 'w')
    file.write("#include <stdio.h>")
    file.write("\nint main() {")
    file.write("\n")
    file.write('\n    printf("Hello Word");')
    file.write("\n    return 0;")
    file.write("\n}")

    file.close()


def cpp_creator(file):
    """

    #include <iostream>

    using namespace std;

    int main() {

        cout << "Hello Word" << endl;

        return 0;

    }

    :param file:
    :return:
    """
    file = open(file, 'w')
    file.write("#include <iostream>")
    file.write("\n")
    file.write("using namespace std;")
    file.write("\n")
    file.write("\nint main() {")
    file.write("\n")
    file.write('\n    cout << "Hello Word" << endl;')
    file.write("\n    return 0;")
    file.write("\n}")

    file.close()


def cs_creator(file):
    """

    using System;

    class HelloWord {

        static void Main() {

            Console.Write("Hello Word!!!!");

        }

    }

    :param file:
    :return:
    """
    file = open(file, 'w')
    file.write("using System")
    file.write("\n")
    file.write("\nclass HelloWord {")
    file.write("\n")
    file.write("\n  static void Main() {")
    file.write("\n")
    file.write('\n      Console.Write("Hello Word!!!");')
    file.write("\n  }")
    file.write("\n}")

    file.close()


def py_creator(file):
    """
    import os

    os.system('cls')

    print("Hello Word!!!")

    :param file:
    :return:
    """
    file = open(file, 'w')
    file.write("import os")
    file.write("\n")
    file.write("os.system('cls')")
    file.write("\n")
    file.write("\nprint('Hello Word')")
    file.write("\n")

    file.close()


def java_creator(file):
    """
    public class HelloWord {
        public static void main(String[] args) {
            System.out.println("Hello Word!!");
        }
    }
    :param file:
    :return:
    """
    file = open(file, 'w')
    file.write("public class HelloWord {\n")
    file.write("    public static void main(String[] args) {\n")
    file.write('        System.out.println("Hello Word!!);\n')
    file.write("    }\n")
    file.write("}\n")

    file.close()


def ino_creator(file):
    """
    void setup() {
        Serial.begin(9600);
        Serial.println("Hello Word");
    }

    void loop(){

    }
    :param file:
    :return:
    """
    file = open(file, 'w')
    file.write("void setup() {\n")
    file.write("    Serial.begin(9600);\n")
    file.write('    Serial.println("Hello Word);\n')
    file.write("}\n")
    file.write("\n")
    file.write("void loop() {\n")
    file.write('\n')
    file.write("}\n")

    file.close()


def site_files_creator(file):
    # file = open(file, 'w')
    # file.write("#include <iostream>")
    # file.write("\n")
    # file.write("using namespace std;")
    # file.write("\n")
    # file.write("\nint main() {")
    # file.write("\n")
    # file.write('\n    cout << "Hello Word" << endl;')
    # file.write("\n    return 0;")
    # file.write("\n}")
    #
    # file.close()
    print("Coming...")


def get_path(path, file_name, file_type):
    _path = path + '\\' + file_name + '.' + file_type

    if file_type == 'c':
        c_creator(file=_path)
    elif file_type == "cpp":
        cpp_creator(_path)
    elif file_type == "cs":
        cs_creator(_path)
    elif file_type == "py":
        py_creator(_path)
    elif file_type == "java":
        java_creator(_path)
    elif file_type == "ino":
        ino_creator(_path)
    elif file_type == "none type":
        site_files_creator(_path)

    else:
        print("File extension invalid!!!!")
        exit(0)


if __name__ == '__main__':
    pass
