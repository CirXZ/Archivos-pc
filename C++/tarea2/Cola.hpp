#include <iostream>
#include <string>
#include "Equipo.hpp"
 
typedef tNodoArbolBin tElemCola;

class tCola{ 
    private:
        unsigned int maxSize;
        unsigned int head;
        unsigned int tail;
        unsigned int size;
        tElemCola* queueArray;
    public:
        tCola();
        ~tCola();
        void clear();
        int enqueue(tElemCola);
        void dequeue();
        tElemCola frontValue();
        int length();
};