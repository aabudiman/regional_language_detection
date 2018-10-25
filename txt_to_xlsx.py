import xlsxwriter

jawa = []
sunda = []
indonesia = []

tweets = []

workbook = xlsxwriter.Workbook('dataset.xlsx')
worksheet = workbook.add_worksheet()

with open('jawa.txt', 'rt') as jw:
    for line in jw:
        jawa.append(jw.readline().split('/'))

with open('sunda.txt', 'rt') as sd:
    for line in sd:
        sunda.append(sd.readline().split('/'))

with open('indonesia.txt', 'rt') as id:
    for line in id:
        indonesia.append(id.readline().split('/'))

for line in jawa + sunda + indonesia:
    if (len(line) == 2):
        words = line[0]
        etnik = line[1].replace("\n", "")
        tweets.append((words, etnik))

def write():
    worksheet.write(0, 0, "word")
    worksheet.write(0, 1, "label")
    row = 1
    col = 0
    for words, label in (tweets):
        worksheet.write(row, col, words)
        worksheet.write(row, col + 1, label)
        row += 1

write()
workbook.close()

