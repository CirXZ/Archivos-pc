#include "Torneo.hpp"
#include <cmath>
#include <string>
#include <fstream>
using namespace std;

//Función lee el archivo y retorna un array de equipos

Equipo* guardar_teams(string name,int &k){
    Equipo apoyo;
    int n_per,poder;
    string nombre,captain;
    ifstream fp;

    fp.open(name);
    if(!fp.is_open()){
        cerr<<"ERROR AL ABRIR EL ARCHIVO";
        return NULL;
    }
    fp>>k;
    Equipo* teams=new Equipo[k];
    for(int i=0;i<k;i++){
        fp>>n_per;
        for(int j=0;j<n_per;j++){
            fp>>nombre;
            fp>>poder;
            teams[i].agregar_companero(nombre,poder);
        }
        fp>>captain;
        teams[i].nombrar_capitan(captain);
    }
    fp.close();
    return teams;
}




int main(){
    int N;
    Torneo T;
    Equipo* equipos=guardar_teams("Equipos.txt",N);
    //for(int i=0;i<N;i++){
    //    equipos[i].imprimir_equipo();
    //}
    T.crear_torneo(equipos,N);
    cout<<T.get_fase()<<endl;
    T.imprimir_bracket();
    T.avanzar_ronda();
    cout<<T.get_fase()<<endl;
    T.imprimir_bracket();
    T.avanzar_ronda();
    cout<<T.get_fase()<<endl;
    T.imprimir_bracket();
    T.avanzar_ronda();
    cout<<T.get_fase()<<endl;
    T.imprimir_bracket();
    delete[] equipos;
    return 0;
}