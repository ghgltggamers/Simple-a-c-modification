# This is the first Simple++ Transpiler program written purely in python becasuse of it's simplicity
# Written officially by ghgl tg gamer
# Started writting on Aug 30 2024 at 16:38pm in india/new delhi

#source

import sys
import os

argv = sys.argv[1];

print ('Processing ' + argv + '...');

spp_header_file = open("spp.hpp", "w");

__GENERATED_CPP = '// Generated C++ from Simple++ (S++) v1.0-py\n\n#include "spp.hpp"\n\n';

# File extension check
if argv.endswith('.spp'):
    print ('File check was successfull \n\n Checking fatals...');
    
    # Opening the file
    file = open(argv, 'r');
    
    print ('\n\nTranspiling the code...');
    

    # Storing the file content 
    file_content = file.read();

    # print('\n\n\n' + file_content)

    # Processing

    # import statement
    file_content = file_content.replace('import', '#include ');

    # comment:-
    file_content = file_content.replace("comment:-", "//");

    # var int:-
    file_content = file_content.replace("var:int", "int");

    # var string:-
    file_content = file_content.replace("var:string", "std::string");

    # var float:-
    file_content = file_content.replace("var:float", "float");

    # var str = string:-
    file_content = file_content.replace("var:str", "std::string");

    # var bool:-
    file_content = file_content.replace("var:bool", "bool");

    # var double:-
    file_content = file_content.replace("var:dob", "double");

    # cprint:-
    file_content = file_content.replace("cprint:", "std::cout<<");

    # cinput:-
    file_content = file_content.replace("cinput:", "std::cin>>");

    # cpr = cprint:-
    file_content = file_content.replace("cpr:", "std::cout<<");

    # cin = cinput:-
    file_content = file_content.replace("cin:", "std::cin>>");

    # and:-
    file_content = file_content.replace("op:and", "&&");

    # or:-
    file_content = file_content.replace("op:or", "||");

    # not:-
    file_content = file_content.replace("op:not", "!");

    # out:-
    file_content = file_content.replace("op:out", "<<");

    # in:-
    file_content = file_content.replace("op:in", ">>");

    # is:-
    file_content = file_content.replace("op:is", "=");

    # is:-
    file_content = file_content.replace("op:is_equal", "==");

    # not:-
    file_content = file_content.replace("op:not", "!");

    # func:-
    file_content = file_content.replace("func", "void");

    # main:-
    file_content = file_content.replace("main(){", "int main(){");

    # generating a c++ file
    __GENERATED_CPP += file_content;

    CPP = open(argv.replace(".spp", ".cpp"), "w");
    CPP.write(__GENERATED_CPP);

    print ("C++ transpilation done!");

else :
    print('\n\n Error : Fatal SPP ERROR -> Unable to transpile an invalid spp file because spp files ends with .spp file extension but the file you mentioned does not ends with .spp file extension');
    exit ();