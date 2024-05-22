#include <iostream>
#include <string>
#define M 10
#define NOUSADA -1
#define OCUPADA -2
#define LIBERADA -3
#define VALORINVALIDO -4;
typedef int tipoClave;
typedef int tipoInfo;
using namespace std;

struct ranura{
	tipoClave clave;
	tipoInfo info;
	int estado;
};




int h(tipoClave k){
	return k%M;
}

int p(tipoClave k,int i){
	//cuadratico
	return i;
}

int hashInsert(ranura* HT,tipoClave k, tipoInfo I){
	int inicio,i;
	cout<<"INSERT: "<<I<<endl;
	int pos=inicio=h(k);
	for(i=1;HT[pos].estado!=NOUSADA && HT[pos].estado!=LIBERADA  && HT[pos].clave!=k;i++){
		pos=(inicio + p(k,i))%M;
	}
	if(HT[pos].clave==k){
		return 0;
	}
	else{
		cout<<"Insert con "<<i-1<<" colisiones exitoso"<<endl;
		HT[pos].clave=k;
		HT[pos].info=I;
		HT[pos].estado=OCUPADA;
		return 1;
	}
}

int hashDelete(ranura* HT,tipoClave k){
	int inicio,i;
	int pos=inicio=h(k);
	for(i=1;HT[pos].estado!=NOUSADA && HT[pos].clave!=k;i++){
		pos=(inicio + p(k,i))%M;
	}
	if(HT[pos].clave==k){
		HT[pos].estado=LIBERADA;
		return HT[pos].info;
	}
	else{
		return 0;
	}
}

tipoInfo hashSearch(ranura* HT,tipoClave k){
	int inicio,i;
	int pos=inicio=h(k);
	for(i=1;HT[pos].estado!=NOUSADA && HT[pos].clave!=k;i++){
		pos= (inicio + p(k,i)) %M;
	}
	if(HT[pos].clave==k){
		return HT[pos].info;
	}
	else{
		return VALORINVALIDO;
	}
}

int main(){
	ranura HT[M];
	for(int i=0;i<10;i++){
		HT[i].info=-1;
		HT[i].estado=NOUSADA;
	}


	hashInsert(HT,3013,3013);
	hashInsert(HT,9877,9877);
	hashInsert(HT,1000,1000);
	hashInsert(HT,2007,2007);
	hashInsert(HT,9879,9879);
	hashInsert(HT,9530,9530);
	hashInsert(HT,1057,1057);
	hashDelete(HT,9879);
	hashInsert(HT,9,9);
	cout<<hashSearch(HT,9)<<endl;
	hashInsert(HT,39,39);
	hashDelete(HT,9);
	cout<<hashSearch(HT,39)<<endl;
	//for(int i=0;i<10;i++){
	//	if(HT[i].estado==OCUPADA){
	//		cout<<HT[i].info<<endl;
	//	}
	//}
	return 0;
}