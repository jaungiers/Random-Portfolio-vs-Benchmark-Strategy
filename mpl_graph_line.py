import matplotlib.pyplot as plt

class mpl_graph_line(object):

    def __init__(self, window_title, xlab, ylab, save_img):
        # These are the "Tableau 20" colors as RGB.
        self.colours_tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
                                 (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
                                 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
                                 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
                                 (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

        # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
        for i in range(len(self.colours_tableau20)):
            r, g, b = self.colours_tableau20[i]
            self.colours_tableau20[i] = (r / 255., g / 255., b / 255.)

        self.save_img = save_img
        self.fig = plt.figure(facecolor='white', dpi=70, figsize=(20, 12))
        self.fig.canvas.set_window_title(window_title)
        self.ax = self.fig.add_subplot(1, 1, 1)
        plt.xlabel(xlab, color='0.4')
        plt.ylabel(ylab, color='0.4')
        self.prettify()

    def prettify(self):
        '''Remove Top/Right Lines and Ticks'''
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['bottom'].set_color('0.5')
        self.ax.spines['left'].set_color('0.5')
        self.ax.tick_params(axis='x', which='both', bottom='on', top='off', color='0.5', labelcolor='0.4')
        self.ax.tick_params(axis='y', which='both', left='on', right='off', color='0.5', labelcolor='0.4')

    def plot(self, data_list,legend_list):
        colour_i = 0
        for data, lw in data_list:
            self.ax.plot(data, linewidth=lw, color=self.colours_tableau20[colour_i])
            colour_i += 1
            if colour_i >= len(self.colours_tableau20):
                colour_i = 0

        plt.legend(legend_list, loc='upper left', prop={'size':'10'}, frameon=False)

        if self.save_img:
            dir_output = 'output'
            plt.savefig(dir_output + '/graph_output.png')
        plt.show()