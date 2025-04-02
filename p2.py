#include<iostream>
#include<Windows.h>
using namespace std;

int main() {
	int choice;
	cin >> choice;
	for (int i = 0; i < choice; i++)
		Beep(300+i*20, 200);

}
