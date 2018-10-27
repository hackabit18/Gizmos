#include <string>
using namespace std;

string removeWhiteSpaces(string line, int a, int b){
	string newLine = line;
	int counter = a;
	for(int i = a; i < b; i++){
		if(line[i] != ' '){
			newLine[counter] = line[i];
			counter++;
		}
	}
	for(int i = b; i < line.size(); i++){
		newLine[counter] = line[i];
		counter++;
	}
	newLine.resize(counter);
	return newLine;
}