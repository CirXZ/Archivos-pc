#include <iostream>
#include <strings>
using namespace std;

#define M 
#define VACIA -1
typedef Carta tipoclave;

struct Carta
{
    int id;
    string nombre;
    int ataque;
    int defensa;
    int precio;
};
