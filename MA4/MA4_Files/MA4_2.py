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

	n_list = [n for n in range(30, 46)]
	print("Now performing timing tests for 30 to 45")
	py_time = []
	for n in range(30, 46):
		start = pf()
		print(fib_python(n))
		end = pf()
		py_time.append(end - start)
	print("Done with python timing")
	py_numba_time = []
	for n in range(30, 46):
		start = pf()
		print(fib_python_numba(n))
		end = pf()
		py_numba_time.append(end - start)
	print("Done with numba timing")
	cpp_time = []
	for n in range(30, 46):
		start = pf()
		f = Person(n)
		print(f.fib())
		end = pf()
		cpp_time.append(end - start)

	pp.figure(1)
	for i, y in enumerate([py_time, py_numba_time, cpp_time]):
		pp.xlabel("n")
		pp.ylabel("seconds")
		pp.grid(True)
		if i == 0:
			pp.title("Normal python time")
		if i == 1:
			pp.title("Numba python time")
		if i == 2:
			pp.title("C++ time")
		pp.plot(n_list, y)

	pp.legend(['Normal Python', 'Python with Numba', 'C++'])
	pp.yscale('log')
	pp.tight_layout()
	pp.savefig(fname="timing30to45")

	n_list = [n for n in range(20, 31)]
	print("Now performing timing tests for 20 to 30")
	py_time = []
	for n in range(20, 31):
		start = pf()
		print(fib_python(n))
		end = pf()
		py_time.append(end - start)
	print("Done with python timing")
	py_numba_time = []
	for n in range(20, 31):
		start = pf()
		print(fib_python_numba(n))
		end = pf()
		py_numba_time.append(end - start)
	print("Done with numba timing")

	pp.figure(2)
	for i, y in enumerate([py_time, py_numba_time]):
		pp.xlabel("n")
		pp.ylabel("seconds")
		pp.grid(True)
		if i == 0:
			pp.title("Normal python time")
		if i == 1:
			pp.title("Numba python time")
		pp.plot(n_list, y)
	pp.legend(['Normal python', 'Python with Numba', 'C++'])
	pp.yscale('log')
	pp.tight_layout()
	pp.savefig(fname="timing20to30")

#	print("Now calculating fib(47) with python using numba")
#	print(fib_python_numba(47))
#	print("Now calculating fib(47) with c++")
#	f = Person(47)
#	print(f.fib())

	'''
	Output:
	Now calculating fib(47) with python using numba
        2971215073
        Now calculating fib(47) with c++
        -1323752223

	The value using c++ becomes negative because of integer overflow. In this case it could be solved by using unsigned int since we don't
	care about negatvie values.
	'''



if __name__ == '__main__':
	main()
