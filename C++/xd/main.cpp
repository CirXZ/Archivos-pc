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
    string apellido;
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


void printAlumnos(Alumno* alumnos, int N){
    cout<<"|||||||||||||||||ALUMNOS||||||||||||"<<endl;
    for(int i=0;i<N;i++){
        cout<<alumnos[i].nombre<<" "<<alumnos[i].apellido<<" "<<alumnos[i].rol<<" "<<alumnos[i].paralelo<<endl;
    }
}

void printRegistro(Registro *r,int N){
    cout<<"||||||||||||REGISTRO||||||||||"<<endl;
    for(int i=0;i<N;i++){
        cout<<r[i].dia<<" "<<r[i].mes<<" "<<r[i].rol<<" "<<r[i].ppm<<" "<<r[i].presicion<<endl;
    }
}

//Funcion que retorna la cantidad de alumnos en el archivo(estudiantes.txt)

int Numero_Alumnos(string texto){
    ifstream fp;
    string apoyo;
    int N=0;
    fp.open(texto);
    if(!fp.is_open()){
        cerr<<"Error al abrir el archivo"<<endl;
        return -1;
    }
    while(!fp.eof()){
        getline(fp,apoyo);
        N++;
    }
    fp.close();
    return N;
}

//Funcion que retorna un arreglo de struct con los datos del archivo "estudiantes.txt"
Alumno* save_Alumnos(string texto,int N){
    ifstream fp;
    fp.open(texto);
    if(!fp.is_open()){
        cerr<<"Error al abrir el archivo"<<endl;
    }
    Alumno *a = new Alumno[N];

    for(int i=0;i<N;i++){
        fp>>a[i].rol;
        fp>>a[i].nombre;
        fp>>a[i].apellido;
        fp>>a[i].paralelo;
    }
    fp.close();
    return a;
}

//Leer y guardar datos bin
Registro* save_Registro(string texto,int *N_reg){
    ifstream fp;
    fp.open(texto,ios::binary);
    if(!fp.is_open()){
    }
    fp.read((char*)N_reg,sizeof(int));
    Registro* reg=new Registro[*N_reg];
    fp.read((char*)reg,*N_reg*sizeof(Registro));
    fp.close();
    return reg;

}

//Main:
int main(){
    int Q;
    //Leer y guardar datos de Alumnos
    int N=Numero_Alumnos("estudiantes.txt");
    Alumno* alumnos=save_Alumnos("estudiantes.txt",N);
    //Leer y guardar datos de Registro
    int N_reg;
    Registro *r=save_Registro("registro.dat",&N_reg);
    //Print datos
    
    printAlumnos(alumnos,N);
    cout<<"\n";
    printRegistro(r,N_reg);
    
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

    for(int i=0;i<Q;i++){
        cout<<cons[i].t<<" "<<cons[i].d<<" "<<cons[i].m<<" "<<cons[i].a<<"\n";
        
    }


    delete[] alumnos;
    delete[] r;
    return 0;
}
