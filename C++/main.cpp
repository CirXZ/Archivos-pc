#include <cmath>
#include <string>
#include <fstream>
#include <iostream>
using namespace std;


struct Carta{
	int id;
	string nombre;
	int ataque;
	int defensa;
	int precio;
};

struct Sobre{
	int id;
	Carta cartas[10];
};



Carta* tipos_carta(string archive){
	int K,i;
	//string nombre;
	ifstream fp;
    fp.open(archive+".txt");
	if (!fp.is_open()){
        cout<<  "Error al abrir el archivo"<<endl;
        
    }
    fp >> K;

    Carta* tipos_cartas= new Carta[K];

    for(int i=0;i<K;i++){
    	fp >> tipos_cartas[i].id;
    	fp >> tipos_cartas[i].nombre;
    	fp >> tipos_cartas[i].ataque;
    	fp >> tipos_cartas[i].defensa;
    	fp >> tipos_cartas[i].precio;

    }
    fp.close();

    return tipos_cartas;
}

Sobre* sobre(string archive){
	int P,i,j;
	//string nombre;
	ifstream fp;
    fp.open(archive+".txt");
	if (!fp.is_open()){
        cout<<  "Error al abrir el archivo"<<endl;
        
    }
    fp >> P;

    Sobre* sobres = new Sobre[P];

    for(i=0; i<P;i++){
    	fp >> sobres[i].id;
    	
    	for(j=0;j<10;j++){
    		fp >> sobres[i].cartas[j].id;
    		
    		fp >> sobres[i].cartas[j].nombre;
    		
    		fp >> sobres[i].cartas[j].ataque;
    		
    		fp >> sobres[i].cartas[j].defensa;
    		
    		fp >> sobres[i].cartas[j].precio;
    		
    	}
    }

    fp.close();

    return sobres;
}

void Print_sobre(Sobre* sobres,int P){
	int i,j;
	for(i=0; i<P;i++){
    	cout << sobres[i].id;
    	for(j=0;j<10;j++){
    		cout << sobres[i].cartas[j].id<<"\n";
    		
    		cout << sobres[i].cartas[j].nombre<<"\n";
    		
    		cout << sobres[i].cartas[j].ataque<<"\n";
    		
    		cout << sobres[i].cartas[j].defensa<<"\n";
    		
    		cout << sobres[i].cartas[j].precio<<"\n";
    		
    	}
    }

int Numero_carta(string archive){
    int K;
    //string nombre;
    ifstream fp;
    fp.open(archive+".txt");
    if (!fp.is_open()){
        cout<<  "Error al abrir el archivo"<<endl;
        
    }
    fp >> K;

    fp.close();
    return K;
}

int Numero_sobre(string archive){
    int P,K;
    string aux;
    ifstream fp;
    fp.open(archive+".txt");
    if (!fp.is_open()){
        cout<<  "Error al abrir el archivo"<<endl;
        
    }
    fp >> K;

    for(int i=0;i<K;i++){
        fp >> aux;
        fp >> aux;
        fp >> aux;
        fp >> aux;
        fp >> aux;

    }
    fp >> P;
    fp.close();

    return P;
}



}
void print_tienda(Carta* tipos_cartas, int K){
	int i;
	for(int i=0;i<K;i++){
    	cout << tipos_cartas[i].id<<"\n";
    	cout << tipos_cartas[i].nombre<<"\n";
    	cout << tipos_cartas[i].ataque<<"\n";
    	cout << tipos_cartas[i].defensa<<"\n";
    	cout << tipos_cartas[i].precio<<"\n";
    }
}
int main(){
    int K,P;
    K= Numero_carta("Tienda");
    P=Numero_sobre("Tienda");
	Carta *tipos_cartas = tipos_carta("Tienda");
	Sobre *sobres = sobre("Tienda");
	print_tienda(tipos_cartas,K);
	Print_sobre(sobres,P);

	return 0;
}