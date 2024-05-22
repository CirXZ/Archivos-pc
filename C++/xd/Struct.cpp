#include <iostream>
using namespace std;

typedef struct guerrero {
	int vida;
	int fuerza;
	char nombre;
	float velocidad;
} guerrero ;

int main(){
	guerrero g1;
	g1.fuerza = 20;
	g1.nombre = 'c';
	g1.velocidad = 10.7;
	cin >> g1.vida;
	cout << &g1 << "\n"
		 << &g1.vida << "\n" 
		 << &g1.fuerza << "\n" 
		 << (void*) &g1.nombre << "\n" 
		 << &g1.velocidad << "\n";
    

    /*
	guerrero gs[3];
	for(int i = 0; i < 3; i++){
		cin >> gs[i].vida
			>> gs[i].fuerza
			>> gs[i].nombre
			>> gs[i].velocidad;
	}
	for(int i = 0; i < 3; i++){
		cout << gs[i].vida << " " 
			 << gs[i].fuerza << " " 
			 << gs[i].nombre << " " 
			 << gs[i].velocidad << "\n";
	}*/
	return 0;
}
