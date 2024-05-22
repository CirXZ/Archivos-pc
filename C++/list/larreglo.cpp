#include <iostream>
#include <string>
using namespace std;

#define MAXSIZE 500

typedef int tElemLista;

class tLista{
    private:
        unsigned int maxSize; //Tamaño maximo de la lista (del arreglo)
        unsigned int listSize; //Tamaño actual de la lista
        unsigned int curr; //Posicion actual del cursor
        tElemLista* listArray; //Array que guarda los datos de la lista
    public:
        //Constructor y destructor respectivamente
        tLista(){
            maxSize=MAXSIZE;
            listSize=0;
            curr=0;
            listArray=new tElemLista[maxSize]; 
        }
        ~tLista(){
            delete[] listArray;
        }
        
        //Reiniciar lista
        void clear(){
            curr=0;
            listSize=0;
        }
        
        //Insertar un elemento en la posicion actual
        int insert(tElemLista item){
            int i;
            if(listSize>=maxSize){
                return -1;
            }

            for(i=listSize;i>curr;i--){
                listArray[i]=listArray[i-1];
            }
            listArray[i]=item;
            listSize++;
            return i;//retorna la pos de insercion
        }
        
        //Insertar un elemento al final de la lista
        int append(tElemLista item){
            if(listSize!=maxSize){
                listArray[listSize++]=item;
                return 1;
            }
            cout<<"Error, lista llena"<<endl;
            return -1;
        }

        //Borra el elemento en la pos actual de la lista
        tElemLista erase(){
            tElemLista item;
            int i;
            if(curr<0 || curr>=listSize){
                return -1;
            }
            item=listArray[curr];
            for(i=curr;i<listSize-1;i++){
                listArray[i]=listArray[i+1];
            }
            listSize--;
            return item;
        }
        //Operaciones del cursor

        //Mover el cursor al inicio
        void moveToStart(){
            curr=0;
        }

        //Mover el cursor al final
        void moveToEnd(){
            curr=listSize;
        }

        //Mover el cursor a la siguiente posicion
        void next(){
            if(curr<listSize){
                curr++;
            }
        }

        //Mover el cursor a la posicion anterior
        void prev(){
            if(curr>0){
                curr--;
            }
        }

        //Operaciones de obtener valores

        //Obtener el largo de la lista
        int length(){
            return listSize;
        }

        //Obtener la posicion del cursor
        int currPos(){
            return curr;
        }

        //Mueve el cursor a la pos especificada
        void moveToPos(int pos){
            if(0<=pos<=listSize){
                curr=pos;
            }
        }

        tElemLista getValue(){
            return listArray[curr];
        }

        //Imprimir lista
        void printL(){
            cout<<'[';
            for(int i=0;i<listSize;i++){
                if(i==listSize-1){
                    cout<<listArray[i];
                }
                else{
                    cout<<listArray[i]<<",";
                }
            }
            cout<<']'<<endl;
        }

};


int main(){
    tElemLista h=1;
    tLista L;
    tLista F;

    for(int i=0;i<10;i++){
        L.append(h++);
    }

    L.moveToPos(5);
    L.insert(23);
    L.prev();
    L.erase();
    L.moveToEnd();
    L.insert(100);
    L.moveToStart();
    L.insert(213);
    L.printL();
    
}
