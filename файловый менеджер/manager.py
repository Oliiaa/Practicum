import os
import sys
import shutil
import settings


path = ""
settings.start()


def help():
    print("Показать все команды, атрибуты: сама команда - help \n"
          "Узнать текущее местонахождение, атрибуты: сама команда - current_directory \n"
          "Создание папки, атрибуты: сама команда, имя папки - create_directory \n"
          "Удаление папки по имени, атрибуты: сама команда, имя папки - delete_dir \n"
          "Создание пустого текстового файла, атрибуты: сама команда, имя файла - make_file \n"
          "Записать текст в файл, атрибуты: сама команда, имя файла - write_file \n"
          "Посмотреть содержимое файла, атрибуты: сама команда, имя файла - read_file \n"
          "Удаление файла по имени, атрибуты: сама команда, имя файла - delete_file \n"
          "Скопировать файл, атрибуты: сама команда, имя файла, путь - copy_file \n"
          "Переместить файл, атрибуты: сама команда, имя файла, путь - move_file \n"
          "Переимновать файл, атрибуты: сама команда, первое имя, второе имя - rename_file \n"
          "Спустить в директории на один уровень ниже, атрибуты: сама команда, имя директроии - change_directory \n"
          "Подняться в директории на один уровень выше, атрибуты: сама команда - change_dirr_up \n"
          "Выход из программы, атрибуты: сама команда - exit ")


def current_directory():
    print(os.getcwd())


def create_directory(dirName):
    try:
        os.mkdir(dirName)
    except FileExistsError:
        print('Директория уже существует')


def delete_dir(dirName):
    try:
        os.rmdir(dirName)
    except FileNotFoundError:
        print('Директория не существует')


def make_file(fileName):
    file = open(fileName, "w+")
    file.close()


def write_file(filename, w):
    try:
        f = open(filename, "a")
        f.write(w)
        f.close()
    except FileExistsError:
        print('Файл не существует')


def read_file(fileName):
    try:
        file = open(fileName, "r")
        print(file.read())
        file.close()
    except FileExistsError:
        print('Файл не существует')


def delete_file(fileName):
    try:
        os.remove(fileName)
    except FileExistsError:
        print('Файл не существует')


def copy_file(fileName, newFilename):
    try:
        shutil.copy(fileName, newFilename)
    except FileExistsError:
        print('Файл не существует')


def move_file(fileName, path_n):
    try:
        shutil.move(fileName, path+path_n)
    except FileExistsError:
        print('Файл не существует')


def rename_file(fileName, newFilename):
    try:
        os.rename(fileName, newFilename)
    except FileExistsError:
        print('Файл не существует')


def change_directory(dirName):
    try:
        OS = sys.platform
        if OS == 'darwin':
            a = os.getcwd()
            os.chdir(a + '/' + dirName)
            print(os.getcwd())

        elif OS == 'cygwin' or OS == 'win32':
            a = os.getcwd()
            os.chdir(a + '\\' + dirName)
            print(os.getcwd())
    except FileNotFoundError:
        print('Директория не существует')


def change_dirr_up():
    try:
        z = os.getcwd()
        if len(os.path.split(os.getcwd())[0]) < len(path):
            print('Выход за пределы рабочей папки')
        elif len(os.path.split(os.getcwd())[0]) <= len(z) or len(os.path.split(os.getcwd())[0]) + 1 <= len(z):
            OS = sys.platform
            # print(OS)
            if OS == 'darwin':
                a = os.getcwd()
                b = a.split('/')
                del b[-1]
                a = '/'.join([str(item) for item in b])
                os.chdir(a)
                print(os.getcwd())

            elif OS == 'cygwin' or OS == 'win32':
                a = os.getcwd()
                b = a.split('\\')
                del b[-1]
                a = '\\'.join([str(item) for item in b])
                os.chdir(a)
                print(os.getcwd())
        else:
            print("Невозможно перейти в директорию")
            print(os.getcwd())
    except:
        print('Ошибка. Невозможно перейти в директорию')


print("Добро пожаловать в демо файловый менеджер")
while True:
    try:
        command = input('Введите команду (по умолчанию, если нажать ENTER - help): ')
        command = command.split(' ')
        if command[0] == 'exit':
            break
        elif command[0] == 'help' or command[0] == '':
            help()
        elif command[0] == 'create_directory':
            create_directory(command[1])
        elif command[0] == 'delete_dir':
            delete_dir(command[1])
        elif command[0] == 'make_file':
            make_file(command[1])
        elif command[0] == 'read_file':
            read_file(command[1])
        elif command[0] == 'write_file':
            contentWrap = input("Текст: ")
            write_file(command[1], contentWrap)
        elif command[0] == 'current_directory':
            current_directory()
        elif command[0] == 'delete_file':
            delete_file(command[1])
        elif command[0] == 'copy_file':
            copy_file(command[1], command[2])
        elif command[0] == 'move_file':
            move_file(command[1], command[2])
        elif command[0] == 'rename_file':
            rename_file(command[1], command[2])
        elif command[0] == 'change_directory':
            change_directory(command[1])
        elif command[0] == 'change_dirr_up':
            change_dirr_up()
        else:
            print('команды не существует')
    except:
        print('Команда введена неправильно')
