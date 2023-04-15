
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages



def join_all(places, stations, distances):
    df_final = pd.concat([places, stations, distances], axis=1)
    df_final = df_final[['title', '@type', 'street-address', 'name_stn', 'address_station']]
    df_final = df_final.rename(columns={'title': 'Place of interest', '@type': 'Type of place', 'street-address': 'Place address', 'name_stn': 'BiciMAD station', 'address_station': 'Station location'})
    return df_final


def result(dff,args):
    if args.typeof == 'all':
        dff.to_csv('./data/gardens.csv')
        fig, ax =plt.subplots(figsize=(2.5,0.5))
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=dff.values,colLabels=dff.columns,loc='center') # falta asignar qué es en cada fila
        pp = PdfPages("./data/gardens.pdf")
        pp.savefig(fig, bbox_inches= None)
        pp.close()
    else:
        dff = dff.set_index("Place of interest")
        dff = dff.loc[args.typeof]
        dff = pd.DataFrame(dff)
        fig, ax =plt.subplots(figsize=(2.5,0.5))
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=dff.values,colLabels=dff.columns,loc='center') # falta asignar qué es en cada fila
        pp = PdfPages("./data/" + args.typeof + ".pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()