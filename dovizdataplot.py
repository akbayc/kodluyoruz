from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def dovizdata():

    pasterURL = 'https://kur.doviz.com/serbest-piyasa/sterlin'
    data = urlopen(Request(pasterURL))
    parse = BeautifulSoup(data, 'html.parser')

    sterlin_list = []
    for i in parse.find('div', class_='data').find_all('span', class_='value'):
        sterlin_list.append(float(str(i.text).replace(',', '.')))

    banks = []
    for i in parse.find_all('td'):
        banks.append(str(i.text))

    records = {}

    for i in range(len(banks)//3):
        records[banks[3*i]] = [float(banks[3*i+1].replace(',', '.')), float(banks[3*i+2].replace(',', '.'))]

    records['doviz'] = sterlin_list

    return records


def showData(data):

    df = pd.DataFrame.from_dict(data, orient='index', columns=['alis', 'satis'])

    plt.scatter(df['alis'], df.index)
    plt.scatter(df['satis'], df.index)
    plt.xlabel('Kur')
    plt.ylabel('Banka')
    plt.title('Sterlin Kuru')

    plt.show()


if __name__ == '__main__':
    data = dovizdata()
    showData(data)
