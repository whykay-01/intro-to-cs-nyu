import matplotlib.pyplot as plt

data_file = open('data.csv', 'a')
data_file.close()
data_file = open('data.csv', 'r')

ls = []
dictionary = {}

data_file.readline()