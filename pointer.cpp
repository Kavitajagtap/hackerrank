/* This program returns multiple values through single function with the help of pointers.
1 findout factorial of entered number.
2.check entered number is palindrome or not.
3.check entered number is armstrong or not.*/

#include <iostream>
using namespace std;
void pointer(int,int*,int,int*,int,int*);

int main()
{
    int x,p = 0,y,q = 0,z,r = 0;
    cout<<"Enter any number to find factorial:";
    cin >> x;
    cout<<"Enter any number to check if that entered number is Palindrome or not:";
    cin >> y;
    cout<<"Enter any number to check if that entered number is Armstrong or not:";
    cin >> z;
    cout<<"-----------***--------------------***-------------------***--------------------***-------"<<endl;
    star(x,&p,y,&q,z,&r);
    cout<<"factorial of "<<x <<" is: "<<p<<endl;
    cout<<"-------------------------------------------------------------"<<endl;
    if(y == q)
        cout<<y<<" is Palindrome number."<<endl;
    else
        cout<<y<<" is not a Palindrome number"<<endl;
    cout<<"-------------------------------------------------------------"<<endl;
    if(z == r)
        cout<<z<<" is Armstrong number."<<endl;
    else
        cout<<z<<" is not a Armstrong number"<<endl;
    cout<<"-------------------------------------------------------------"<<endl;
    return 0;
}
void pointer(int x,int *p,int y,int *q,int z,int *r)
{   int fact = 1,d, rev = 0,sum = 0,v;
    for(int i = 1;i <= x;i++)
    {
        fact = fact * i;
    }
    *p = fact;
    while (y > 0) {
        d = y % 10;
        rev = rev * 10 + d;
        y = y / 10;
    }
    *q = rev;
    while (z > 0) {
        v = z % 10;
        sum = sum + v*v*v;
        z = z / 10;
    }
    *r = sum;
}
/*Output :-
Enter any number to find factorial:7
Enter any number to check if that entered number is Palindrome or not:121
Enter any number to check if that entered number is Armstrong or not:153
-----------***--------------------***-------------------***--------------------***-------
factorial of 7 is: 5040
-------------------------------------------------------------
121 is Palindrome number.
-------------------------------------------------------------
153 is Armstrong number.
-------------------------------------------------------------*/


