import csv
import matplotlib.pyplot as plot

plot.plot

list = []

with open('nfcap.csv') as data:
    reader = csv.reader(data)
    for i in reader:
        list.append(i)

ibyte = 0
cost = 0
x_duration = []          #время трафика
y_amount = []            #объем трафика

for i in range(len(list)):
    if '192.168.250.27' in list[i]:
        ibyte += float(list[i][12])
        x_duration.append(float(list[i][11]))
        y_amount.append(float(list[i][12]))

ibyte = ibyte/(2**20)
cost = ibyte*1
print("%.2f" % cost)

x_duration.sort()
y_amount.sort()
assert len(x_duration) == len(y_amount)
plot.plot(x_duration,y_amount)
plot.grid(True)
plot.show()