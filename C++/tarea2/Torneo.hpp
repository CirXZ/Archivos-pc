#include <string>
#include "Cola.hpp"


class Torneo{
    private:
        tNodoArbolBin* raiz;
        int nEquipos;
        int nRondas;
        int faseActual;
    public:
        //CONSTRUCTOR
        Torneo();
        ~Torneo();
        void clear();
        void clearHelp(tNodoArbolBin*);
        bool crear_torneo(tipoElem*,int);
        tNodoArbolBin* tAux(int,tipoElem*,int&);
        void imprimir_bracket();
        void imprimir_bracket_aux();
        void avanzar_ronda();
        void avanzar_ronda_aux(tNodoArbolBin*&,int);
        int get_fase();
};