import matplotlib.pyplot as plt 

def generate_plot(data: tuple[list[int], list[int]]):
    plt.plot(data[0], data[1])
    plt.xlabel("N (size of input)")
    plt.ylabel("Execution Time (seconds)")
    plt.show()
