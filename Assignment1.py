
datapath = "../../../data/height_weight/height-weight.csv"

outfile = os.path.join("out", "height_weight_data.png")



def my_function(datapath, outfile):

    my_data = pd.read_csv(datapath)
    x = my_data["Height"]
    y = my_data["Weight"]
    fig, ax = plt.subplots()

    ax.scatter(x,y)
    stats = lr(x,y)
    m = stats.slope
    b = stats.intercept
    y2 = (m*x + b)
    ax.plot(x, y2, color = "red")
    fig.savefig(outfile)

my_function(datapath, outfile)