1
# with open("hello.txt", "w") as file:
#     file.write("Salom, Jahon!")


2
# with open("notes.txt", "r") as file:
#     print(file.read())

3
# with open("notes.txt", "w") as file:
#     file.writelines(["apple\n", "banana\n", "cherry\n"])
# with open("notes.txt", "r") as file:
#     for i in file:
#         print(i.rstrip())

4
# with open("notes.txt", "r") as file:
#     lines = file.readlines()
#     print(len(lines))


def read():
    with open("notes.txt", "r") as file:
        for i in file:
            print(i.strip())

5
# with open("notes.txt", "w") as file:
#     file.writelines(["apple\n", "banana\n"])
# with open("notes.txt", "a") as file:
#     file.write("orange")
# read()

6
# names = ["Ali", "Vali", "Guli"]
# with open("notes.txt", "w") as file:
#     for i in names:
#         file.write(f"{i}\n")
    
# read()


7
# with open("notes.txt", "r") as file:
#     l = file.read().split()
#     print(len(l))


8
# with open("notes.txt", "r") as file:
#     a = file.read().replace(" ", "").strip()
#     print(len(a))

9
# with open("notes.txt", "r") as file:
#     tot = 0
#     for i in file:
#         tot += int(i.strip())
#     print(tot)

10
# with open("notes.txt", "r") as file:
#     f = file.read().split()
#     b = [int(i) for i in f]
#     print(max(b))

import shutil
11
# shutil.copy("notes.txt", "hello.txt")

12
# with open("notes.txt", "r") as file:
#     f = file.readlines()
#     for index, item in enumerate(f, start=1):
#         print(f"{index}: {item.strip()}")

13
# with open("text.txt") as file:
#     f = file.read().split()
#     print(f.count("python"))

14
# with open("text.txt") as file:
#     f = file.readlines()
#     print(max(f, key=len))

15
# with open("text.txt") as file:
#     upp = file.read()

# with open("upper.txt", "w") as file:
#     file.write(upp.upper())

16
# with open("text.txt") as file:
#     new = []
#     f = file.readlines()
#     for line in f:
#         if not line.strip() == "":
#            new.append(line)

# with open("clean.txt", "w") as file:
#     file.writelines(new) 

17
# with open("upper.txt") as file:
#     file1 = file.readlines()

# with open("clean.txt") as file:
#     file2 = file.readlines()

# with open("merged.txt", "w") as file:
#     file.writelines(file1)
#     file.writelines(file2)

18
# with open("scores.txt") as file:
#     f = file.readlines()
#     k = [i.split() for i in f]
#     tot =0
#     for i in k:
#         tot += int(i[1]) 
#     sorted_students = sorted(k, key=lambda s: int(s[1]), reverse=True)
#     print(f"Average: {tot/ len(k):.2f}")
#     print(f"Top: {sorted_students[0][0]}")


19
# with open("notes.txt") as file:
#     f = file.read().strip().split()
#     freq = {}
#     for i in f:
#         freq[i] = f.count(i)
#     print(freq)

# with open("freq.txt", "w") as file:
#     for k,v in freq.items():
#         file.write(f"{k}: {v}\n")

20
# class Contact:

#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone


# contacts = []
# with open("contacts.txt") as file:
#     lines = file.readlines()
#     for line in lines:
#         name , phone = line.strip().split(",")
#         contacts.append(Contact(name, phone))

# contacts.append(Contact("Sara", "555-1234"))
# with open("contacts.txt", "w") as file:
#     for i in contacts:
#         file.write(f"{i.name},{i.phone}\n")