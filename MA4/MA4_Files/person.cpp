#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int fib();
		int get();
		void set(int);
	private:
		int age;
		int helpfib(int);
	};
 
Person::Person(int n){
	age = n;
	}

int Person::helpfib(int n){
	if (n <= 1){
		return n;
	}
	else{
		return(helpfib(n-1) + helpfib(n-2));
	}
}

int Person::fib(){
	return helpfib(age);
}


int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	// int Person_helpfib(Person* person, int n) {return person->helpfib(n);}
        int Person_fib(Person* person) {return person->fib();}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
