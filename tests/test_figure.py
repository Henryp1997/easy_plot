from easy_plot import Figure

fig = Figure(title="Test figure", legend_on=True)
fig.plot(
    [1,2,3], [4,5,6], "bo-",
    xlabel="X axis", ylabel="Y axis", label="Test data 1"
)
fig.plot(
    [0, 1, 2], [4, 5, 6], "r^-", label="Test data 2"
)
fig.show()
Figure.display()
