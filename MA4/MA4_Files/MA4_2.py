#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pf
import matplotlib
import matplotlib.pyplot as pp

def fib_python(n):
	if n <= 1:
		return n
	else:
		return(fib_python(n-1) + fib_python(n-2))

@njit
def fib_python_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_python_numba(n-1) + fib_python_numba(n-2))



def main():
	print("Now testing get")
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print("Now testing fib for c++")
	f = Person(5)
	print(f.fib())
	f.set(7)
	print(f.fib())
	print("Now testing fib for normal python")
	print(fib_python(5))
	print(fib_python(7))
	print("Now testing fib for python with numba")
	print(fib_python_numba(5))
	print(fib_python_numba(7))

	n_list = [n for n in range(30, 40)]
	print("Now performing timing tests")
	py_time = []
	for n in range(30, 40):
		start = pf()
		print(fib_python(n))
		end = pf()
		py_time.append(end - start)
	print("Done with python timing")
	py_numba_time = []
	for n in range(30, 40):
		start = pf()
		print(fib_python_numba(n))
		end = pf()
		py_numba_time.append(end - start)
	print("Done with numba timing")
	cpp_time = []
	for n in range(30, 40):
		start = pf()
		f = Person(n)
		print(f.fib())
		end = pf()
		cpp_time.append(end - start)

	fig, axes = pp.subplots(1, 3, figsize=(15, 4))
	for i, y in enumerate([py_time, py_numba_time, cpp_time]):
		ax = axes[i]
		ax.set_xlabel("n")
		ax.set_ylabel("seconds")
		ax.grid(True)
		if i == 0:
			ax.set_title("normal python time")
		if i == 1:
			ax.set_title("numba python time")
		if i == 2:
			ax.set_title("cpp time")
		ax.bar(n_list, y)
	pp.tight_layout()
	pp.savefig(fname="timing30to40")



if __name__ == '__main__':
	main()
