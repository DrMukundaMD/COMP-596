import plotly
from plotly.offline import iplot, init_notebook_mode
#import plotly.plotly as py
import plotly.graph_objs as go
import plotly.io as pio

import os

#plotly.__version__

init_notebook_mode(connected=True)

plotly.io.orca.config.executable = '/home/royce/orca/orca-1.2.1-x86_64.AppImage'
plotly.io.orca.config.save() 

class potly(object):
    def __init__(self, pot=0):
        self.pot = 0
    

    def save_plot(self, train_y, val_y, output_dir, filename):
#         if(len(train_y) != len(val_y)):
#             print("Train not same length as validation")
        
        # get x axis
        train_x = [i for i in range(len(train_y))]
        val_x = [i for i in range(len(val_y))]
        
        # create plots
        fig1 = go.Scatter(x=train_x, y=train_y, name='training')
        fig2 = go.Scatter(x=val_x, y=val_y, name='validation')
        
        # needed for data input
        data = [fig1, fig2]
        
        # create layout: titles
        layout = go.Layout(
            title='Plot Title',
            xaxis=dict(
                title='Batch #',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            ),
            yaxis=dict(
                title='Loss',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        )
        
        # load data and layout
        fig = go.Figure(data=data, layout=layout)
        
        # double check to make sure if directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        pio.write_image(fig, output_dir + filename + '.png')

        