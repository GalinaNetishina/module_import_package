import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd


def get_employees():
    print("employees:")
    data = pd.read_csv("application/bd/employees.csv")
    sb.heatmap(data, vmax=500, vmin=100, cmap="Greens")
    plt.show()



