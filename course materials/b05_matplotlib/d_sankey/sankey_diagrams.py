import matplotlib.sankey


my_sankey = matplotlib.sankey.Sankey()
my_sankey.add(patchlabel='My Flow',
              flows=[1, 2, 3],
              orientations=[0, 0, 0],
              labels=['One', 'Two', 'Three'],
              trunklength=70,
              pathlengths=[60,50,40],
              )
my_sankey.finish()
