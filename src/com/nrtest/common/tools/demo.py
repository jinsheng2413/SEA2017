import os


def fileg(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            if fullpath.endswith('py') and '__init__' not in fullpath:
                op = fullpath.split('\\')
                name = op[len(op) - 1]
                lis = []
                with open(fullpath, 'r', encoding='utf-8') as file:
                    lis = file.readlines()
                    for item in lis:
                        if '@file' in item:
                            f = item.replace(' ', '')
                            l = f.split(':')
                            fname = l[1]
                if name in fname:
                    pass
                else:
                    lis[line(lis)] = '@file: ' + name + '\n'
                    with open(fullpath, 'w', encoding='utf-8') as n_file:
                        n_file.writelines(lis)
                    lis.clear()


def line(lis):
    for i, item in enumerate(lis):
        if '@file' in item:
            return int(i)


if __name__ == '__main__':
    fileg(r'D:\pythonworkspace\SEA2017\src\com\nrtest\sea\testcase\stat_rey\workQuery')
