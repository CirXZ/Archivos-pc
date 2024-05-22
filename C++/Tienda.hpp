#include <iostream>
#include <string>
struct Carta{
	int id;
	string nombre;
	int ataque;
	int defensa;
	int precio;
};

struct Sobre{
	int id;
	Carta cartas[10];
};

struct ranura_Cartas{
	int clave;
	Carta info;
	int estado;
    int cantidad;
};

struct ranura_Sobres{
	int clave;
	Sobre info;
	int estado;
    int cantidad;
};


class Tienda{
    private:
        ranura_Cartas* Tabla_Cartas;
        ranura_Sobres* Tabla_Sobres;
        int money_act;
        int size_t_cartas;
        int size_t_sobres;
    public:
        Tienda(std::string text);
        ~Tienda();
        int tengo_la_carta(int id);
        void mostrar_cartas();
        void mostrar_sobres();
        void vender_carta(int id);
        void vender_sobre(int id);
        int getRecaudado();
        int h_cartas(int k);
        int h_sobres(int k);
        int p_cartas(int k,int i);
        int p_sobres(int k,int i);
        Carta hashDelete_cartas(int k);
        Sobre hashDelete_sobres(int k);
        Carta hashSearch_cartas(int k);
        Sobre hashSearch_sobres(int k);
        int hashInsert_cartas(int k, Carta I);
        int hashInsert_sobres(int k, Sobre I);
};
