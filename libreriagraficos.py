import numpy as np
import matplotlib.pyplot as plt

group_names = ["hola", "chau"]
group_data = [1,2]
fig, ax = plt.subplots()
ax.barh(group_names, group_data)