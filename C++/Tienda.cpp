#include "Tienda.hpp"
#include <cmath>
#define NOUSADA -1
#define OCUPADA -2
#define LIBERADA -3
#define VALORINVALIDO -4;
using namespace std;

// constructor que lee el archivo txt y extrae la informacion   
Tienda::Tienda(string text){
    int K,P,id;
    ifstream fp;
    fp.open(text+".txt");
	if (!fp.is_open()){
        cout<<  "Error al abrir el archivo"<<endl;
        
    }
    fp >> K;
    // obteniendo el tamaño de la tabla
    int size_carta= round(K/0.6);
    size_t_cartas=size_carta;
    Carta C;
    ranura_Cartas* Tabla_Cartas = new ranura_Cartas[size_carta]; 

    for(int l=0;l<size_carta;l++){
        tabla_carta[l].estado= NOUSADA;
        tabla_carta[l].cantidad=0;
    }
    for(int i=0;i<K;i++){
        fp>>C.id;
        fp>>C.nombre;
        fp>>C.ataque;
        fp>>C.defensa;
        fp>>C.precio;


        hashInsert_cartas(C.id,C);
    }
    fp>>P;  
    int size_sobre= round(P/0.6);
    size_t_sobres=size_sobre;

    ranura_Sobres* tabla_sobre = new ranura_Sobres[size_sobre];
    for(int l=0;l<size_sobre;l++){
        Tabla_Sobres[l].estado= NOUSADA;
        Tabla_Sobres[l].cantidad=0;
    }
    Sobre D;
    for(int i=0;i<P;i++){
        fp>>D.id;
        for(int j=0;j<10;j++){
            fp>>D.cartas[j].id;
            fp>>D.cartas[j].nombre;
            fp>>D.cartas[j].ataque;
            fp>>D.cartas[j].defensa;
            fp>>D.cartas[j].precio;
        }
        hashInsert_sobres(D.id,D);
    }



    
}
//Destructor
Tienda::~Tienda(){}
//Funciones de la tienda
int Tienda::tengo_la_carta(int id){
    
    return hashSearch_cartas(id);
    
}
void Tienda::mostrar_cartas();
void Tienda::mostrar_sobres();
void Tienda::vender_carta(int id);
void Tienda::vender_sobre(int id);
int Tienda::getRecaudado();
//Hashing
int Tienda::h_cartas(int k){
    return k%size_t_cartas;
}

int Tienda::h_sobres(int k){
    return k%size_t_sobres;
}

int Tienda::p_cartas(int k,int i){
    if(i==0) return 0;
    return 11*i*i + 7*i + 19;
}
int Tienda::p_sobres(int k,int i){
    if(i==0) return 0;
    return 11*i*i + 7*i + 19;
}
//HASH DELETE
int Tienda::hashDelete_cartas(int k){
    int inicio,i;
	int pos=inicio=h(k);
	for(i=1;Tabla_Cartas[pos].estado!=NOUSADA && Tabla_Cartas[pos].clave!=k;i++){
		pos=(inicio + p(k,i))%size_t_cartas;
	}
	if(Tabla_Cartas[pos].clave==k){
		Tabla_Cartas[pos].estado=LIBERADA;
        //delete nodo;
		return Tabla_Cartas[pos].info;
	}
	else{
		return 0;
	}
}
int Tienda::hashDelete_sobres(int k);

//HASH SEARCH
Carta Tienda::hashSearch_cartas(int k){
    int inicio,i;
	int pos=inicio=h(k);
	for(i=1;Tabla_Cartas[pos].estado!=NOUSADA && Tabla_Cartas[pos].clave!=k;i++){
		pos= (inicio + p(k,i)) %M;
	}
	if(Tabla_Cartas[pos].clave==k){
		return Tabla_Cartas[pos].cantidad;
	}
	else{
		return VALORINVALIDO;
	}
}

tipoInfo Tienda::hashSearch_sobres(int k);



//INSERT HASH DE CARTAS
int Tienda::hashInsert_cartas(int k, Carta I){
	int inicio,i;
	int pos=inicio=h(k);
	for(i=1;Tabla_Cartas[pos].estado!=NOUSADA && Tabla_Cartas[pos].estado!=LIBERADA  && Tabla_Cartas[pos].clave!=k;i++){
		pos=(inicio + p(k,i))%size_t_cartas;
	}
	if(Tabla_Cartas[pos].clave==k){
		Tabla_Cartas[pos].cantidad+=1;
	}
	else{
		Tabla_Cartas[pos].clave=k;
		Tabla_Cartas[pos].info=I;
		Tabla_Cartas[pos].estado=OCUPADA;
        Tabla_Cartas[pos].cantidad+=1;
		return 1;
	}
}

//INSERT HASH DE SOBRES
int Tienda::hashInsert_sobres(int k, Sobre I);