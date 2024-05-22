#include <iostream>
int* arreglodenumeros(int t){
    int* arr = new int[t];
    for(int i=0;i<t;i++)
    arr[i] = i;
return arr;
}
int main(){
    int* a;
    a = arreglodenumeros(10);
    std::cout << 'f'<< std::endl;
    /* ... usar arreglo a */
    delete[] a;
return 0;
}
