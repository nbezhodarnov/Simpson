import numpy as np
import matplotlib.pyplot as plt
import math 

def function(x_input):
	return (x_input ** 2 + 2 * x_input + math.log10(x_input)) ** (1/2)

def Simpson_rule(start, end, error):
	function_array = np.array([function(start), function((start + end) / 2), function(end)], dtype = float)
	f_a = function(start)
	f_center = function((start + end) / 2)
	f_b = function(end)
	step = 1
	dots_count = 3
	h = end - start
	result = (h / 6) * (f_a + 4 * f_center + f_b)
	sum_2 = f_center
	sum_1 = 0
	step = 2
	for i in range(2):
		sum_1 += function((start * (4 - 2 * i - 1) + end * (2 * i + 1)) / 4)
	result_next = (h / 12) * (f_a + 2 * sum_2 + 4 * sum_1 + f_b)
	while (abs(result - result_next) / 15 > error):
		sum_2 += sum_1
		sum_1 = 0
		result = result_next
		dots_count = dots_count + (2 ** (step - 1))
		for i in range(2 ** step):
			sum_1 += function((start * (2 ** (step + 1) - 2 * i - 1) + end * (i * 2 + 1)) / (2 ** (step + 1)))
		step += 1
		result_next = (h / (3 * (2 ** step))) * (f_a + 2 * sum_2 + 4 * sum_1 + f_b)
	dots_count = dots_count + (2 ** (step - 1))
	print('Result: ', result_next)
	print('Count of dots: ', dots_count)
	return result_next

def main():
	Simpson_rule(2, 3, 0.000005 / 10000000)
	
if __name__ == '__main__':
    main()
