// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
class pinnacleclub
{
    int prn;
    char name[50]; 
    public:
    void getdata()
    {
    cout<<"enter your name: ";
    cin>>name;
    cout<<"enter your prn number ";
    cin>>prn;
    }
    void putdata();
    };
    void pinnacleclub :: putdata()
    {
        cout<<"name is "<<name<<end1;
        cout<<"prn is  "<<prn<<end1;
    }
    int main()
    {
        pinnacleclub p;
        p.getdata();
        p.putdata();
    
    return 0;
    }
