#include <iostream>
using namespace std;

typedef int tElemPila;

struct tNodo{
    tNodo* sig;
    tElemPila info;
};

class tPila{
    private:
        unsigned int top;
        tNodo* head;
    public:
        tPila(){
            top=0;
            head=new tNodo;
            head->sig=NULL;
        }
        ~tPila(){
            tNodo* aux;
            unsigned int size=top;
            for(int i=0;i<top;i++){
                if(size==1){
                    tNodo* aux=head->sig;
                    delete aux;
                    size--;
                }
                if(size>1){
                    aux=head->sig;
                    head->sig=aux->sig;
                    delete aux;
                    size--;
                }
            }
            delete head;
        }

        void clear(){
            tNodo* aux;
            unsigned int size=top;
            for(int i=0;i<top;i++){
                if(size==1){
                    tNodo* aux=head->sig;
                    delete aux;
                    size--;
                }
                if(size>1){
                    aux=head->sig;
                    head->sig=aux->sig;
                    delete aux;
                    size--;
                }
            }
            top=0;
            head->sig=NULL;
        }

        int push(tElemPila item){
            if(top==0){
                head->sig=new tNodo;
                head->sig->sig=NULL;
                head->sig->info=item;
                top++;
                return 1;
            }
            tNodo* aux=head->sig;
            head->sig=new tNodo;
            head->sig->sig=aux;
            head->sig->info=item;
            top++;
            return 1;
        }

        void pop(){
            if(top==0){
                return;
            }
            if(top==1){
                tNodo* aux=head->sig;
                delete aux;
                top--;
                return;
            }
            tNodo* aux=head->sig;
            head->sig=aux->sig;
            delete aux;
            top--;
            return;
        }

        tElemPila topValue(){
            return head->sig->info;
        }

        int size(){
            return top;
        }
};

int main(){
    tPila P;
    cout<<"Cuenta hacia adelante: "<<endl;
    for(int i=0;i<10;i++){
        cout<<i+1<<endl;
        P.push(i+1);
    }
    P.clear();
    P.push(10);
    cout<<"Cuenta hacia atras: "<<endl;
    int h=P.size();
    for(int i=0;i<h;i++){
        cout<<P.topValue()<<endl;
        P.pop();
    }
    return 0;
}