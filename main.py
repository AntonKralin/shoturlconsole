from utils.storage import StorageService


def main():
    st_service = StorageService()

    while (True):
        print('\nПрограмма для сокращения интернет-адрессов')
        print('Введите:')
        print('1 - регистрация короткого интернет-адресса по стандартному')
        print('2 - получение и проверка домашней страницы интернет адреса'
              ' по псевдониму')
        print('3 - получени и проверка стандартного интернет-адресса'
              ' по короткому')
        print('4 - получение всех пар адрессов')
        print('5 - завершение программы')

        choice = int(input('Ваш выбор: '))

        if choice == 1:
            http = input('Введите стандартный url для регистрации: ').lower()
            st_service.append(http)
        elif choice == 2:
            alias = input('Введите псевдоним домашней страницы: ').lower()
            st_service.print_by_alias(alias)
        elif choice == 3:
            shot_url = input('Введите короткий интернет-адресс: ').lower()
            st_service.print_by_short(shot_url)
        elif choice == 4:
            st_service.print_all()
        else:
            break


if __name__ == '__main__':
    main()
