#include "Cola.hpp"
using namespace std;

 
tCola::tCola(){
    maxSize=100000000;
    size=0;
    head=0;
    tail=0;
    queueArray=new tElemCola[maxSize];
}

tCola::~tCola(){
    delete[] queueArray;
}

void tCola::clear(){
    head=0;
    tail=0;
    size=0;
}

int tCola::enqueue(tElemCola item){
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

void tCola::dequeue(){
    if(size==0) return;

    if(head==maxSize-1){
        head=(head+1)%maxSize;
        size--;
        return;
    }
    head++;
    size--;
}

tElemCola tCola::frontValue(){
    return queueArray[head];
}

int tCola::length(){
    return size;
} 

