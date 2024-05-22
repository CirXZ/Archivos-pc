#include <iostream>
using namespace std;

typedef int tElemPila;


class tPila{
    private:
        unsigned int maxSize;
        unsigned int top;
        tElemPila* stackArray;
    public:
        tPila(){
            top=0;
            maxSize=100;
            stackArray=new tElemPila[maxSize];
        }
        ~tPila(){
            delete[] stackArray;
        }

        void clear(){
            top=0;
        }

        int push(tElemPila item){
            if(top==maxSize) return 0;
            stackArray[top++]=item;
            return 1;
        }

        void pop(){
            if(top!=0){
                top--;
            }
        }

        tElemPila topValue(){
            return stackArray[top-1];
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