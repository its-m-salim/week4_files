# 📂 Python: Работа с файлами / Working with Files / Кор бо файлҳо — 20 задач

# Task 1: Create and Write a File 🟢

## English Description

Create a file `hello.txt` and write one line into it: `Salom, jahon!`

- Use `with open("hello.txt", "w") as f:` and `f.write(...)`.

## Описание задачи (на русском)

Создайте файл `hello.txt` и запишите в него одну строку: `Salom, jahon!`

- Используйте `with open("hello.txt", "w") as f:` и `f.write(...)`.

## Тавсифи масъала (бо тоҷикӣ)

Файли `hello.txt` созед ва ба он як сатр нависед: `Salom, jahon!`

- `with open("hello.txt", "w") as f:` ва `f.write(...)`-ро истифода баред.

### Example:
```
hello.txt (result):
Salom, jahon!
```

---

# Task 2: Read a File 🟢

## English Description

Read the **entire** contents of `notes.txt` with `read()` and print it to the console.

- Open the file in mode `r`.

## Описание задачи (на русском)

Считайте **всё** содержимое файла `notes.txt` методом `read()` и выведите его в консоль.

- Откройте файл в режиме `r`.

## Тавсифи масъала (бо тоҷикӣ)

Мундариҷаи **пурраи** файли `notes.txt`-ро бо усули `read()` хонед ва ба консол чоп кунед.

- Файлро дар реҷаи `r` кушоед.

### Example:
```
notes.txt:
Line one
Line two

Output:
Line one
Line two
```

---

# Task 3: Read Line by Line 🟢

## English Description

Open `notes.txt` and print **each line separately** using a `for` loop over the file object.

- Remove the trailing newline with `.strip()` (or `.rstrip()`).

## Описание задачи (на русском)

Откройте `notes.txt` и выведите **каждую строку отдельно**, используя цикл `for` по объекту файла.

- Убирайте конечный перенос строки с помощью `.strip()` (или `.rstrip()`).

## Тавсифи масъала (бо тоҷикӣ)

Файли `notes.txt`-ро кушоед ва **ҳар сатрро алоҳида** бо ҳалқаи `for` аз рӯи объекти файл чоп кунед.

- Гузариши сатри охирро бо `.strip()` (ё `.rstrip()`) тоза кунед.

### Example:
```
notes.txt:
apple
banana
cherry

Output:
apple
banana
cherry
```

---

# Task 4: Count Lines 🟢

## English Description

Count how many lines are in `notes.txt` and print the number.

- Hint: `readlines()` returns a list of lines.

## Описание задачи (на русском)

Посчитайте, сколько строк в файле `notes.txt`, и выведите число.

- Подсказка: `readlines()` возвращает список строк.

## Тавсифи масъала (бо тоҷикӣ)

Ҳисоб кунед, ки дар файли `notes.txt` чанд сатр аст, ва ададро чоп кунед.

- Маслиҳат: `readlines()` рӯйхати сатрҳоро бармегардонад.

### Example:
```
notes.txt:
apple
banana
cherry

Output:
3
```

---

# Task 5: Append a Line 🟢

## English Description

Open `notes.txt` in **append** mode (`a`) and add a new line `orange` to the end (do not erase the old data).

## Описание задачи (на русском)

Откройте `notes.txt` в режиме **дозаписи** (`a`) и добавьте в конец новую строку `orange` (не стирая старые данные).

## Тавсифи масъала (бо тоҷикӣ)

Файли `notes.txt`-ро дар реҷаи **иловакунӣ** (`a`) кушоед ва ба охири он сатри нави `orange`-ро илова кунед (маълумоти кӯҳнаро нест накунед).

### Example:
```
notes.txt (before):
apple
banana

notes.txt (after):
apple
banana
orange
```

---

# Task 6: Write a List to a File 🟢

## English Description

You have a list of names in your program. Write them to `names.txt`, **each name on its own line**.

- Add `"\n"` after each name (or use `writelines`).

## Описание задачи (на русском)

В программе есть список имён. Запишите их в `names.txt`, **каждое имя на отдельной строке**.

