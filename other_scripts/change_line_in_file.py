# with open('test.txt', 'r') as file:
#     lines = file.readlines()
#     lines2 = []
#     for line in lines:
#
#         if line.rfind('content') != -1:
#             line = '     content = new_key_222\n'
#         lines2.append(line)
#
# with open('test2.txt', 'w') as file2:
#     file2.writelines(lines2)


with open('test.txt', 'r') as file, open('test2.txt', 'w') as file2:
    lines = file.readlines()
    lines2 = []
    for line in lines:

        if line.rfind('content') != -1:
            line = '     content = new_key_222\n'
        lines2.append(line)
    file2.writelines(lines2)


# source_file = 'test.txt'
# target_file = 'test2.txt'
# shablon = 'content'
# replace = 'content = new_key\n'
#
#
# def change_line(source_file, target_file, shablon, replace):
#     with open(source_file, 'r') as file:
#         lines = file.readlines()
#         lines2 = []
#         for line in lines:
#             if line.rfind(shablon) != -1:
#                 line = replace
#             lines2.append(line)
#
#     with open(target_file, 'w') as file2:
#         file2.writelines(lines2)
