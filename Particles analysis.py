%reset -f
import numpy as np
import pandas as pd
import files
import matplotlib.pyplot as plt

DepFile = pd.read_csv("simulated_microturbine_data.csv")
#print(DepFile.head())
increment1 = 25   #sampling frame size
increment2 = 50
density = 1.225
lenfine = increment1*11 #the maximum of a sampling area
lencoarse = increment2*130
tablempat = np.empty((len(DepFile),1))
tablempat2 = np.empty((len(DepFile),1))
xlocpattern = []
xlocmaxpattern = []
ylocmaxpattern = []
zlocmaxpattern = []
strip_count = 0
masspattern = []
#----------------------------

increment1 = int(input('Enter the width of the strips to process data: '))
amount1 = int(input('Enter the amount of strips: '))
lenfine = increment1*amount1

for a in range(increment1, lenfine + increment1, increment1):
  mask1 = (DepFile.iloc[:, 0] > (a - increment1) / 1000) & (DepFile.iloc[:, 0] <= a / 1000)

  tablempat[:, 0] = (DepFile.iloc[:, 3] * DepFile.iloc[:, 4]) * mask1.to_numpy()
  column_sums = np.sum(tablempat, axis=0, dtype=np.float64)

  x_masked = np.where(mask1.to_numpy(), DepFile.iloc[:, 0].astype(float), -np.inf)
  y_masked = np.where(mask1.to_numpy(), DepFile.iloc[:, 1].astype(float), -np.inf)
  z_masked = np.where(mask1.to_numpy(), DepFile.iloc[:, 2].astype(float), -np.inf) #assignes everything outside the boundaries as negative infinity

  masspattern.append(column_sums)
  xlocpattern.append(a - increment1 + (increment1 / 2)) # the mid point of a strip

  xlocmaxpattern.append(np.max(x_masked)) # the maximum point within the strip
  ylocmaxpattern.append(np.max(y_masked))
  zlocmaxpattern.append(np.max(y_masked))

#negative direction-----------------
  mask2 = (DepFile.iloc[:, 0] < (-a + increment1) / 1000) & (DepFile.iloc[:, 0] >= -a / 1000)
  tablempat2[:, 0] = (DepFile.iloc[:, 3] * DepFile.iloc[:, 4]) * mask2.to_numpy()

  column_sums = np.sum(tablempat2, axis=0, dtype=np.float64)
  masspattern.append(column_sums)
  xlocpattern.append(-a + increment1 - (increment1 / 2))

  x_masked = np.where(mask2.to_numpy(), DepFile.iloc[:, 0].astype(float), -np.inf)
  y_masked = np.where(mask2.to_numpy(), DepFile.iloc[:, 1].astype(float), -np.inf)
  z_masked = np.where(mask2.to_numpy(), DepFile.iloc[:, 2].astype(float), -np.inf)

  xlocmaxpattern.append(np.max(x_masked))
  ylocmaxpattern.append(np.max(y_masked))
  zlocmaxpattern.append(np.max(y_masked))

increment2 = int(input('Enter a different width of the strips to process data: '))
amount2 = int(input('Enter the amount of these strips: '))
lencoarse = increment2*amount2


#bigger strips------------------------------------------------------------------------
for a in range(lenfine+increment2, lencoarse + increment2, increment2):
  mask3 = (DepFile.iloc[:,0] > (a - increment2) / 1000) & (DepFile.iloc[:, 0] <= a / 1000)

  tablempat[:, 0] = (DepFile.iloc[:, 3] * DepFile.iloc[:, 4]) * mask3.to_numpy()
  column_sums = np.sum(tablempat, axis=0, dtype=np.float64)

  x_masked = np.where(mask3.to_numpy(), DepFile.iloc[:, 0].astype(float), -np.inf)
  y_masked = np.where(mask3.to_numpy(), DepFile.iloc[:, 1].astype(float), -np.inf)

  masspattern.append(column_sums)
  xlocpattern.append(a - increment2 + (increment2 / 2))

  xlocmaxpattern.append(np.max(x_masked))
  ylocmaxpattern.append(np.max(y_masked))

  #negative bigger strips------------
  mask2 = (DepFile.iloc[:, 0] < (-a + increment2) / 1000) & (DepFile.iloc[:, 0] >= -a / 1000)
  tablempat2[:, 0] = (DepFile.iloc[:, 3] * DepFile.iloc[:, 4]) * mask2.to_numpy()

  column_sums = np.sum(tablempat2, axis=0, dtype=np.float64)
  masspattern.append(column_sums)
  xlocpattern.append(-a + increment2 - (increment2 / 2))

  x_masked = np.where(mask2.to_numpy(), DepFile.iloc[:, 0].astype(float), -np.inf)
  y_masked = np.where(mask2.to_numpy(), DepFile.iloc[:, 1].astype(float), -np.inf)

  xlocmaxpattern.append(np.max(x_masked))
  ylocmaxpattern.append(np.max(y_masked))



print(masspattern)
print(xlocpattern)
#---------------------------------------------

labels = xlocpattern
values = masspattern
# Extract scalar values from the arrays in masspattern
masspattern_scalar = [item[0] for item in masspattern] #converts the array of arrays into a list to use it in a graph.
plt.bar(xlocpattern, masspattern_scalar, width= increment1, color = 'orange')
plt.title('Mass of a strip vs. Midpoints of strips')
plt.xlabel('midpoints of strips (mm)')
plt.ylabel('mass of a strip')
plt.show()
