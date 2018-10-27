#include "basicFunctions.h"
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main(){
	vector<string> keyWords;
	ifstream file;
	file.open("keywords.txt");
	int counter = 0;
	while(!file.eof()){
		string testLine;
		getline(file, testLine);
		keyWords.push_back(testLine);
	}
	cout<<keyWords.size();
	for (int i = 0; i < keyWords.size(); i++){
		cout<<keyWords[i]<<endl;
	}
	string line("Osama Ashhad Azmi means to a p r e h e n d y o u a l l now that he is upset");
	cout<<removeWhiteSpaces(line, 27, 55);
	cin.get();
}