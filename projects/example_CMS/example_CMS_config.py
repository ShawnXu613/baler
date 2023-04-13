def set_config(c):
    c.input_path = "data/example_CMS/example_CMS.npz"
    # c.compression_ratio            = 2.0
    c.number_of_columns = 24
    c.latent_space_size = 15
    c.epochs = 25
    c.early_stopping = True
    c.early_stopping_patience = 100
    c.min_delta = 0
    c.lr_scheduler = False
    c.lr_scheduler_patience = 100
    c.model_name = "AE"
    c.custom_norm = False
    c.l1 = True
    c.reg_param = 0.001
    c.RHO = 0.05
    c.lr = 0.001
    c.batch_size = 512
    c.test_size = 0.15
    c.data_dimension = 1
    c.apply_normalization = True
    c.extra_compression = False
    c.intermittent_model_saving = False
    c.intermittent_saving_patience = 100
    c.type_list = [
        "int",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
    ]
