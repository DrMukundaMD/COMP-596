#import numpy as np
import json


class logly(object):
    def __init__(self, validation_flag, epoch, batch):
        if validation_flag:
            # Creates a list containing #(epoch) lists, each of #(batch) items, all set to 0.0
            self._logs = [[[0.0 for x in range(batch)] for y in range(epoch)] for z in range(2)]
        else:
            self._logs = [[0.0 for x in range(batch)] for y in range(epoch)]

        #print("first: {}, second: {}, third:{}".format(len(self._logs), len(self._logs[0]), len(self._logs[0][0])))

    def log(self, phase, epoch, batch, loss):
        if phase == 'train':
            i = 0
        if phase == 'val':
            i = 1
#         print("this is the end")
        self._logs[i][epoch][batch] = loss

    def write(self, save_dir, filename):
        with open(save_dir + filename + '.log', 'w') as outfile:
            json.dump(self._logs, outfile)

    def get_log(self):
        return self._logs
