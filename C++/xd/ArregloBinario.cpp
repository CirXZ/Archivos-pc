#include <iostream>
// funcionalidades de char*
#include <cstring>
// objeto string
#include <string>
#include <fstream>

using namespace std;

typedef struct abc {
	char a;
	float b;
	int c;
} abc;

int main(){
	ofstream fwb;
	fwb.open("entrada.dat", ios::binary);
	if(!fwb.is_open()){
		cout << "??????\n";
		exit(1);
	}
	abc a1;
	a1.a = 'A';
	a1.b = 2.12312;
	a1.c = 5;

	int n = 2;
	abc* a2 = new abc[n];

	a2[0] = a1;
	a1.a = 'C';
	a2[1] = a1;
	fwb.write((char*) a2, sizeof(abc) * n);
	fwb.close();

	ifstream frb;
	frb.open("entrada.dat", ios::binary);

	abc* a = new abc[n];
	frb.read((char*) a, n * sizeof(abc));
	if(!frb.is_open()){
		cout << "??????\n";
		exit(1);
	}
	for(int i = 0; i < n; i++){
		cout << a[i].a << " " << a[i].b << " " << a[i].c << "\n";
	}
	return 0;
}
	