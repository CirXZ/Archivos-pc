#include <iostream>
using namespace std;

#define N 10
#define C N

#define MI_ENTERO int
#define arreglo int*

int a;

void modificar_a(int entero){
	a = entero;
	cout << "modificar_a " <<  a << "\n";
}

void a_fake(){
	int a;
	a = 3;
	modificar_a(a);
	cout << "a_fake " << a << "\n";
}

int main(){
	a = 0;
	cout << "main " << a << "\n";
	a_fake();
	cout << "main " << a << "\n";

	arreglo c = new int[3];
	MI_ENTERO const b = 2;
	cout << b << "\n";
	c[0] = 3;
	cout << c[0] << "\n";
	return 0;
}