- Добавляйте `"\n"` после каждого имени (или используйте `writelines`).

## Тавсифи масъала (бо тоҷикӣ)

Дар барнома рӯйхати номҳо ҳаст. Онҳоро ба `names.txt` нависед, **ҳар ном дар сатри алоҳида**.

- Пас аз ҳар ном `"\n"` илова кунед (ё `writelines`-ро истифода баред).

### Example:
```
names = ["Ali", "Vali", "Guli"]

names.txt (result):
Ali
Vali
Guli
```

---

# Task 7: Count Words 🟡

## English Description

Read `text.txt` and count the **total number of words**. Words are separated by whitespace.

- Hint: `split()` splits text into a list of words.

## Описание задачи (на русском)

Считайте `text.txt` и посчитайте **общее количество слов**. Слова разделены пробелами.

- Подсказка: `split()` разбивает текст на список слов.

## Тавсифи масъала (бо тоҷикӣ)

Файли `text.txt`-ро хонед ва **шумораи умумии калимаҳоро** ҳисоб кунед. Калимаҳо бо фосила ҷудо шудаанд.

- Маслиҳат: `split()` матнро ба рӯйхати калимаҳо тақсим мекунад.

### Example:
```
text.txt:
the quick brown fox
jumps over

Output:
6
```

---

# Task 8: Count Characters 🟡

## English Description

Read `text.txt` and count the number of characters, **not counting spaces and newlines**.

## Описание задачи (на русском)

Считайте `text.txt` и посчитайте количество символов, **не считая пробелы и переносы строк**.

## Тавсифи масъала (бо тоҷикӣ)

Файли `text.txt`-ро хонед ва шумораи аломатҳоро ҳисоб кунед, **бе ҳисоб кардани фосилаҳо ва гузаришҳои сатр**.

### Example:
```
text.txt:
abc def

Output:
6
```

---

# Task 9: Sum of Numbers 🟡

## English Description

The file `numbers.txt` has one integer per line. Read them, add them together, and print the **total**.

- Convert each line to a number with `int()`.

## Описание задачи (на русском)

В файле `numbers.txt` записано по одному целому числу в строке. Считайте их, сложите и выведите **сумму**.

- Преобразуйте каждую строку в число через `int()`.

## Тавсифи масъала (бо тоҷикӣ)

Дар файли `numbers.txt` дар ҳар сатр як адади бутун аст. Онҳоро хонед, ҷамъ кунед ва **суммаро** чоп кунед.

- Ҳар сатрро бо `int()` ба адад табдил диҳед.

### Example:
```
numbers.txt:
10
20
30

Output:
60
```

---

# Task 10: Largest Number 🟡

## English Description

The file `numbers.txt` has one integer per line. Read them and print the **largest** one.

## Описание задачи (на русском)

В файле `numbers.txt` по одному целому числу в строке. Считайте их и выведите **наибольшее**.

## Тавсифи масъала (бо тоҷикӣ)

Дар файли `numbers.txt` дар ҳар сатр як адади бутун аст. Онҳоро хонед ва **калонтаринро** чоп кунед.

### Example:
```
numbers.txt:
7
2
9
4

Output:
9
```

---

# Task 11: Copy a File 🟡

## English Description

Read all contents of `source.txt` and write them into a new file `copy.txt`.

## Описание задачи (на русском)

Считайте всё содержимое `source.txt` и запишите его в новый файл `copy.txt`.

## Тавсифи масъала (бо тоҷикӣ)

Тамоми мундариҷаи `source.txt`-ро хонед ва онро ба файли нави `copy.txt` нависед.

### Example:
```
source.txt:
Hello
World

copy.txt (result):
Hello
World
```

---

# Task 12: Numbered Lines 🟡

## English Description

Read `notes.txt` and print each line with its **line number** in the format `<n>: <line>`.

- Hint: `enumerate(..., start=1)` gives you the number and the line.

## Описание задачи (на русском)

Считайте `notes.txt` и выведите каждую строку с её **номером** в формате `<n>: <строка>`.

- Подсказка: `enumerate(..., start=1)` даёт номер и строку.

