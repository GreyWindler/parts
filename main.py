from os import listdir


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
    found_num = 0
    for drc in dirs:
        new_drc = search_file(drc, squery)
        if new_drc:
            found_num += 1
            new_dirs.append(new_drc)
    return new_dirs, found_num


if __name__ == '__main__':
    dirs = ['\\'.join(['Migrations', d]) for d in listdir('Migrations') if d[-4:] == '.sql']
    while True:
        dirs, found_num = search(dirs)
        print('Всего найдено: ', found_num)
