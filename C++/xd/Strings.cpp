#include <iostream>
// funcionalidades de char*
#include <cstring>
// objeto string
#include <string>

using namespace std;

int main(){
	cout << "ARREGLO DE CHAR\n";
	char* A = new char[12];
	cin >> A;
	cout << strlen(A) << "\n";
	cout << A << "\n";

	cout << "STRINGS\n";
	string s;
	cin >> s;
	cout << s << "\n";
	s += s;
	cout << s << "\n";
	cout << s.length() << "\n";
	char c;
	cin >> c;
	cout << s.find(c) << "\n";
 	return 0;
}