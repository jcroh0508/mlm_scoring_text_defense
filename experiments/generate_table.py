import pandas as pd
import numpy as np

def generate_table(defense_type, data_selected, threshold_list, attack_success_rate_list, clean_acc_list):
    attack_percentage_list = [i * 100 for i in attack_success_rate_list]
    clean_percentage_list = [i * 100 for i in clean_acc_list]

    if data_selected == 'sst-2':
        orig_asr = 100 
        orig_clean_acc = 90.88
    elif data_selected == 'sst-2_high_50': 
        orig_asr = 93.30
        orig_clean_acc == 90.33
    elif data_selected == 'sst-2_middle_50': 
        orig_asr = 99.96
        orig_clean_acc == 90.72
    elif data_selected == 'offenseval': 
        orig_asr = 100
        orig_clean_acc = 81.96
    elif data_selected == 'offenseval_high_50': 
        orig_asr = 98.86
        orig_clean_acc = 81.72
    elif data_selected == 'offenseval_middle_50': 
        orig_asr = 100
        orig_clean_acc = 8044
    elif data_selected == 'ag': 
        orig_asr = 100
        orig_clean_acc = 93.97
        
    ASR = [orig_asr] * len(attack_success_rate_list)
    CACC = [orig_clean_acc] * len(clean_acc_list) 

    delta_ASR = list(np.subtract(np.array(ASR), np.array(attack_percentage_list)))
    delta_CACC = list(np.subtract(np.array(CACC), np.array(clean_percentage_list)))


    df = pd.DataFrame()
    df['threshold'] = pd.Series(threshold_list)
    df['ASR'] = pd.Series(ASR)
    df['delta_ASR'] = pd.Series(delta_ASR)
    df['CACC'] = pd.Series(CACC)
    df['delta_CACC'] = pd.Series(delta_CACC)

    df.to_csv('tables/{} ({})_table.csv'.format(defense_type, data_selected))


