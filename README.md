# Simple++ a new C++ modification
Simple++ allows the developers to write C++ programs in a lot easier way with the help of it's simple syntax.

Simple++ allows you to write c++ even in spp files and spp will compile all of those for you

Simple++ is itself written in simple++ and it is a transpiled language which gets transpiled into native C++ after build is completed

Simple++ has the following features

Simple and C++ similar syntax
C++ can be natively written with SPP
Every C and C++ header can be used in S++


functions
main() : This function is important for console application and this function need to be defined like this 

```spp

main(){
    // Spp or cpp code goes here
}

```

No headerfiles needs to be imported for basic work because SPP automatically imports the following C++ headerfiles into the program.

```cpp
#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <cstdio>
#include <cstdlib>
```

## import statement
import helps you to include a C++ headerfile without writting #include just like this

```spp

import <iostream> // in C++ #include <iostream>

import "myheaderc.hpp" // in C++ #include "myheaderc.hpp"

```

## cprint & cpr
cprint & cpr: takes anything and prints it on the console

## cinput & cin
cinput & cin: takes a single argument and then inputs it in console

## op
op stands for operator which helps you in calculations

## op:is
op:is stands for '='

## op:out
op:out stands for '<<'

## op:in
op:in stands for '>>'

## op:and
op:and stands for '&&'

## op:or
op:or stands for '||'

## op:not
op:not stands for '!'


## func
func stands for a void function which is used like this

```spp

func myFunction(){
    // data no return type can be defined with func
}

```

## var
var is used to define a variable datatype

## var:int 
var:int defines an integer variable data type

## var:float 
var:float defines a float variable data type

## var:string 
var:string defines a string variable data type

## var:str 
var:str defines a string variable data type

## var:bool 
var:bool defines a boolean variable data type

## var:dob 
var:dob defines a double variable data type

## comment:-
comment:- defines a comment

# Demo project with spp

```spp

comment:- Including the spp files

main(){
    cprint: "Hellow world 2024";

    var:int a, b, c;

    a = 67;
    b = 78;

    cinput:c;

    cprint: "The result is " op:out a + b + c;
}

```