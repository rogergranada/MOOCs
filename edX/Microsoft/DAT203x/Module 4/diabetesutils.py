def set_meds_class(x, cut):
    import pandas as pd
    out = pd.DataFrame([0] * x.shape[0])
    out.ix[x > cut] = 1
    return out

def set_readmit_class(x):
    import pandas as pd
    out = pd.DataFrame([0] * x.shape[0])
    out.ix[x != 'NO'] = 1
    return out

def create_map():
    ## list of tuples with name and number of repititions
    name_list = [('infections', 139),
                 ('neoplasms', (239 - 139)),
                 ('endocrine', (279 - 239)),
                 ('blood', (289 - 279)),
                 ('mental', (319 - 289)),
                 ('nervous', (359 - 319)),
                 ('sense', (389 - 359)),
                 ('circulatory', (459 - 389)),
                 ('respiratory', (519 - 459)),
                 ('digestive', (579 - 519)),
                 ('genitourinary', (629 - 579)),
                 ('pregnancy', (679 - 629)),
                 ('skin', (709 - 679)),
                 ('musculoskeletal', (739 - 709)),
                 ('congenital', (759 - 739)),
                 ('perinatal', (779 - 759)),
                 ('ill-defined', (799 - 779)),
                 ('injury', (999 - 799))]
    ##Loop over the tuples to create a dictionary to map codes to names
    out_dict = {}
    count = 1
    for name, num in name_list:
        for i in range(num):
            out_dict.update({str(count): name})
            count += 1
    return out_dict

def map_codes(df, codes):
    import pandas as pd
    indx = 0
    dims = df.shape
    for j in range(dims[1]):
        sub_list = ['i'] * dims[0]
        in_list = df.ix[:,j].tolist()
        for indx in range(dims[0]):
            num = in_list[indx]
            char1 = num[0].upper()
            if ((num == 'unknown') | (num == '?') | (pd.isnull(num))):
                sub_list[indx] = 'unknown'
            elif (char1 == 'V'):
                sub_list[indx] = 'supplemental'
            elif (char1 == 'E'):
                sub_list[indx] = 'injury'
            else:
                lkup = num.split('.')[0]
                sub_list[indx] = codes[lkup]
        df.ix[:,j] = pd.Series(sub_list)
    return df