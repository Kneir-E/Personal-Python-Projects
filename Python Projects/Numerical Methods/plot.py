import matplotlib.pyplot as plt


# plot data without approximation
def plot(x, y):
    plt.plot(x, y, label="Data Points")
    plt.title("Data Points")
    plt.xlabel("Date")
    plt.ylabel("Price(Open)")
    plt.show()


# plot data with approximation
def plot_approximate(x, y, input_val, output):
    plt.plot(x, y, label="Data Points")
    plt.plot(input_val, output, "o", label="Approximated Point")
    plt.title("Data Points")
    plt.xlabel("Date")
    plt.ylabel("Price(Open)")
    plt.show()