## Тавсифи масъала (бо тоҷикӣ)

Файли `notes.txt`-ро хонед ва ҳар сатрро бо **рақами** он дар формати `<n>: <сатр>` чоп кунед.

- Маслиҳат: `enumerate(..., start=1)` рақам ва сатрро медиҳад.

### Example:
```
notes.txt:
apple
banana
cherry

Output:
1: apple
2: banana
3: cherry
```

---

# Task 13: Count a Word 🟡

## English Description

Read `text.txt` and count **how many times the word `python`** appears (among the words).

- Hint: split the text into words, then use `.count("python")`.

## Описание задачи (на русском)

Считайте `text.txt` и посчитайте, **сколько раз встречается слово `python`** (среди слов).

- Подсказка: разбейте текст на слова, затем `.count("python")`.

## Тавсифи масъала (бо тоҷикӣ)

Файли `text.txt`-ро хонед ва ҳисоб кунед, ки **калимаи `python` чанд маротиба** вомехӯрад (дар байни калимаҳо).

- Маслиҳат: матнро ба калимаҳо тақсим кунед, баъд `.count("python")`.

### Example:
```
text.txt:
python is fun
i love python
python python

Output:
4
```

---

# Task 14: Longest Line 🟡

## English Description

Read `text.txt` and print the **longest line** (the one with the most characters).

- Hint: `max(lines, key=len)`.

## Описание задачи (на русском)

Считайте `text.txt` и выведите **самую длинную строку** (с наибольшим числом символов).

- Подсказка: `max(lines, key=len)`.

## Тавсифи масъала (бо тоҷикӣ)

Файли `text.txt`-ро хонед ва **сатри дарозтаринро** (бо бештарин аломатҳо) чоп кунед.

- Маслиҳат: `max(lines, key=len)`.

### Example:
```
text.txt:
short
a longer line here
mid

Output:
a longer line here
```

---

# Task 15: Uppercase to a New File 🟡

## English Description

Read `text.txt`, convert **all text to uppercase**, and save the result to a new file `upper.txt`.

- Hint: `.upper()`.

## Описание задачи (на русском)

Считайте `text.txt`, переведите **весь текст в верхний регистр** и сохраните результат в новый файл `upper.txt`.

- Подсказка: `.upper()`.

## Тавсифи масъала (бо тоҷикӣ)

Файли `text.txt`-ро хонед, **тамоми матнро ба ҳарфҳои калон** табдил диҳед ва натиҷаро ба файли нави `upper.txt` сабт кунед.

- Маслиҳат: `.upper()`.

### Example:
```
text.txt:
hello world

upper.txt (result):
HELLO WORLD
```

---

# Task 16: Remove Empty Lines 🟡

## English Description

Read `text.txt`, **remove the empty (blank) lines**, and save the result to `clean.txt`.

- A line is empty if, after `.strip()`, it becomes `""`.

## Описание задачи (на русском)

Считайте `text.txt`, **удалите пустые строки** и сохраните результат в `clean.txt`.

- Строка пустая, если после `.strip()` она равна `""`.

## Тавсифи масъала (бо тоҷикӣ)

Файли `text.txt`-ро хонед, **сатрҳои холиро нест кунед** ва натиҷаро ба `clean.txt` сабт кунед.

- Сатр холӣ аст, агар пас аз `.strip()` он ба `""` баробар шавад.

### Example:
```
text.txt:
apple

banana

cherry

clean.txt (result):
apple
banana
cherry
```

---

# Task 17: Merge Two Files 🔴

## English Description

Read `file1.txt` and `file2.txt` and write all their lines into a new file `merged.txt` — first the lines of `file1`, then the lines of `file2`.

## Описание задачи (на русском)

Считайте `file1.txt` и `file2.txt` и запишите все их строки в новый файл `merged.txt` — сначала строки `file1`, затем строки `file2`.

## Тавсифи масъала (бо тоҷикӣ)

Файлҳои `file1.txt` ва `file2.txt`-ро хонед ва тамоми сатрҳои онҳоро ба файли нави `merged.txt` нависед — аввал сатрҳои `file1`, баъд сатрҳои `file2`.

