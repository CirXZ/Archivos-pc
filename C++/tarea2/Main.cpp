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
    for(int i=0;i<k;i++){   //solo esta leyendo los equipos
        fp>>n_per;      //lee la cantidad de personas en el equipo  
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


void consultaa(){

    int N,k,l,p;
    Torneo T;
    Equipo* equipos=guardar_teams("Equipos.txt",N);
    T.crear_torneo(equipos,N);
    while(T.get_fase() != 1){
        cout<<"Ingrese consulta "<<" ";
        cin>>p;
        if(p == 1 or p == 3 or p == 2){
            if(p==1){

                T.avanzar_ronda();
            }

            if(p==2){
                T.imprimir_bracket();
                cout<<"\n";
            
            }

            if(p==3){
                //cout<<"ingrese poder a comparar"<<" ";
                cin>>k;
                for(int j=0;j<N;j++){
                    l=0;
                    l= equipos[j].calcular_poder();
                    if(l>=k){
                    cout<<"Equipo: "<<"\n";
                    equipos[j].imprimir_equipo();
                    cout<<"\n";

                    }
                }
            }
        }
        else{
            cout<<"Error valor fuera de rango; ingrese otra vez"<<endl;
        }    
    }
    if(T.get_fase()==1){
        T.imprimir_bracket();
    }
    delete[] equipos;    
}


int main(){
    //Torneo T;
    int p;
    //Equipo* equipos=guardar_teams("Equipos.txt",N);
    //for(int i=0;i<N;i++){
        //equipos[i].imprimir_equipo();
    //}
    //T.crear_torneo(equipos,N);
    consultaa();
 
    //delete[] equipos;
    return 0;       
    }


    ///T.imprimir_bracket();
    //cout<<"\n";
    //T.test(equipos[0]);
    //T.print();
 