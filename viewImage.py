import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
import numpy as np
from IPython import embed

for filename in glob.glob("logs/images/*"):
    img=mpimg.imread(filename)
    plt.imshow(img)
    plt.title(filename)
    plt.show()
    embed()

