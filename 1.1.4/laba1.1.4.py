import matplotlib.pyplot as plt
import seaborn as sns


file = open("1.1.4\data.txt", "r")

def get_arr(raw, q):
    i = 0
    arr = []
    summ = 0
    while(i < len(raw)):
        for j in range(q):
            summ += raw[i]
            i+=1
        arr.append(summ)
        summ = 0
    return arr

raw = []
for line in file:
    raw.append(int(line))
print(len(raw))

from docx import Document

doc = Document()

arr20 = get_arr(raw,20)

# # добавляем пустую таблицу 2х2 ячейки
# table = doc.add_table(rows=21, cols=11)
# table.cell(0, 0).text = "Опыт"
# for i in range(1,11):
#     table.cell(0, int(i)).text = str(i)
# for i in range(1,21):
#     table.cell(int(i), 0).text = str(i*10-10)

# q = 0
# for x in range(1,21):
#     for y in range(1,11):
#         table.cell(x,y).text = str(arr20[q])
#         q+=1

# table.style = 'Light Shading Accent 1'

# doc.save('demo.docx')

# arr80 = get_arr(raw,20)
# mx = max(arr80)

# all = 0

# x = [1]
# for i in range(2,mx+1):
#     x.append(i)
# y = [0] * mx

# for i in range(len(arr80)):
#     if(arr80[i] != 0):
#         y[arr80[i]-1]+=1
#         all+=1

# for i in range(len(y)):
#     y[i] = y[i]/all

# ax = plt.gca()
# #ax.axes.xaxis.set_visible(False)
# vis = []
# # e = [""]
# for i in range(0,mx,10):
#     for j in range(10):
#         vis.append("")
#     vis.append(str(i+10))
# ax.set_xticklabels(vis)
# sns.barplot(x=x, y=y, color='blue')
# plt.xlabel("n") # Подпись оси X
# plt.ylabel("w") # Подпись оси Y
# plt.title('Гистограмма для t = 20') #Название


# plt.show()