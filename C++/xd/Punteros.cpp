#include <iostream>
using namespace std;

int main(){
	int A[11];
	for(int i = 0; i < 10; i++){
		A[i] = i;
	}
	A[10] = -1;

	int *p;
	p = A;
	while(*p != -1){
		cout << *p << " ";
		p++;
	}
	cout << "\n";
	return 0;
}