import matplotlib.pyplot as plt
class scl_plt():
    def __init__(self):
        self.font()
        self.ax_line()
        self.ticks()
    
    def size(self, figurefigsize):
        plt.rcParams['figure.figsize']=figurefigsize
        
    def font(self, fontfamily='STIXGeneral', textusetext=False, mathtextfontsize='cm', fontsize=20):
        plt.rcParams["font.family"] = fontfamily
        plt.rcParams['text.usetex'] = textusetext
        plt.rcParams["mathtext.fontset"] = mathtextfontsize
        plt.rcParams['font.size']=fontsize
        
    def ax_line(self, axeslinewidth=2):
        plt.rcParams['axes.linewidth']=axeslinewidth
        
    def ticks(self, xtickdirection='in', ytickdirection='in', xtickminorvisible=True, ytickminorvisible=True, xtickmajorsize=7,
              ytickmajorsize=7, xtickminorsize=3.5, ytickminorsize=3.5, xtickmajorwidth=1.5, ytickmajorwidth=1.5, xtickminorwidth=1.5,
              ytickminorwidth=1.5, ytickright=True, xticktop=True):
        plt.rcParams['xtick.direction'] = xtickdirection
        plt.rcParams['ytick.direction'] = ytickdirection
        plt.rcParams['xtick.minor.visible'] = xtickminorvisible
        plt.rcParams['ytick.minor.visible'] = ytickminorvisible
        plt.rcParams['xtick.major.size'] = xtickmajorsize
        plt.rcParams['ytick.major.size'] = ytickmajorsize
        plt.rcParams['xtick.minor.size']= xtickminorsize
        plt.rcParams['ytick.minor.size']= ytickminorsize
        plt.rcParams['xtick.major.width']= xtickmajorwidth
        plt.rcParams['ytick.major.width']= ytickmajorwidth
        plt.rcParams['xtick.minor.width']= xtickminorwidth
        plt.rcParams['ytick.minor.width']= ytickminorwidth
        plt.rcParams['ytick.right']= ytickright
        plt.rcParams['xtick.top']= xticktop
        