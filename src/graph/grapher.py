import matplotlib.pyplot as plt 

def generate_plot(data: tuple[list[int], list[int]], name: str):
    plt.plot(data[0], data[1])
    plt.xlabel("N (size of input)")
    plt.xticks()
    plt.ylabel("Execution Time (seconds)")
    plt.savefig(f'{name}_execution_time.png')
    plt.show()
