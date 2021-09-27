# This is a sample Python script.
from visdom import Visdom
import torch
import os
import csv
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def read_visual(file_path):
    if not os.path.exists(file_path):
        raise ValueError("The loss file is not exit")
        return
    with open(file_path,'r') as f:
        reader = csv.reader(f)
        for row in reader:
            viz.line([float(row[1])],[float(row[0])],win = 'train_loss',update ='append')
        print('visualization completed....')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    loss_path = 'loss.csv'
    print(torch.__version__)
    viz = Visdom()
    viz.line([0],[0],win = 'train_loss',opts =dict(xlabel = 'iter_num',ylabel ='loss',title = 'train_loss'))
    read_visual(loss_path)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
