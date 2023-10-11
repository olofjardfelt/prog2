#!/usr/bin/env python3

from person import Person

def main():
	print("Now testing get")
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print("Now testing fib")
	f = Person(5)
	print(f.fib(f.get()))
	f.set(7)
	print(f.fib(f.get()))

if __name__ == '__main__':
	main()
