import numpy as np

def calculate(list):
	if len(lst_input) < 9:
		raise ValueError('List must contain nine numbers.')
	tmp = np.array(lst_input)
	tmp1 = tmp.reshape(3,3)

	lst_mean = list((np.mean(tmp1, axis = 0), np.mean(tmp1, axis = 1), np.mean(tmp1)))
	lst_var = list((np.var(tmp1, axis = 0), np.var(tmp1, axis = 1), np.var(tmp1)))
	lst_sd = list((np.std(tmp1, axis = 0), np.std(tmp1, axis = 1), np.std(tmp1)))
	lst_max = list((np.max(tmp1, axis = 0), np.max(tmp1, axis = 1), np.max(tmp1)))
	lst_min = list((np.min(tmp1, axis = 0), np.min(tmp1, axis = 1), np.min(tmp1)))
	lst_sum = list((np.sum(tmp1, axis = 0), np.sum(tmp1, axis = 1), np.sum(tmp1)))

	calculations = {}
	calculations['mean'] = lst_mean
	calculations['variance'] = lst_var
	calculations['stndard deviation'] = lst_sd
	calculations['max'] = lst_max
	calculations['min'] = lst_min
	calculations['sum'] = lst_sum

	return calculations
    
