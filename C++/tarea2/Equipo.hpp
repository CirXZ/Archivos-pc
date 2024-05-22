#include <string>
#include <iostream>
struct Persona{
    std::string nombre;
    bool capitan;
    int poder;
};

typedef Persona tElemLista; 

struct tNodo{
    tNodo* prev;
    tElemLista info;
    tNodo* sig;
};


class Equipo{
    private:
        tNodo* capt;
        tNodo* head;
        tNodo* tail;
        tNodo* curr;
        unsigned int listSize;
        unsigned int pos;
    public:
        Equipo();
        ~Equipo();

        void clear();
        int agregar_companero(std::string,int);
        tElemLista erase();
        void moveToStart();
        void moveToEnd();
        void next();
        void prev();
        void moveToPos(int);
        int length();
        int currPos();
        tElemLista getValue();
        int calcular_poder();
        void imprimir_equipo();
        int nombrar_capitan(std::string);
        std::string get_captain();
};

typedef Equipo tipoElem;

struct tNodoArbolBin{
    tipoElem* info;
    tNodoArbolBin* izq;
    tNodoArbolBin* der;
};
