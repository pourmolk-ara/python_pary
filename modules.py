def verification(config_main, *args):
    final_var = list()

    for i, element in enumerate(config_main) :
        if config_main[i].split('=')[0].strip().lower() == args[i]:
            final_var.append(int(config_main[i].split('=')[1].strip()))
        else:
            print('Expected: {}. Recieved : {}'.format(args[i].lower().capitalize(),config_main[i].split('=')[0].strip()))
    return final_var
