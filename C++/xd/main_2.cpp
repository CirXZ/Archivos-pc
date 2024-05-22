#include <iostream>
#include <string>
#include <fstream>
using namespace std;

 //Estructuras
struct Registro{
    int dia;
    int mes;
    int anio;
    char rol[12];
    int ppm;
    float presicion;
};

struct Alumno{
    string nombre;
    char rol[12];
    int paralelo;

};

struct consulta{
    int t;
    int d;
    int m;
    int a;
    
};


//Funciones:


void printAlumnos(Alumno* alumnos, int K){
    for(int i=0;i<K-1   ;i++){
        cout<<alumnos[i].nombre<<" "<<alumnos[i].rol<<" "<<alumnos[i].paralelo<<endl;
    }
}

//Main:
int main(){
    // definicion de las variables
    int N,Q;  //Funcion que guarda los registros del binario en el struct
    string name,ap,name_ap;
    int mjr_ppm;
    float mjr_precision;
    string nombre_mjr, rol;
    
    // Abriendo los archivos
    ifstream registro;
    registro.open("registros.dat", ios::binary);

    if (!registro.is_open()){
        cerr<<  "Error al abrir el archivo"<<endl;
        return 1;
    }

    registro.read((char*)&N, sizeof(int));

    cout<<N<<"\n";

    Registro reg[N];

    registro.read((char*)reg, N*sizeof(Registro));
    
    // for(int i=0;i<N;i++){
    //     cout<<reg[i].dia<<" "<<reg[i].mes<<" "<<reg[i].anio<<" "<<reg[i].rol<<" "<<reg[i].ppm<<" "<<reg[i].presicion<<"\n";
        
    // }
    registro.close();



    // Lee el archivo .txt y cuenta los alumnos y guarda los datos es un struct
    int K=0;  
    string apoyo;

    // i) Abirendo el archivo, posteriormente contar la cantidad de alumnos
    ifstream fp;
    fp.open("estudiantes.txt");
    if (!fp.is_open()){
        cerr<<  "Error al abrir el archivo"<<endl;
        return 1;
    }
    while(!fp.eof()){
        getline(fp,apoyo);
        K++;
    }

    
    fp.close();
    

    ifstream archivo;
    archivo.open("estudiantes.txt");
    if(!archivo.is_open()){
        cerr<<"Error al abrir el archivo"<<endl;
        return 1;
    }

    // ii) Guardando los datos de los alumnos en un arreglo de struct
    Alumno alumnos[K];
    
    for(int i=0;i<K;i++){
        archivo >> alumnos[i].rol;
        archivo >>name; archivo >>ap;
        name_ap=name+" "+ap;
        alumnos[i].nombre=name_ap;
        archivo >>alumnos[i].paralelo;
    }
    archivo.close();
    printAlumnos(alumnos,K);



    // Consulta

    cout << "Ingrese número de consultas:";cin>>Q;
    
    consulta cons[Q];

    for(int i=0; i<Q;i++){
        
        cin>>cons[i].t>>cons[i].d>>cons[i].m>>cons[i].a;
        if((cons[i].t == 0 or cons[i].t ==1) and ((cons[i].d<=31 and cons[i].d>0) or cons[i].d == -1) and ((cons[i].m<=12 and cons[i].m>0) or cons[i].m == -1) and (cons[i].a <= 3000 and cons[i].a >0)){
            cout<<"Registro Hecho"<<"\n";

        }
        else{
            cout<<"Registro Malo"<<"\n";
            i--;
            cout<<"Intente otra vez!!"<<"\n";
        }
        
    }  
  
    for(int n=0;n<Q;n++){
        int i;
        int k;
        nombre_mjr= "no hay";
        mjr_ppm= -1;
        mjr_precision=0.0;
        cout<<cons[n].t<<" "<<cons[n].d<<" "<<cons[n].m<<" "<<cons[n].a<<"\n";
        if(cons[n].t==0){
            for(i=0;i<N;i++){
                if(reg[i].anio==cons[n].a){
                    if(cons[n].m != -1){
                        if(cons[n].m== reg[i].mes){
                            if(cons[n].d != -1){
                                if(cons[n].d== reg[i].dia){
                                    if(reg[i].presicion>mjr_precision){
                                        rol= reg[i].rol;
                                    }
                                    else{

                                    }
                                }

                            }
                            else{
                                if(reg[i].presicion>mjr_precision){
                                    rol=reg[i].rol;
                                }
                                else{

                                }   

                            }

                        }
                        else{

                        }

                    }
                    else{
                        if(reg[i].presicion>mjr_precision){
                            rol = reg[i].rol;
                        }
                        else{

                        }
                    }

                }
                else{

                }

            }

        }        
        else{
            for(i=0;i<N;i++){
                if(reg[i].anio==cons[n].a){
                    if(cons[n].m != -1){
                        if(cons[n].m== reg[i].mes){
                            if(cons[n].d!= -1){
                                if(cons[n].d== reg[i].dia){
                                    if(reg[i].ppm>mjr_ppm){
                                        rol= reg[i].rol;
                                    }
                                    else{

                                    }
                                }

                            }
                            else{
                                if(reg[i].ppm>mjr_ppm){
                                    rol=reg[i].rol;
                                }
                                else{

                                }   

                            }

                        }
                        else{

                        }

                    }
                    else{
                        if(reg[i].ppm>mjr_ppm){
                            rol = reg[i].rol;
                        }
                        else{

                        }
                    }

                }
                else{

                }                

            }

        }
        for(k=0;k<K;k++){
            if(rol == alumnos[k].rol){
                nombre_mjr = alumnos[k].nombre;
            }
        }
        cout<<nombre_mjr<<"\n";                


    }

    return 0;
}