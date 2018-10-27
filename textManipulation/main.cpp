#include "basicFunctions.h"
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

void readFileToProcess(vector<string> &text){
	ifstream fileToProcess;
	fileToProcess.open("fileToProcess.txt");
	while(!fileToProcess.eof()){
		string testLine;
		getline(fileToProcess, testLine);
		text.push_back(testLine);
	}
	fileToProcess.close();
}

void readKeyWords(vector<string> &keyWords){
	ifstream keywordfile;
	keywordfile.open("keywords.txt");
	while(!keywordfile.eof()){
		string testLine;
		getline(keywordfile, testLine);
		keyWords.push_back(testLine);
	}
	keywordfile.close();
}

void printKeyWords(vector<string> &keyWords){
	for (int i = 0; i < keyWords.size(); i++){
		cout<<keyWords[i]<<endl;
	}
}

int main(){
	vector<string> keyWords;
	readKeyWords(keyWords);
	
	vector<string> text;
	readFileToProcess(text);

	printKeyWords(keyWords);
	
	string line("Osama Ashhad Azmi means to a p r e h e n d y o u a l l now that he is upset");
	cout<<removeWhiteSpaces(line, 27, 55);
	cin.get();
}