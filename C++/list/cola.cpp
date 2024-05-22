#include <iostream>
#include <string>
using namespace std;

typedef int tElemCola;

class tCola{
    private:
        unsigned int maxSize;
        unsigned int head;
        unsigned int tail;
        unsigned int size;
        tElemCola* queueArray;
    public:
        tCola(){
            maxSize=100;
            size=0;
            head=0;
            tail=0;
            queueArray=new tElemCola[maxSize];
        }
        ~tCola(){
            delete[] queueArray;
        }

        void clear(){
            head=0;
            tail=0;
            size=0;
        }

        int enqueue(tElemCola item){
            if(size==maxSize) return 0;
            
            if(tail==maxSize-1){
                queueArray[tail]=item;
                size++;
                tail=(tail+1)%maxSize;
                return 1;
            }
            queueArray[tail++]=item;
            size++;
            return 1;
        }

        void dequeue(){
            if(size==0) return;

            if(head==maxSize-1){
                head=(head+1)%maxSize;
                size--;
                return;
            }
            head++;
            size--;
        }

        tElemCola frontValue(){
            if(size!=0){
                return queueArray[head];
            }
        }

        int length(){
            return size;
        }
};  