'''Small utility module to clean up the edu notebooks'''

from cosipy.cpkernel.cosipy_core import cosipy_core
from cosipy.cpkernel.io import IOClass

def create_IO(NAMELIST, restart=False):
    '''Create io, data, results for the run'''
    # Create the essentials.
    IO = IOClass(NAMELIST)
    DATA = IO.create_data_file()
    RESULT = IO.create_result_file()

    # If we want the restart as well
    if restart:
        RESTART = IO.create_restart_file()

        return IO, DATA, RESULT, RESTART

    return IO, DATA, RESULT


def run_model(DATA, IO, NAMELIST, RESULT, RESTART=None,
              stake_names=None, df_stakes_data=None):
# We pass the index of our point to cosipy_core, since python is zero
# indexed we have to subtract one.
    x = 0
    y = 0
    model = cosipy_core(DATA.isel(lat=y, lon=x), y, x, NAMELIST,
                        stake_names=stake_names,
                        stake_data=df_stakes_data)
# Create numpy arrays which aggregates all local results
    IO.create_global_result_arrays()


# Here we are unpacking the results from the model run,
# getting ready to save it to our RESULTS dataframe.
    indY, indX, local_restart, RAIN, SNOWFALL, LWin, LWout, H, LE, B,\
    QRR, MB, surfMB, Q, SNOWHEIGHT, TOTALHEIGHT, TS, ALBEDO, NLAYERS,\
    ME, intMB, EVAPORATION, SUBLIMATION, CONDENSATION, DEPOSITION,\
    REFREEZE, subM, Z0, surfM, MOL, LAYER_HEIGHT, LAYER_RHO, LAYER_T,\
    LAYER_LWC, LAYER_CC, LAYER_POROSITY, LAYER_ICE_FRACTION,\
    LAYER_IRREDUCIBLE_WATER, LAYER_REFREEZE, stake_names, stat, df_eval = model
        
        
                       
    IO.copy_local_to_global(indY, indX, RAIN, SNOWFALL, LWin, LWout, H, LE,
                            B, QRR, MB, surfMB, Q, SNOWHEIGHT, TOTALHEIGHT,
                            TS, ALBEDO, NLAYERS, ME, intMB, EVAPORATION, 
                            SUBLIMATION,  CONDENSATION, DEPOSITION,
                            REFREEZE, subM, Z0, surfM, MOL, LAYER_HEIGHT,
                            LAYER_RHO, LAYER_T, LAYER_LWC, LAYER_CC,
                            LAYER_POROSITY, LAYER_ICE_FRACTION,
                            LAYER_IRREDUCIBLE_WATER,
                            LAYER_REFREEZE)

# Write results to file
    IO.write_results_to_file()
    print('Finished!')
