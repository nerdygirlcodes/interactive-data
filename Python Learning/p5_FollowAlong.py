import pandas as pd
from p5 import *
import vispy

df = pd.DataFrame({ 'x': [5, 12, 9, 16, 22, 6, 11], 'y': [40, 63, 33, 23, 73, 45, 56]})

def setup():
    size(500, 500)
    background(255)

def draw():
    background(230)
    color = 0
    line((10, 490), (20 * df['x'].max() + 50, 490))
    line((10, 490), (10, 500 - (5 * df['y'].max() + 80)))
    push()
    no_stroke()
    for i in df.index:
        fill((color + (i * 30)))
        circle((df['x'][i] * 20, df['y'][i] * 5), 10)
    pop()

run(renderer = "vispy")
