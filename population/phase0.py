class Rabbit():
    # TODO

class Experiment():
    def __init__(self, rabbit):
        self.rabbit = rabbit
        self.size = 100
        self.setup_plot()

    def run(self, iterations):
        for i in range(iterations):
            self.step()
            self.draw()

    def step(self):
        self.rabbit.step()

    def draw(self):
        x_values = [self.rabbit.pos_x * self.size]
        y_values = [self.rabbit.pos_y * self.size]
        colors = [self.rabbit.color]
        self.ax1.axis([0, self.size, 0, self.size])
        self.ax1.scatter(x_values, y_values, color = colors)

        plt.draw()
        plt.pause(0.01)
        self.ax1.cla()

    def setup_plot(self):
        self.fig, self.ax1 = plt.subplots(1)
        self.ax1.set_aspect('equal')
        self.ax1.axes.get_xaxis().set_visible(False)
        self.ax1.axes.get_yaxis().set_visible(False)


my_rabbit = Rabbit(0.25, 0.75, math.pi/4)
my_experiment = Experiment(my_rabbit)
my_experiment.run(100)
