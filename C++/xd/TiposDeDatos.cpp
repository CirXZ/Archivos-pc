#include <iostream>
using namespace std;

int main(){
	/*
	int entero = 71;
	//long int entero_mas_grande;
	//long long int entero_aun_mas_grande;
	
	char caracter = entero;
	cout << caracter << "\n";
	caracter++;
	cout << caracter << "\n";
	//float flotante;
	//double doble;
	//long double mas_preciso;

	cin >> entero;
	if(entero >= 10){
		cout << "el entero es mayor a 10\n";
	} else {
		cout << "el entero no es mayor a 10\n";
	}

	int potencia = 0;
	while(entero != 0){
		entero /= 2;
		if(entero != 0){
			potencia++;
		}
	}
	cout << "2^" << potencia << "\n";

	cin >> entero;
	for(int i = 1; i < entero; i *= 2){
		cout << i << "\n";
	}
*/
	// tamano del arreglo
	int n = 10;
	int a[n];
	for(int i = 0; i < n; i++){
		cin >> a[i];
	}

	for(int i = 0; i < n; i++){
		cout << a[i] << " ";
	}
	cout << "\n";

	long long int a[100];
	float f[100];
	char d[100];

	return 0;
}