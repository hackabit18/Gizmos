#include "basicFunctions.h"
#include <iostream>
#include <string>
using namespace std;

int main(){
	string line("Osama Ashhad Azmi means to a p r e h e n d y o u a l l now that he is upset");
	cout<<removeWhiteSpaces(line, 27, 55);
	cin.get();
}