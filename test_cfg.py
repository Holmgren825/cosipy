import cfg


def test_init_config():
    config = cfg.init_config()
    # Just some sanity checks.
    assert type(config) == dict
    assert type(config['data_path']) == str
    assert config['local_port'] == 8786
    assert type(config['WRF']) == bool
    assert config['eval_method'] == 'rmse'


def test_init_constants():
    config = cfg.init_config()
    constants = cfg.init_constants(config)
    # Sanity checks
    assert type(constants) == dict
    # Strings are still strings
    assert constants['albedo_method'] == 'Oerlemans98'
    assert type(constants['albedo_method']) == str
    assert constants['remesh_method'] == 'log_profile'
    # Floats are floats.
    assert constants['temperature_bottom'] == 270.16
    assert constants['lat_heat_sublimation'] == 2.834e6


def test_init_main_dict():

    # We are basically doing the same checks as in the individual init
    # functions, but making sure that things stay the same in the merge.
    # Strings are still strings
    assert cfg.NAMELIST['albedo_method'] == 'Oerlemans98'
    assert type(cfg.NAMELIST['albedo_method']) == str
    assert cfg.NAMELIST['remesh_method'] == 'log_profile'
    # Floats are floats.
    assert cfg.NAMELIST['temperature_bottom'] == 270.16
    assert cfg.NAMELIST['lat_heat_sublimation'] == 2.834e6
    assert cfg.NAMELIST['local_port'] == 8786
    assert type(cfg.NAMELIST['WRF']) == bool
    assert cfg.NAMELIST['eval_method'] == 'rmse'
