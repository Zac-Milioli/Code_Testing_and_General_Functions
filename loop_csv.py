import os

os.chdir(r'C:\Users\zacmi_vekn7n0\PycharmProjects\Prática\csv_file_testing')
# for file in os.listdir():
#     print(file)

csvs = []

# csv names loop
for i in os.listdir():
    csvs.append(i)

periods = []

# year separation loop
for i in os.listdir():
    i = i.split('.')
    i = i[0].split('_')
    if i[-1] not in periods:
        periods.append(i[-1])


print({'file': csvs, 'period': periods})
