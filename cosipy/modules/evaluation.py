import numpy as np


def evaluate(stake_names, stake_data, df_, NAMELIST):
    """ This methods evaluates the simulation with the stake measurements
        stake_name  ::  """

    if NAMELIST['eval_method'] == 'rmse':
        stat = rmse(stake_names, stake_data, df_)
    else:
        stat = None
       
    return stat


def rmse(stake_names, stake_data, df_, NAMELIST):

    obs_type = NAMELIST['obs_type']
    if (obs_type=='mb'):
        rmse = ((stake_data[stake_names].subtract(df_['mb'],axis=0))**2).mean()**.5
    if (obs_type=='snowheight'):
        rmse = ((stake_data[stake_names].subtract(df_['snowheight'],axis=0))**2).mean()**.5
    return rmse
