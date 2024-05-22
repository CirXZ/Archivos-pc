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
	cout << sizeof(abc) << "\n";
	fwb.write((char*) &a1, sizeof(abc));
	fwb.close();

	ifstream frb;
	frb.open("entrada.dat", ios::binary);
	if(!frb.is_open()){
		cout << "??????\n";
		exit(1);
	}
	abc a2;
	frb.read((char*) &a2, sizeof(abc));

	cout << a2.a << " " << a2.b << " " << a2.c << "\n";
	frb.close();

	return 0;
}