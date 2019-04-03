import matplotlib.pyplot as plt
import GraphScalerLib as GSL
import json

# loading dataset
f = open("dataset.json", 'r')
dataset_raw = f.read()
dataset_json = json.loads(dataset_raw)
data_U_mess = dataset_json['3NZ70_U']  # choosing data from json dictionary
data_I_mess = dataset_json['3NZ70_I']
x = sorted(data_U_mess)
y = sorted(data_I_mess)

# x-axis ticks
ticks_x = [-8, -7, -6, -5, -4, -3, -2, -1, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.30, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]

# scaling
above_zero_scale = 5  # scaling factor above zero
below_zero_scale = 0.3  # scaling factor below zero
scaled_ticks_x = GSL.scaler(GSL.scaler(ticks_x, 0, above_zero_scale), 0, below_zero_scale, GSL.SmallerThan)
scaled_data_x = GSL.scaler(GSL.scaler(x, 0, above_zero_scale), 0, below_zero_scale, GSL.SmallerThan)

# plotting
fig, ax = plt.subplots()
ax.scatter(scaled_data_x, y, s=20, c="red", marker="x", linewidths=0.1)  # plotting data as scatter
ax.set_xticks(scaled_ticks_x)
ax.set_xticklabels(ticks_x)
# tick styling
ax.tick_params(axis='both', labelsize='small')
ax.tick_params(axis='x', labelrotation=45)
ax.grid()
# axis lines
ax.axhline(linewidth=1)  # x and y axes
ax.axvline(linewidth=1)
ax.set_ylim(-0.125, 0.09)  # setting y limits to show the necessary range of data
ax.set_xlabel("U[V]")
ax.set_ylabel("I[mA]")
ax.set_title("Voltampérová charakteristika Zenerovy diody 3NZ70")
#ax.set_title("Voltampérová charakteristika usměrňovací diody KY132/150")

plt.show()
