
#define HELPER_1(fun) fun(1);
#define HELPER_2(fun) HELPER_1(fun); fun(2)
#define HELPER_3(fun) HELPER_2(fun); fun(3)
#define HELPER(n, fun) HELPER_##n(fun)
#define LOOP(n, fun) HELPER(n, fun)
#define HELPER2_1(fun) fun(1)
#define HELPER2_2(fun) HELPER2_1(fun), fun(2)
#define HELPER2_3(fun) HELPER2_2(fun), fun(3)
#define HELPER2(n, fun) HELPER2_##n(fun)
#define LOOP_comma(n, fun) HELPER2(n, fun)

#include <iostream>
using namespace std;
void put_n(int n){
    cout << n << endl;
}

#define para(n) int p##n
void put_some_n(LOOP_comma(3, para)){
    cout << p1 << " " << p2 << " " << p3 << endl;
}

int main(){
    LOOP(3, put_n);
    put_some_n(1 ,2,3);
    return 0;
}
