
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    content = read_file('referat.txt')

    str_len = len(content)
    print(f'Длина строки - {str_len}')

    count_words = len(content.split())
    print(f'Количество слов - {count_words}')

    dot_repl = content.replace('.', '!')
    write_file('change_referat.txt', dot_repl)

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as wf:
        wf.write(content)


if __name__ == '__main__':
    main()



