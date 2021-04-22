import matplotlib.pyplot as plt

squares = [i**2 for i in range(1,10)]
inputValues = [i for i in range(len(squares))]

fig, ax = plt.subplots()
ax.set_title("SquareNumbers")
ax.plot(inputValues, squares)
plt.show()