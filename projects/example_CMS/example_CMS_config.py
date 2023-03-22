def set_config(c):
    c.input_path = "data/example_CMS/example_CMS.npz"
    c.latent_space_size = 15
    c.number_of_columns = 24
    c.epochs = 2
    c.early_stopping = False
    c.lr_scheduler = True
    c.patience = 50
    c.min_delta = 0
    c.model_name = "george_SAE"
    c.custom_norm = False
    c.l1 = True
    c.reg_param = 0.001
    c.RHO = 0.05
    c.lr = 0.001
    c.batch_size = 512
    c.save_as_root = True
    c.test_size = 0.15
    c.energy_conversion = False
    c.extra_compression = False
    c.data_dimension = 1
    c.apply_normalization = True