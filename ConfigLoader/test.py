from ConfigLoader import ConfigLoader


config_file_informations = {
    "settings": # SECTION NAME
        {
            'items':{ # SECTION ITEMS 
                'full_screen':'bool',
                'dev_mode':'bool',
                'screen_size':'other',
                'server_host':'str',
                'server_port':'int',
            }
        },
}

CONFIGURATIONS = ConfigLoader.Load("config.ini", config_file_informations)
print(CONFIGURATIONS)
