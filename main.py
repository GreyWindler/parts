from os import listdir
import os.path

def search_file(drc, squery):
    with open(drc) as f:
        for line in f:
            if squery in line:
                print(drc)
                return drc


def search(dirs):
    print('Введите искомую строку')
    squery = input()

    new_dirs = []
    for drc in dirs:
        new_drc = search_file(drc, squery)
        if new_drc:
            new_dirs.append(new_drc)
    return new_dirs


if __name__ == '__main__':
    dirs = [os.path('Migrations', d) for d in listdir('Migrations') if os.path.splitext(d)[-1] == '.sql']
    while True:
        dirs = search(dirs)
        print('Всего найдено: %s' % len(dirs))
        
