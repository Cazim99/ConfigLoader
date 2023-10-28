

HOW TO USE EXAMPLE ( bool, str, int and other means what type is item value in .ini file)

 ...   config.ini ...

    [settings]
    bool_test = False
    int_test = 6
    string_test = True
    other_test = 6
    notdefined_test = 4,3,4

 ... config.ini ...


... test.py ...

    config_file_informations = {
        "settings": # SECTION NAME
            {
                'items':{ # SECTION ITEMS 
                    'bool_test':'bool',
                    'int_test':'int',
                    'string_test':'str',
                    'other_test':'other',
                }
            },
    }

    CONFIGURATIONS = ConfigLoader.Load("config.ini", config_file_informations)

 ... test.py ...

if you dont define the variable type(section item) it will auto load in 'CONFIGURATIONS' with ast module and detect variable type
