#include <iostream>
using namespace std;

typedef int tElemLista; 

struct tNodo{
    tNodo* prev;
    tElemLista info;
    tNodo* sig;
};

class tLista{
    private:
        tNodo* head;
        tNodo* tail;
        tNodo* curr;
        unsigned int listSize;
        unsigned int pos; //Pos actual del cursor
    public:
        tLista(){
            listSize=pos=0;
            head=tail=curr=new tNodo;
            head->sig=NULL;
            head->prev=NULL;
        }
        ~tLista(){
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

        void clear(){
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
        int append(tElemLista item){
            if(listSize==0){
                tail->sig=new tNodo;
                tail->sig->sig=NULL;
                tail->sig->info=item;
                tail->sig->prev=tail;
                listSize++;
                return 1;
            }
            tail->sig->sig=new tNodo;
            tail->sig->sig->info=item;
            tail->sig->sig->sig=NULL;
            tail->sig->sig->prev=tail->sig;
            tail=tail->sig;
            listSize++;
            return 1;
        }

        int insert(tElemLista item){
            tNodo* aux=curr->sig;
            curr->sig=new tNodo;
            aux->prev=curr->sig;
            curr->sig->sig=aux;
            curr->sig->info=item;
            curr->sig->prev=curr;
            if(curr==tail){
                tail=curr->sig;
                listSize++;
                return 1;
            }
            listSize++;
            return 1;
        }

        tElemLista erase(){
            if(listSize==0){
                return -1;
            }

            if(curr==tail){
                tElemLista item;
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
                tElemLista item;
                tNodo* aux=curr->sig;
                curr->sig=aux->sig;
                curr->sig->prev=curr;
                item=aux->info;
                tail=curr;
                listSize--;
                delete aux;
                return item;  
            }
            tElemLista item;
            tNodo* aux=curr->sig;
            curr->sig=aux->sig;
            curr->sig->prev=curr;
            item=aux->info;
            listSize--;
            delete aux;
            return item;
        }

        void moveToStart(){
            curr=head;
            pos=0;
        }

        void moveToEnd(){
            curr=tail;
            pos=listSize-1;
        }

        void next(){
            if(curr==tail){
                return;
            }
            curr=curr->sig;
            pos++;
        }

        void prev(){
            if(curr==head){
                return;
            }
            curr=curr->prev;
            pos--;
            return;
        }

        void moveToPos(int posicion){
            unsigned int i;
            if(posicion<0||posicion>listSize) return;

            curr=head;
            pos=0;
            for(i=0;i<posicion;i++){
                curr=curr->sig;
                pos++;
            }
        }

        int length(){
            return listSize;
        }

        int currPos(){
            return pos;
        }

        tElemLista getValue(){
            tElemLista item;
            item=curr->sig->info;
            return item;
        }
};


int main(){
    tLista L;
    L.append(10);
    L.append(20);
    L.append(100);
    L.moveToEnd();
    L.insert(83);
    L.append(1000);
    L.moveToPos(2);
    L.insert(80);
    L.moveToStart();
    for(int i=0;i<L.length();i++){
        cout<<L.getValue()<<endl;
        L.next();
    }
    return 0;
}