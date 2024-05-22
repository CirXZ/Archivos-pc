#include <iostream>
using namespace std;

int* arreglodenumeros(int t){
	int* arr = new int[t];
	for(int i=0;i<t;i++)
		arr[i] = i;
	return arr;
}

void reverse(int* a, int n){
	for(int i = 0; i < n / 2; i++){
		int left, right;
		left = a[i];
		right = a[n - i - 1];
		a[i] = right;
		a[n - i - 1] = left;
	}
}

int main(){
	int* a;
	a = arreglodenumeros(10);
	for(int i = 0;i < 10;i++)
		cout << a[i] << " ";
	cout << "\n";
	reverse(a, 10);
	for(int i = 0;i < 10;i++)
		cout << a[i] << " ";
	cout << "\n";
	delete[] a;
	return 0;
}