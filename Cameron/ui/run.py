print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

from .. import setup
print("The value of setup.count is {0}".format(setup.predicted_sentence))