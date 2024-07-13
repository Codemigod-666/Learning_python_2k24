// Online C++ compiler to run C++ program online
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {

    int n = 5;
    // cin>>n;

    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < n ; j++){
            cout<<"*";
        }
        cout<<endl;
    }
    cout<<"first"<<" "<<"-------------------------"<<endl;

    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j <= i ; j++){
            cout<<"*";
        }
        cout<<endl;
    }

    cout<<"second"<<" "<<"-------------------------"<<endl;

    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < i ; j++){
            cout<<j+1;
        }
        cout<<endl;
    }

    cout<<"third"<<" "<<"-------------------------"<<endl;

    for(int i = 0 ; i <= n ; i++){
        for(int j = 0 ; j < i ; j++){
            cout<<i;
        }
        cout<<endl;
    }

    cout<<"fourth"<<" "<<"-------------------------"<<endl;

    for(int i = 0 ; i <= n ; i++){
        for(int j = n ; j >= i ; j--){
            cout<<"*";
        }
        cout<<endl;
    }

    cout<<"fifth"<<" "<<"-------------------------"<<endl;

    for(int i = 0 ; i <= n ; i++){
        for(int j = n ; j >= i ; j--){
            cout<<n-j+1;
        }
        cout<<endl;
    }

    cout<<"sixth"<<" "<<"-------------------------"<<endl;

    for(int i = 0 ; i <= n ; i++){
        for(int j = n ; j >= i ; j--){
            cout<<" ";
        }
        for(int k = 0 ; k <= i ; k++){
            cout<<"*";
        }
        for(int l = 1 ; l <= i ; l++){
            cout<<"*";
        }
        cout<<endl;
    }

    cout<<"seventh"<<" "<<"-------------------------"<<endl;

    for(int i = 0 ; i <= n ; i++){
        for(int l = 1 ; l <= i ; l++){
            cout<<" ";
        }
        for(int j = n ; j >= i ; j--){
            cout<<"*";
        }
        for(int k = n ; k > i ; k--){
            cout<<"*";
        }
        cout<<endl;
    }

    cout<<"eighth"<<" "<<"-------------------------"<<endl;

    for(int i = 0 ; i < n ; i++){
        for(int j = n ; j > i ; j--){
            cout<<" ";
        }
        for(int k = 0 ; k <= i ; k++){
            cout<<"*";
        }
        for(int l = 1 ; l <= i ; l++){
            cout<<"*";
        }
        cout<<endl;
    }
    for(int i = 0 ; i <= n ; i++){
        for(int l = 1 ; l <= i ; l++){
            cout<<" ";
        }
        for(int j = n ; j >= i ; j--){
            cout<<"*";
        }
        for(int k = n ; k > i ; k--){
            cout<<"*";
        }
        cout<<endl;
    }

    cout<<"nineth"<<" "<<"----------------------------------"<<endl;


    for(int i = 0 ; i < n ; i++){
        for(int k = 0 ; k <= i ; k++){
            cout<<"*";
        }
        cout<<endl;
    }
    for(int i = 0 ; i <= n ; i++){
        for(int j = n ; j >= i ; j--){
            cout<<"*";
        }
        cout<<endl;
    }

    cout<<"tenth"<<" "<<"------------------------------"<<endl;


    for(int i = 0 ; i< n ; i++){
       int k = (i+1) % 2;
        for(int j = 0 ; j <= i ; j++){
            cout<<k;
            if(k == 1) k = 0 ;
            else k = 1;
        }
        cout<<endl;
    }
    cout<<"eleventh"<<" "<<"------------------------------"<<endl;


    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < i ; j++ ){
            cout<<j+1;
        }
        for(int k = n-1; k > i ; k--){
            cout<<" ";
        }
        for(int k = n-2; k > i-1 ; k--){
            cout<<" ";
        }
        for(int k = i ; k > 0 ; k--){
            cout<<k;
        }

        cout<<endl;
    }
    cout<<"twelth"<<" "<<"------------------------------"<<endl;
    int temp = 1;
    for(int i = 0 ;  i < n ; i++){
        for(int j = 0 ; j <= i ; j++){
            cout<<temp++<<" ";
        }
        cout<<endl;
    }
    cout<<"thirteenth"<<" "<<"------------------------------"<<endl;


    for(int i = 0 ; i < n ; i++){
        for(int j = n ; j>i ; j--){
            cout<<" ";
        }
        for(int k = 0 ; k < i ; k++){
            cout<<k+1;
        }
        for(int k = 0 ; k<i-1 ;k++){
            cout<<k+1;
        }
        cout<<endl;
    }
    cout<<"fourteenth"<<" "<<"------------------------------"<<endl;

    for(int i = 0 ; i < n ; i++){
        for( int j = 0 ; j <= i ; j++){
            int k = n-j;
            cout<<k--;
        }
        cout<<endl;
    }
    cout<<"fourteenth"<<" "<<"------------------------------"<<endl;





//*****
//*****
//*****
//*****
//*****
//first -------------------------
//*
//**
//***
//****
//*****
//second -------------------------
//
//1
//12
//123
//1234
//third -------------------------
//
//1
//22
//333
//4444
//55555
//fourth -------------------------
//******
//*****
//****
//***
//**
//*
//fifth -------------------------
//123456
//12345
//1234
//123
//12
//1
//sixth -------------------------
//      *
//     ***
//    *****
//   *******
//  *********
// ***********
//seventh -------------------------
//***********
// *********
//  *******
//   *****
//    ***
//     *
//eighth -------------------------
//     *
//    ***
//   *****
//  *******
// *********
//***********
// *********
//  *******
//   *****
//    ***
//     *
//nineth ----------------------------------
//*
//**
//***
//****
//*****
//******
//*****
//****
//***
//**
//*
//tenth ------------------------------
//1
//01
//101
//0101
//10101
//eleventh ------------------------------
//
//1      1
//12    21
//123  321
//12344321
//twelth ------------------------------
//1
//2 3
//4 5 6
//7 8 9 10
//11 12 13 14 15
//thirteenth ------------------------------
//
//    1
//   121
//  12312
// 1234123
//fourteenth ------------------------------
//5
//45
//345
//2345
//12345
//fourteenth ------------------------------


    return 0;
}