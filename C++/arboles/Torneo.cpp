#include <iostream>
#include "Equipo.hpp"
#include <string>
using namespace std;

typedef Equipo tipoElem;

struct tNodoArbolBin{
    tipoElem info;
    tNodoArbolBin* izq;
    tNodoArbolBin* der;
};

class tABB{
    private:
        tNodoArbolBin* raiz;
        int nElems;
    public:
//CLEAR
        
        tABB(){
            raiz=NULL;
            nElems=0;
        }
        ~tABB(){
            clear();
            delete raiz;
        }

        void clear(){
            clearHelp(raiz);
            raiz=NULL;
            nElems=0;
        }

        void clearHelp(tNodoArbolBin* nodo){
            if(nodo==NULL) return;
            clearHelp(nodo->izq);
            clearHelp(nodo->der);
            delete nodo;
        }
//FIND
        int find(tipoElem item){
            return findHelp(raiz,item);
        }

        int findHelp(tNodoArbolBin* nodo,tipoElem item){
            if(nodo==NULL) return 0;
            if(nodo->info==item) return 1;
            if(item<nodo->info) return findHelp(nodo->izq,item);
            else{
                return findHelp(nodo->der,item);
            }
        }
//INSERT

        void insert(tipoElem item){
            if(find(item)==0){
                return insertHelp(raiz,item);
            }
        }

        void insertHelp(tNodoArbolBin* &nodo,tipoElem item){
            if(nodo==NULL){
                nodo = new tNodoArbolBin;
                nodo->info=item;
                nodo->izq=NULL;
                nodo->der=NULL;
                nElems++;
                return;

            }
            if(item<nodo->info){
                return insertHelp(nodo->izq,item);
            }
            else{
                return insertHelp(nodo->der,item);
            }

        }

        void remove(tipoElem item){
            if(find(item)!=0){
                return removeHelp(raiz,item);
            }
            
        }

        void removeHelp(tNodoArbolBin* &nodo,tipoElem item){
            if(nodo->info==item){
                //CASO 1
                if(nodo->izq==NULL && nodo->der==NULL){
                    tNodoArbolBin* aux=nodo;
                    nodo=NULL;
                    nElems--;
                    delete aux;
                    delete nodo;
                    return;
                }
                //CASO 2.1
                if(nodo->izq==NULL && nodo->der!=NULL){
                    tNodoArbolBin* aux=nodo;
                    nodo=aux->der;
                    delete aux;
                    nElems--;
                    return;
                }
                //CASO 2.2
                if(nodo->izq!=NULL && nodo->der==NULL){
                    tNodoArbolBin* aux=nodo;
                    nodo=aux->izq;
                    delete aux;
                    nElems--;
                    return;
                }
                //CASO 3
                if(nodo->izq!=NULL && nodo->der!=NULL){
                    //BUSCAR PREDECESOR
                    tipoElem pred=findPred(nodo->izq);
                    remove(pred);
                    nodo->info=pred;
                    return;
                }
            }

            if(item<nodo->info){
                return removeHelp(nodo->izq,item);
            }

            if(item>nodo->info){
                return removeHelp(nodo->der,item);
            }


        }

        tipoElem findPred(tNodoArbolBin* nodo){
            if(nodo->der==NULL){
                return nodo->info;
            }
            return findPred(nodo->der);
        }

        void inOrden(){
            inOrdenHelp(raiz);
        }

        void inOrdenHelp(tNodoArbolBin* nodo){
            if(nodo==NULL) return;
            inOrdenHelp(nodo->izq);
            cout<<nodo->info<<endl;//PROCESAR
            inOrdenHelp(nodo->der);
        }

        void As(){
            cout<<raiz->info;
        }
};

