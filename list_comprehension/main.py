file1_list = []
file2_list = []

with open("file1.txt") as fp:
    file1_content = fp.readlines()
    for file in file1_content:
        file = int(file.strip())
        file1_list.append(file)

with open("file2.txt") as fp:
    file2_content = fp.readlines()
    for file in file2_content:
        file = int(file.strip())
        file2_list.append(file)

result = [number for number in file1_list if number in file2_list]
print(result)

