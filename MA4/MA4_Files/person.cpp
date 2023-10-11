#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int fib(int);
		int get();
		void set(int);
	private:
		int age;
	};
 
Person::Person(int n){
	age = n;
	}

int Person::fib(int n){
	if (n <= 1){
		return n;
	}
	else{
		return(fib(n-1) + fib(n-2));
	}
}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_fib(Person* person, int n) {return person->fib(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
