import numpy as np

def calculate(lst_input):
	if len(lst_input) < 9:
		raise ValueError('List must contain nine numbers.')
	tmp = np.array(lst_input)
	tmp1 = tmp.reshape(3,3)

	lst_mean = list((np.mean(tmp1, axis = 0).tolist(), np.mean(tmp1, axis = 1).tolist(), np.mean(tmp1).tolist()))
	lst_var = list((np.var(tmp1, axis = 0).tolist(), np.var(tmp1, axis = 1).tolist(), np.var(tmp1).tolist()))
	lst_sd = list((np.std(tmp1, axis = 0).tolist(), np.std(tmp1, axis = 1).tolist(), np.std(tmp1).tolist()))
	lst_max = list((np.max(tmp1, axis = 0).tolist(), np.max(tmp1, axis = 1).tolist(), np.max(tmp1).tolist()))
	lst_min = list((np.min(tmp1, axis = 0).tolist(), np.min(tmp1, axis = 1).tolist(), np.min(tmp1).tolist()))
	lst_sum = list((np.sum(tmp1, axis = 0).tolist(), np.sum(tmp1, axis = 1).tolist(), np.sum(tmp1).tolist()))

	calculations = {}
	calculations['mean'] = lst_mean
	calculations['variance'] = lst_var
	calculations['standard deviation'] = lst_sd
	calculations['max'] = lst_max
	calculations['min'] = lst_min
	calculations['sum'] = lst_sum

	return calculations
    
