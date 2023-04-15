import argparse
from modules import m_adquisition as mac
from modules import m_wrangling as mwr
from modules import m_analysis as man 
from modules import m_reporting as mre 


def argument_parser():
    parser = argparse.ArgumentParser(description = 'Type of places or one place')
    help_message = 'Two options: 1.- "all" 2.- Name of place.'
    parser.add_argument("-t", "--typeof", help=help_message, type=str)
    args = parser.parse_args()
    return args




def main (some_args):
    data_g = mac.adquisition_gardens()
    data_bm = mac.adquisition_db_bicimad()
    wran_gar = mwr.wrangling_garden(data_g)
    wran_bm = mwr.wrangling_bicimad(data_bm)
    distances_gb = man.calculate_distances(wran_gar, wran_bm) # Se puede acortar más el tiempo
    wran_dist = mwr.wrangcoor(distances_gb)
    min_stn = man.min_stations(wran_dist, wran_bm)
    final_df = mre.join_all(wran_gar, wran_bm, min_stn)
    result_gbm = mre.result(final_df, argument_parser())
    print('====================You may find the results in the folder ./data/ ===================')

    
    
if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)
    
    
    
    
    
    
    
    
'''    parser.add_argument("-b", "--place", help="Show the nearest station of bicimad to the place", action="store_true")'''