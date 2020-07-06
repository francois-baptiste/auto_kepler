# -*- coding: utf-8 -*-
from data import datasets, config
from kepler import head, tail

def JSify(mydict):
    return str(mydict).replace('None', 'null').replace('True', 'true').replace('False', 'false')

middle = """
const datasets = {datasets};
const config = {config};
""".format(
    datasets=JSify(datasets),
    config=JSify(config))

"".join((head, middle, tail))

with open('index.html', 'w') as the_file:
    the_file.write(head)
    the_file.write(middle)
    the_file.write(tail)

