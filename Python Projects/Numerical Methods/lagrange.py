import pandas as pd


# lagrange interpolation and extrapolation function
def lagrange(x, y, input_val, num_data_points):
    output = 0

    input_val = pd.Timestamp(input_val).timestamp()

    if input_val > pd.Timestamp(x[-1]).timestamp():
        # reverse the list
        x = x[::-1]
        y = y[::-1]
    elif pd.Timestamp(x[0]).timestamp() <= input_val <= pd.Timestamp(x[-1]).timestamp():
        # create list containing differences between picked date and all dates
        cloz_list = []

        for i in x:
            cloz_list.append(abs(pd.Timestamp(i).timestamp() - input_val))

        # find index of closest data point
        closest = cloz_list.index(min(cloz_list))
        print(closest)

        # update arrays to closest - num_data_points/2
        x = x[int(closest - num_data_points / 2)::]
        y = y[int(closest - num_data_points / 2)::]

    for i in range(num_data_points):
        temp = 1

        for j in range(num_data_points):
            if i != j:
                xi = pd.Timestamp(x[i]).timestamp()
                xj = pd.Timestamp(x[j]).timestamp()
                temp = temp * (input_val - xj) / (xi - xj)

        output = output + temp * y[i]

    return output
