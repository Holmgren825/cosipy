import cfg


def test_init_config():
    # Just some sanity checks.
    assert type(cfg.config) == dict
    assert type(cfg.config['data_path']) == str
    assert cfg.config['local_port'] == 8786
    assert type(cfg.config['WRF']) == bool
    assert cfg.config['eval_method'] == 'rmse'


def test_init_constants():
    # Sanity checks
    assert type(cfg.constants) == dict
    # Strings are still strings
    assert cfg.constants['albedo_method'] == 'Oerlemans98'
    assert type(cfg.constants['albedo_method']) == str
    assert cfg.constants['remesh_method'] == 'log_profile'
    # Floats are floats.
    assert cfg.constants['temperature_bottom'] == 270.16
    assert cfg.constants['lat_heat_sublimation'] == 2.834e6
