import scipy.io
import numpy as np
import csv

# initial settings
root = "C:\Users\Tulakan\Documents\Python Scripts\\"
data = scipy.io.loadmat(root+"2Moons.mat")

# get data from .mat file
for i in data:
    if i == "x":
        x = data[i]
        xShape = np.shape(x)
    if i == "y":
        y = data[i]
        yShape = np.shape(y)
    if i == "xt":
        xt = data[i]
        xtShape = np.shape(xt)
    if i == "yt":
        yt = data[i]
        ytShape = np.shape(yt)

# preparing desired data to be written
xy = np.insert(x, 2, np.reshape(y,(1,max(yShape))), axis=1)
xtyt = np.insert(xt, 2, np.reshape(yt,(1,max(ytShape))), axis=1)

# write to csv files
with open(root+"converted/"+'xy.csv', 'w') as csvfile:
    fieldnames = ['X1', 'X2', 'Y']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    for i in xy:
        writer.writerow({'X1': i[0], 'X2': i[1], 'Y': i[2]})

with open(root+"converted/"+'xtyt.csv', 'w') as csvfile:
    fieldnames = ['XT1', 'XT2', 'YT']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    for i in xtyt:
        writer.writerow({'XT1': i[0], 'XT2': i[1], 'YT': i[2]})

# deprecated
# np.savetxt((root+"filesforyou/"+"xy.csv"),xy,delimiter=',')
# np.savetxt((root+"filesforyou/"+"xtyt.csv"),xtyt,delimiter=',')
