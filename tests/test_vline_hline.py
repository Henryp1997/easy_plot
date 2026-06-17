from easy_plot import Figure

fig = Figure(title="Test figure")
fig.plot(
    [1,2,3], [4,5,6], "bo-",
    xlabel="X axis", ylabel="Y axis"
)
fig.hline_full(y=5.5, colour="g")
fig.vline_full(x=2.5, colour="m", linewidth=3.0)
fig.show()
Figure.display()
