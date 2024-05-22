#include <iostream>
using namespace std;

class bitvector
{
private:
    int len;
    bool vector[500];
public:
    bitvector();
    ~bitvector();
    int length();
    int member(int j);
    int select(int j);
};

bitvector::bitvector()
{
}
int bitvector::length()
{
    return len;
}
int bitvector::member(int j)
{
    if (j == 1)
    {
        return 1;
    }else
    {
        return 0;
    }
}
int bitvector::select(int j)
{
    return j;
}
bitvector::~bitvector()
{
}


interseccion(bitvector *B, bitvector * C)
{
    
};