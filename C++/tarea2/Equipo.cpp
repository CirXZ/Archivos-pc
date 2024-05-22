#include "Equipo.hpp"
using namespace std;
//Definimos

//Constructor
Equipo::Equipo(){
    listSize=pos=0;
    head=tail=curr=new tNodo;
    head->sig=NULL;
    head->prev=NULL;
    capt=NULL;
}

//Destructor
Equipo::~Equipo(){
    tNodo* aux;
    curr=tail;
    for(int i=listSize;i!=0;i--){
        aux=curr->sig;
        if(curr!=head){
            curr=curr->prev;
        }
        delete aux;
    }
    delete head;
}

//Reiniciar lista
void Equipo::clear(){
    if(listSize==0){
        return;
    }
    tNodo* aux;
    curr=tail;
    for(int i=listSize;i!=0;i--){
        aux=curr->sig;
        if(curr!=head){
            curr=curr->prev;
        }
        delete aux;
    }
    curr=head;
    tail=head;
    listSize=0;
    pos=0;
    curr->sig=NULL;
    curr->prev=NULL;    
}

//Funcion que agrega un companiero al final de la lista
int Equipo::agregar_companero(std::string name,int power){
    if(listSize!=0){
        tail->sig->sig=new tNodo;
        tail->sig->sig->info.nombre=name;
        tail->sig->sig->info.poder=power;
        tail->sig->sig->info.capitan=false;
        tail->sig->sig->sig=NULL;
        tail->sig->sig->prev=tail->sig;
        tail=tail->sig;
        listSize++;
        return listSize-1;
    }
    tail->sig=new tNodo;
    tail->sig->sig=NULL;
    tail->sig->info.nombre=name;
    tail->sig->info.poder=power;
    tail->sig->info.capitan=false;
    tail->sig->prev=head;
    listSize++;
    return listSize-1;
}

//Funcion que elimina el elemento actual
tElemLista Equipo::erase(){
    tElemLista item;
    if(listSize!=0){
        if(curr==tail){
            tNodo* aux=curr->sig;
            curr->sig=NULL;
            curr=curr->prev;pos--;
            tail=curr;
            item=aux->info;
            listSize--;
            delete aux;
            return item;
        }
        if(curr->sig==tail){
            tNodo* aux=curr->sig;
            curr->sig=aux->sig;
            curr->sig->prev=curr;
            item=aux->info;
            tail=curr;
            listSize--;
            delete aux;
            return item;  
        }
        tNodo* aux=curr->sig;
        curr->sig=aux->sig;
        curr->sig->prev=curr;
        item=aux->info;
        listSize--;
        delete aux;
        return item;
    }
    return item;
}

//Mover el cursor al inicio
void Equipo::moveToStart(){
    curr=head;
    pos=0;    
}

//Mover el cursor al final
void Equipo::moveToEnd(){
    curr=tail;
    pos=listSize-1;
}

//Mover el cursor al siguiente elemento
void Equipo::next(){
    if(curr==tail){
        return;
    }
    curr=curr->sig;
    pos++;    
}

//Mover el cursor al elemento anterior
void Equipo::prev(){
    if(curr==head){
        return;
    }
    curr=curr->prev;
    pos--;
    return;    
}

//Mover el cursor a cierta posicion
void Equipo::moveToPos(int posicion){
    unsigned int i;
    if(posicion<0||posicion>listSize) return;
    curr=head;
    pos=0;
    for(i=0;i<posicion;i++){
        curr=curr->sig;
        pos++;
    }    
}

//Retorna el largo de la lista
int Equipo::length(){
    return listSize;    
}

//Retorna la posicion del cursor
int Equipo::currPos(){
    return pos;
}

//Retorna el valor del elemento actual
tElemLista Equipo::getValue(){
    tElemLista item;
    item=curr->sig->info;
    return item;
}

//Calcula el poder del equipo
int Equipo::calcular_poder(){
    tNodo* aux;
    aux=curr;
    curr=head;
    int sum=0;
    for(int i=0;i<listSize;i++){
        sum+=curr->sig->info.poder;
        curr=curr->sig;
    }

    curr=aux;
    return sum;    
}

//Imprime el equipo
void Equipo::imprimir_equipo(){
    tNodo* aux;
    aux=curr;
    curr=head;
    for(int i=0;i<listSize;i++){
        cout<<"Persona "<<i<<": ";
        cout<<curr->sig->info.nombre<<" ";
        cout<<curr->sig->info.capitan<<" ";
        cout<<curr->sig->info.poder<<endl;
        curr=curr->sig;
    }
    curr=aux;    
}

int Equipo::nombrar_capitan(std::string name){
    tNodo* aux;
    aux=curr;
    curr=head;
    for(int i=0;i<listSize;i++){
        if(name==curr->sig->info.nombre){
            curr->sig->info.capitan=true;
            capt=curr->sig;
            curr=aux;
            return 1;//Capitan encontrado
        }
        curr=curr->sig;
    }
    curr=aux;
    return 0; //No se encontró el capitan
}
std::string Equipo::get_captain(){
    return capt->info.nombre;
}
