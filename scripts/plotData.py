import matplotlib.pyplot as plt


def plot_data(xAxis,yAxis):

    if len(xAxis) == len(yAxis):
        
        tempLen = len(xAxis)
        count = 0
        plt.plot()

        while count < tempLen:
            plt.plot(xAxis[count], yAxis[count])
            plt.xlabel('date')
            plt.ylabel('price')
            count += 1
        plt.show()

