import cfg

def test_init_config():
    # Just some sanity checks.
    assert type(cfg.config) == dict
    assert type(cfg.config['data_path']) == str
    assert cfg.config['local_port'] == 8786
    assert type(cfg.config['WRF']) == bool
    assert cfg.config['eval_method'] == 'rmse'