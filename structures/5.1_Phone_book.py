def processing_queries(queries_list):
    phone_book = [''] * 10000000  # Таблица с индексацией

    for query in queries_list:
        command, number, *name = query
        number = int(number)
        if command == 'add':
            phone_book[number] = name[0]
        if command == 'del':
            phone_book[number] = ''
        if command == 'find':
            print('not found') if phone_book[number] == '' else print(phone_book[number])


def main():
    n = int(input())
    queries_list = [input().split() for _ in range(n)]
    print(queries_list)

    processing_queries(queries_list)


if __name__ == "__main__":
    main()