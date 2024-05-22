#include "Torneo.hpp"
#include <cmath>    
#include <math.h>
using namespace std;

//CONSTRUCTOR
Torneo::Torneo(){
    raiz=NULL;
    nEquipos=0;
    nRondas=0;
    faseActual=0;
} 

Torneo::~Torneo(){
    clear();
    delete raiz;
}
//VOID CLEAR
void Torneo::clear(){
    clearHelp(raiz);
    raiz=NULL;
    nEquipos=0;
    nRondas=0;
    faseActual=0;
}

void Torneo::clearHelp(tNodoArbolBin* nodo){
    if(nodo==NULL) return;
    clearHelp(nodo->izq);
    clearHelp(nodo->der);
    delete nodo;    
}

//CREAR TORNEO
bool Torneo::crear_torneo(tipoElem* equipos,int n){
    nEquipos=n;
    int contador=0;
    int levels=log2(n)+1;
    nRondas=log2(n)+1;
    faseActual=levels;
    raiz = tAux(levels,equipos,contador);
    return true;
}

tNodoArbolBin* Torneo::tAux(int levels,tipoElem* equipos,int &count){
    tNodoArbolBin* match=NULL;
    if(levels>0){
        match=new tNodoArbolBin;
        match->info=NULL;
        if(levels-1==0){
            match->info=&equipos[count++];
        }
        match->izq=tAux(levels-1,equipos,count);
        match->der=tAux(levels-1,equipos,count);
    }

    return match;
}
void Torneo::imprimir_bracket(){
    cout<<"\n";
    imprimir_bracket_aux();
}

void Torneo::imprimir_bracket_aux(){
    string namecap1;
    int pod;
    tCola C;
    tCola Cola;
    tNodoArbolBin nodo;
    C.enqueue(*raiz);
    while(C.length()!=0){
        nodo=C.frontValue();
        if(nodo.izq!=NULL){
            C.enqueue(*nodo.izq);
        }
        if(nodo.der!=NULL){
            C.enqueue(*nodo.der);
        }
        Cola.enqueue(nodo);
        C.dequeue();
    }

    //if(Cola.frontValue().info!=NULL){
    //    cout<<Cola.frontValue().info->get_captain();
    //}
    for(int i=0;i<nRondas;i++){
        if(Cola.frontValue().info!=NULL){
            for(int j=0;j<(pow(2,i));j++){
                namecap1=Cola.frontValue().info->get_captain();
                pod=Cola.frontValue().info->calcular_poder();
                if(j%2==0){
                    cout<<"| "<<namecap1<<" ";
                    cout<<pod<<" ";
                }
                if(j%2==1){
                    cout<<"vs "<<namecap1<<" "<<pod<<" ";;
                    cout<<"|";
                }
                Cola.dequeue();
            }
        }
        else{
            for(int j=0;j<(pow(2,i));j++){
                if(j%2==0){
                    cout<<"| -- ";
                }
                if(j%2==1){
                    cout<<"vs -- |";
                }
                Cola.dequeue();
            }
        }
        cout<<"\n";
    }
}

//Funcion Requerida
bool batallar(Equipo &a,Equipo &b){
    int poder_a,poder_b;
    poder_a=a.calcular_poder();
    poder_b=b.calcular_poder();
    if(poder_a>=poder_b){
        return true;
    }
    return false;
}


void Torneo::avanzar_ronda(){
    avanzar_ronda_aux(raiz,faseActual);
    faseActual--;
}
void Torneo::avanzar_ronda_aux(tNodoArbolBin* &nodo,int levels){
    if(levels>0){
        if(levels-1==1){
            Equipo *a=nodo->izq->info;
            Equipo *b=nodo->der->info;
            if(batallar(*a,*b)){
                nodo->info=a;
                return;
            }
            else{
                nodo->info=b;
                return;
            }
        }
    }
    avanzar_ronda_aux(nodo->izq,levels-1);
    avanzar_ronda_aux(nodo->der,levels-1);
}

int Torneo::get_fase(){
    return faseActual;
}