# if __name__ == '__main__':
    """
    # ONION sst-2
    defense_type = 'ONION'
    data_selected = 'sst-2'
    threshold_list = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    attack_success_rate_list = [0.6228070175438597, 0.6195175438596491, 0.6195175438596491, 0.618421052631579, 0.6140350877192983, 0.6118421052631579, 0.6052631578947368, 0.6030701754385965, 0.6019736842105263, 0.6019736842105263, 0.5986842105263158, 0.5932017543859649, 0.5888157894736842, 0.5855263157894737, 0.5822368421052632, 0.5767543859649122, 0.5767543859649122, 0.5756578947368421, 0.5745614035087719, 0.5712719298245614, 0.5701754385964912, 0.5657894736842105, 0.5603070175438597, 0.555921052631579, 0.5515350877192983, 0.5471491228070176, 0.5460526315789473, 0.543859649122807, 0.5394736842105263, 0.5350877192982456, 0.5307017543859649, 0.5252192982456141, 0.5208333333333334, 0.518640350877193, 0.5131578947368421, 0.5087719298245614, 0.5010964912280702, 0.4967105263157895, 0.4901315789473684, 0.48793859649122806, 0.4868421052631579, 0.4857456140350877, 0.48135964912280704, 0.4758771929824561, 0.47039473684210525, 0.46381578947368424, 0.45723684210526316, 0.45285087719298245, 0.44846491228070173, 0.4451754385964912, 0.43859649122807015, 0.43201754385964913, 0.42543859649122806, 0.42105263157894735, 0.4155701754385965, 0.40899122807017546, 0.4067982456140351, 0.40131578947368424, 0.3969298245614035, 0.3925438596491228, 0.3848684210526316, 0.37719298245614036, 0.3717105263157895, 0.36951754385964913, 0.3618421052631579, 0.35635964912280704, 0.35526315789473684, 0.34649122807017546, 0.34100877192982454, 0.3355263157894737, 0.32456140350877194, 0.31798245614035087, 0.3157894736842105, 0.3048245614035088, 0.3048245614035088, 0.29605263157894735, 0.28399122807017546, 0.27960526315789475, 0.2642543859649123, 0.2543859649122807, 0.25219298245614036, 0.24890350877192982, 0.24232456140350878, 0.23684210526315788, 0.22807017543859648, 0.2225877192982456, 0.21710526315789475, 0.21162280701754385, 0.2050438596491228, 0.20285087719298245, 0.2050438596491228, 0.19956140350877194, 0.19188596491228072, 0.18640350877192982, 0.18311403508771928, 0.1787280701754386, 0.17982456140350878, 0.17105263157894737, 0.17105263157894737, 0.16885964912280702]
    clean_acc_list = [0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.8990825688073395, 0.8990825688073395, 0.8990825688073395, 0.8990825688073395, 0.8990825688073395, 0.8990825688073395, 0.8990825688073395, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.9002293577981652, 0.8990825688073395, 0.8990825688073395, 0.8979357798165137, 0.8979357798165137, 0.8979357798165137, 0.8979357798165137, 0.8979357798165137, 0.8979357798165137, 0.8967889908256881, 0.8967889908256881, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8944954128440367, 0.8944954128440367, 0.8944954128440367, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8956422018348624, 0.8967889908256881, 0.8967889908256881, 0.893348623853211, 0.893348623853211, 0.8899082568807339, 0.8899082568807339, 0.8922018348623854, 0.8922018348623854, 0.8922018348623854, 0.893348623853211, 0.8922018348623854, 0.8922018348623854, 0.8899082568807339, 0.8899082568807339, 0.8899082568807339, 0.8876146788990825, 0.8853211009174312, 0.8853211009174312, 0.8853211009174312, 0.8876146788990825, 0.8876146788990825, 0.8876146788990825, 0.8887614678899083, 0.8876146788990825, 0.8864678899082569, 0.8876146788990825, 0.8876146788990825, 0.8876146788990825, 0.8899082568807339, 0.8876146788990825, 0.8876146788990825, 0.8887614678899083, 0.8910550458715596, 0.8887614678899083, 0.8864678899082569, 0.8864678899082569, 0.8876146788990825]
    """
    
    """
    # ONION ag
    defense_type = 'ONION'
    data_selected = 'ag'
    threshold_list = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    attack_success_rate_list = [0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9333333333333333, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93, 0.9266666666666666, 0.9266666666666666, 0.9266666666666666, 0.9266666666666666, 0.9266666666666666, 0.9266666666666666, 0.9266666666666666, 0.9233333333333333, 0.9166666666666666, 0.9133333333333333, 0.9133333333333333, 0.91, 0.9033333333333333, 0.9033333333333333, 0.9, 0.9, 0.8966666666666666, 0.89, 0.8866666666666667, 0.8833333333333333, 0.8766666666666667, 0.87, 0.87, 0.8566666666666667, 0.8533333333333334, 0.8533333333333334, 0.8466666666666667, 0.83, 0.8233333333333334, 0.82, 0.8033333333333333, 0.7833333333333333, 0.7766666666666666, 0.7666666666666667, 0.7366666666666667, 0.7133333333333334, 0.7033333333333334, 0.7, 0.6766666666666666, 0.66, 0.65, 0.6133333333333333, 0.5966666666666667, 0.57, 0.52]
    clean_acc_list = [0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8633333333333333, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.87, 0.8733333333333333, 0.8733333333333333, 0.8733333333333333, 0.8733333333333333, 0.87, 0.87, 0.87, 0.87, 0.8733333333333333, 0.8733333333333333, 0.8733333333333333, 0.8733333333333333, 0.8733333333333333, 0.8733333333333333, 0.8733333333333333, 0.8766666666666667, 0.8766666666666667, 0.8766666666666667, 0.8766666666666667, 0.8766666666666667, 0.8766666666666667, 0.8766666666666667, 0.8766666666666667, 0.8733333333333333, 0.87, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667]
    """

    """
    # ONION dbpedia
    defense_type = 'ONION'
    data_selected = 'dbpedia'
    threshold_list = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    attack_success_rate_list = [0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9366666666666666, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.93, 0.9266666666666666, 0.9266666666666666, 0.9233333333333333, 0.9233333333333333, 0.9233333333333333, 0.9233333333333333, 0.9233333333333333, 0.9233333333333333, 0.92, 0.92, 0.92, 0.92, 0.92, 0.9166666666666666, 0.9133333333333333, 0.91, 0.9066666666666666, 0.9066666666666666, 0.9066666666666666, 0.9033333333333333, 0.9033333333333333, 0.9, 0.9, 0.9, 0.8966666666666666, 0.8966666666666666, 0.89, 0.8866666666666667, 0.8733333333333333, 0.87, 0.8533333333333334, 0.83, 0.8166666666666667, 0.78, 0.7566666666666667, 0.6933333333333334, 0.6533333333333333, 0.5766666666666667]
    clean_acc_list = [0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 0.99, 0.99]
    """

    # ###########################################################################################################################################################
    # MLM sst-2
    """
    defense_type = 'MLMS'
    data_selected = 'sst-2'
    threshold_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 74, 75, 76, 77, 78, 79, 80, 81, 82]
    attack_success_rate_list = [0.0, 0.30043859649122806, 0.37390350877192985, 0.3980263157894737, 0.40131578947368424, 0.39035087719298245, 0.3793859649122807, 0.3574561403508772, 0.34100877192982454, 0.3059210526315789, 0.2850877192982456, 0.25109649122807015, 0.22149122807017543, 0.20175438596491227, 0.20394736842105263, 0.20175438596491227, 0.19846491228070176, 0.19736842105263158, 0.2050438596491228, 0.20723684210526316, 0.21929824561403508, 0.23574561403508773, 0.26096491228070173, 0.3026315789473684, 0.34100877192982454, 0.3991228070175439, 0.44627192982456143, 0.4967105263157895, 0.5471491228070176, 0.5932017543859649, 0.6293859649122807, 0.6699561403508771, 0.7149122807017544, 0.7478070175438597, 0.7905701754385965, 0.8157894736842105, 0.8377192982456141, 0.8497807017543859, 0.8728070175438597, 0.8848684210526315, 0.8914473684210527, 0.9035087719298246, 0.9089912280701754, 0.9177631578947368, 0.9232456140350878, 0.9243421052631579, 0.9265350877192983, 0.9265350877192983, 0.9276315789473685, 0.9276315789473685, 0.9298245614035088, 0.9298245614035088, 0.930921052631579, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491, 0.9320175438596491]
    clean_acc_list = [0.4908256880733945, 0.569954128440367, 0.6077981651376146, 0.6628440366972477, 0.6926605504587156, 0.7052752293577982, 0.7362385321100917, 0.7752293577981652, 0.8084862385321101, 0.8222477064220184, 0.8428899082568807, 0.8451834862385321, 0.8692660550458715, 0.8772935779816514, 0.8795871559633027, 0.8899082568807339, 0.893348623853211, 0.8990825688073395, 0.9059633027522935, 0.908256880733945, 0.9071100917431193, 0.9094036697247706, 0.9105504587155964, 0.911697247706422, 0.9128440366972477, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9185779816513762, 0.9220183486238532, 0.9220183486238532, 0.9197247706422018, 0.9197247706422018, 0.9185779816513762, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505, 0.9174311926605505]
    """

    """
    # MLM ag
    defense_type = 'MLMS'
    data_selected = 'ag'
    threshold_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    attack_success_rate_list = [0.0, 0.2, 0.22, 0.18666666666666668, 0.17333333333333334, 0.16666666666666666, 0.17333333333333334, 0.20333333333333334, 0.22, 0.27, 0.3, 0.32666666666666666, 0.39, 0.4033333333333333, 0.4066666666666667, 0.44, 0.5066666666666667, 0.5733333333333334, 0.62, 0.6833333333333333, 0.7266666666666667, 0.77, 0.82, 0.8366666666666667, 0.8666666666666667, 0.8933333333333333, 0.91, 0.9433333333333334, 0.9466666666666667, 0.95]
    clean_acc_list = [0.22, 0.42, 0.5766666666666667, 0.6733333333333333, 0.73, 0.77, 0.7866666666666666, 0.7966666666666666, 0.8266666666666667, 0.8333333333333334, 0.85, 0.8433333333333334, 0.8433333333333334, 0.85, 0.8533333333333334, 0.8533333333333334, 0.85, 0.8566666666666667, 0.8566666666666667, 0.8633333333333333, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.87, 0.8666666666666667, 0.8666666666666667, 0.87, 0.8733333333333333, 0.8766666666666667, 0.8766666666666667]
    """

    """
    # MLM dbpedia
    defense_type = 'MLMS '
    data_selected = 'dbpedia'
    threshold_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    attack_success_rate_list = [0.0, 0.12, 0.09333333333333334, 0.08666666666666667, 0.10666666666666667, 0.09333333333333334, 0.09333333333333334, 0.14666666666666667, 0.16, 0.17333333333333334, 0.21333333333333335, 0.25333333333333335, 0.2866666666666667, 0.32666666666666666, 0.37333333333333335, 0.41333333333333333, 0.49333333333333335, 0.5466666666666666, 0.54, 0.58, 0.6266666666666667, 0.6533333333333333, 0.68, 0.6866666666666666, 0.7333333333333333, 0.7533333333333333, 0.78, 0.8, 0.8, 0.82, 0.84, 0.8466666666666667, 0.8666666666666667, 0.88, 0.88, 0.8866666666666667, 0.8933333333333333, 0.9, 0.9, 0.9, 0.9066666666666666, 0.9066666666666666, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333, 0.9133333333333333]
    clean_acc_list = [0.07333333333333333, 0.5266666666666666, 0.7, 0.86, 0.8933333333333333, 0.94, 0.9466666666666667, 0.98, 0.9866666666666667, 0.9933333333333333, 0.9933333333333333, 0.9866666666666667, 0.9866666666666667, 0.9866666666666667, 0.9933333333333333, 0.9933333333333333, 0.9933333333333333, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    """

    # generate_table(defense_type=defense_type,
    #             data_selected=data_selected, 
    #             threshold_list=threshold_list,
    #             attack_success_rate_list=attack_success_rate_list,
    #             clean_acc_list=clean_acc_list)
