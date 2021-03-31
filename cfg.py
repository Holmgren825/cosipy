"""
This is the COSIPY configuration file. It reads in constants
and variables from constants.cfg and config.cfg and make
their contents available as dictionaries.
"""
from configobj import ConfigObj


def init_config():
    # Read in the config.cfg file as an config object.
    cp = ConfigObj('./config.cfg')

    # Deep copy to a dict. strings are in the correct format, have to cast others.
    config = cp.dict()

    # Set bools
    config['restart'] = cp.as_bool('restart')
    config['stake_evaluation'] = cp.as_bool('stake_evaluation')
    config['WRF'] = cp.as_bool('WRF')
    config['WRF_X_CSPY'] = cp.as_bool('WRF_X_CSPY')
    config['slurm_use'] = cp.as_bool('slurm_use')
    config['full_field'] = cp.as_bool('full_field')
    config['force_use_TP'] = cp.as_bool('force_use_TP')
    config['force_use_N'] = cp.as_bool('force_use_N')
    config['tile'] = cp.as_bool('tile')

    # Set ints
    config['compression_level'] = cp.as_int('compression_level')
    config['local_port'] = cp.as_int('local_port')
    config['xstart'] = cp.as_int('xstart')
    config['xend'] = cp.as_int('xend')
    config['ystart'] = cp.as_int('ystart')
    config['yend'] = cp.as_int('yend')

    # We do the logic here instead of in the config. Would be nice if this was
    # updated if a user later changes WRF. Requires an ordered dict, see OGGM
    # cfg.py 
    # Change coordinates if WRF
    if config['WRF']:
        config['northing'] = 'south_north'                                # name of dimension in WRF in- and output
        config['easting'] = 'west_east'                                   # name of dimension in WRF in- and output

    if config['WRF_X_CSPY']:
        config['full_field'] = True


    config['time_start_str'] = config['time_start'][0:10].replace('-', '')
    config['time_end_str'] = config['time_end'][0:10].replace('-', '')
    config['output_netcdf'] = 'Zhadang_ERA5_' + config['time_start_str'] +\
                            '-' + config['time_end_str'] + '.nc'

    return config


def init_constants():
    # Parse the constants.cfg file into a dictionary. Casts necessary variables
    # into the correct types.
    return


config = init_config()
constants = init_constants()