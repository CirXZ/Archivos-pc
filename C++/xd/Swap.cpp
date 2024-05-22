#include <iostream>
using namespace std;

void swap(int *a, int *b){
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void big_swap(int *A, int *B, int n, int m){
	int tmp[n];
	for(int i = 0; i < n; i++){
		tmp[i] = A[i];
	}

	for(int i = 0; i < n; i++){
		A[i] = B[i];
	}
	
	for(int i = 0; i < n; i++){
		B[i] = tmp[i];
	}

}

int main(){
	/*
	int c = 5;
	int d = 7;
	cout << c << " " << d << "\n";
	swap(&c, &d);
	cout << c << " " << d << "\n";*/

	int n = 10;
	int m = 8;
	int C[n];
	int D[m];
	int times = 0;
	int i = 0;
	while(times < 10){
		C[times] = i;
		i += 2;
		times++;
	}

	times = 0;
	i = 1;
	while(times < 8){
		D[times] = i;
		i += 2;
		times++;
	}
	for(int i = 0; i < n; i++){
		cout << C[i] << " ";
	}
	cout << "\n";
	for(int i = 0; i < m; i++){
		cout << D[i] << " ";
	}
	cout << "\n";
	big_swap(C, D, n, m);
	for(int i = 0; i < n; i++){
		cout << C[i] << " ";
	}
	cout << "\n";
	for(int i = 0; i < m; i++){
		cout << D[i] << " ";
	}
	cout << "\n";
	return 0;
}