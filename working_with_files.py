#Скачайте файл по ссылке
#Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
#Подсчитайте количество слов в тексте
#Замените точки в тексте на восклицательные знаки
#Сохраните результат в файл referat2.txt


with open('referat.txt', 'r', encoding='utf-8') as of:
    content = of.read()
    str_len = len(content)
    count_words = len(content.split())
    dot_repl = content.replace('.', '!')
    paragraph = str('\n')

with open('referat2.txt', 'w', encoding='utf-8') as wf:
    wf.write(str(str_len))

with open('referat2.txt', 'a', encoding='utf-8') as wf:
    wf.write(str(paragraph))
    wf.write(str(count_words))
    wf.write(str(paragraph))
    wf.write(dot_repl)

wf.close()
of.close()




