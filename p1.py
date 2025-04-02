#include<iostream>
#include<Windows.h>
using namespace std;

int main() {

	int beep;
	cout << "type 1 for a low note" << endl;

	cout << "type 2 for a medium note" << endl; 
	
	cout << "type 3 for a high note" << endl;

	cin >> beep;

	if (beep == 1) {
		cout << "low note" << endl;
		Beep(300, 300);
	}
	else if (beep == 2) {
		cout << "medium note" << endl;
	Beep(500, 300);
	}
	else if (beep == 3)
		cout << "high note" << endl; 
	Beep(800, 300);
}

