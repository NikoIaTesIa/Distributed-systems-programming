import georinex as gr
from matplotlib import pyplot as plt

# Определим необходимые константы 
C = 299792458
f_L1 = 1575.42 * 10 ** 6
f_L2 = 1227.6 * 10 ** 6

# Зададим исходные данные станций наблюдения
obs_station_1 = 'dra30270.23o'
obs_station_2 = 'dra40270.23o'
satnav = 'G10'


# Рассчитаем длину волны несущей с частотами f_L1 и f_L2
lambda_L1 = C / f_L1
lambda_L2 = C / f_L2

# Рассчитаем квадрат отношения несущих с частотами f_L1 и f_L2
gamma = f_L2 ** 2 / f_L1 ** 2


# Рассчет Ionofree-комбинации измерений приемника
def ionofree_combination(Phi_L1, Phi_L2):
    Phi_if_star = Phi_L1 - gamma * Phi_L2
    Phi_if = F_if_star / (1 - gamma)
    return Phi_if

# Рассчет Widelane-комбинации измерений приемника
def widelane_combination(Phi_L1, Phi_L2):
    Phi_wl_star = Phi_L1 / gamma_L1 - Phi_L2 / gamma_L2
    Phi_wl = Phi_wl_star * gamma_L1 * gamma_L2 / (gamma_L2 - gamma_L1)
    return 

# Рассчет фазовой псевдодальности
def get_PhiL1_and_PhiL2(L1, L2):
    return lambda_L1 * L1, lambda_L2 * L2

# Рассчет Ionofree и Widelane комбинаций измерений для станции наблюдения
def get_ionofree_and_widelane(obs_station):
    obs = gr.load(obs_station).sel(sv=satnav)
    ionofree = []
    widelane = []
    for L1, L2 in zip(obs['L1'], obs['L2']):
        Phi_L1, Phi_L2 = get_PhiL1_and_PhiL2(L1.data, L2.data)
        ionofree.append((ionofree_comb(Phi_L1, Phi_L2), L1.time))
        widelane.append((widelane_comb(Phi_L1, Phi_L2), L1.time))
    return ionofree, widelane

# Получение разницы значений двух векторов
def get_diff(second, first, y_range):
    diff = []
    for y in y_range
      diff.append(second[y][0] - first[y][0])
    return diff

# Формирование линейных комбинаций данных двух одновременно наблюдаемых обеими станциями спутников
ionofree_station_1, widelane_station_1 = get_ionofree_and_widelane(obs_station_1)
ionofree_station_2, widelane_station_2 = get_ionofree_and_widelane(obs_station_2)

# Визуализация результатов обработки данных
y_range = range(500, len(ionfree_station_1))
plt.plot(y_range, [ionofree_station_1[y][0] for y in y_range], color='blue',
         label='ionofree-комбинация измерений для станции №1')
plt.legend(loc='best')
plt.show()
plt.plot(y_range, [ionofree_station_2[y][0] for y in y_range], color='red',
         label='ionofree-комбинация измерений для станции №2')
plt.legend(loc='best')
plt.show()
plt.savefig('graph_1.png')


plt.plot(y_range, [widelane_station_1[y][0] for y in y_range], color='blue',
         label='widelane-комбинация измерений для станции №1')
plt.legend(loc='best')
plt.show()
plt.plot(y_range, [widelane_station_2[y][0] for y in y_range], color='red',
         label='widelane-комбинация измерений для станции №2')
plt.legend(loc='best')
plt.show()
plt.savefig('graph_2.png')


plt.plot(y_range, get_diff(ionofree_station_2, ionofree_station_1, y_range),
         label='Разность ionofree-комбинаций измерений')
plt.plot(y_range, get_diff(widelane_station_2, widelane_station_1, y_range),
         label='Разность widelane-комбинаций измерений')
plt.legend(loc='best')
plt.show()
plt.savefig('graph_3.png')