### Example:
```
file1.txt:
A
B

file2.txt:
C
D

merged.txt (result):
A
B
C
D
```

---

# Task 18: Top Student 🔴

## English Description

The file `scores.txt` has lines in the format `name score` (separated by a space). Read them, compute the **average score** (rounded to 2 decimals), and print the **name of the student with the highest score**.

- Hint: `name, score = line.split()`, then `score = int(score)`.

## Описание задачи (на русском)

В файле `scores.txt` строки в формате `имя балл` (через пробел). Считайте их, вычислите **средний балл** (округлённый до 2 знаков) и выведите **имя студента с наибольшим баллом**.

- Подсказка: `name, score = line.split()`, затем `score = int(score)`.

## Тавсифи масъала (бо тоҷикӣ)

Дар файли `scores.txt` сатрҳо дар формати `ном хол` (бо фосила) ҳастанд. Онҳоро хонед, **холи миёнаро** (то 2 рақами баъди вергул) ҳисоб кунед ва **номи донишҷӯи дорои холи баландтаринро** чоп кунед.

- Маслиҳат: `name, score = line.split()`, баъд `score = int(score)`.

### Example:
```
scores.txt:
Ali 80
Vali 95
Guli 88

Output:
Average: 87.67
Top: Vali
```

---

# Task 19: Word Frequency 🔴

## English Description

Read `text.txt`, count **how many times each word appears**, and write the results to `freq.txt`, one `word: count` per line (keep the order in which words first appear).

- Hint: use a dictionary, e.g. `counts[word] = counts.get(word, 0) + 1`.

## Описание задачи (на русском)

Считайте `text.txt`, посчитайте, **сколько раз встречается каждое слово**, и запишите результаты в `freq.txt` — по одной строке `слово: количество` (сохраняя порядок первого появления слов).

- Подсказка: используйте словарь, например `counts[word] = counts.get(word, 0) + 1`.

## Тавсифи масъала (бо тоҷикӣ)

Файли `text.txt`-ро хонед, ҳисоб кунед, ки **ҳар калима чанд маротиба** вомехӯрад, ва натиҷаҳоро ба `freq.txt` нависед — дар ҳар сатр `калима: шумора` (тартиби аввалин пайдошавии калимаҳоро нигоҳ доред).

- Маслиҳат: луғатро (dictionary) истифода баред, масалан `counts[word] = counts.get(word, 0) + 1`.

### Example:
```
text.txt:
apple banana apple
cherry apple banana

freq.txt (result):
apple: 3
banana: 2
cherry: 1
```

---

# Task 20: Contacts (OOP + Files) 🔴

## English Description

Create a class `Contact` with fields `name` and `phone`. Read contacts from `contacts.txt` (each line in the format `name,phone`) into a list of `Contact` objects, add a new contact `Sara,555-1234`, and save **all** contacts back to `contacts.txt`.

- Hint: `name, phone = line.strip().split(",")`.

## Описание задачи (на русском)

Создайте класс `Contact` с полями `name` и `phone`. Считайте контакты из `contacts.txt` (каждая строка в формате `имя,телефон`) в список объектов `Contact`, добавьте новый контакт `Sara,555-1234` и сохраните **все** контакты обратно в `contacts.txt`.

- Подсказка: `name, phone = line.strip().split(",")`.

## Тавсифи масъала (бо тоҷикӣ)

Синфи `Contact`-ро бо майдонҳои `name` ва `phone` созед. Тамосҳоро аз `contacts.txt` (ҳар сатр дар формати `ном,телефон`) ба рӯйхати объектҳои `Contact` хонед, тамоси нави `Sara,555-1234`-ро илова кунед ва **ҳамаи** тамосҳоро дубора ба `contacts.txt` сабт кунед.

- Маслиҳат: `name, phone = line.strip().split(",")`.

### Example:
```
contacts.txt (before):
Ali,111-2222
Vali,333-4444

contacts.txt (after):
Ali,111-2222
Vali,333-4444
Sara,555-1234
```
