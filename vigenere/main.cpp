#include <iostream>
#include <string>
using namespace std;

class VigenereCipher {
	public:
		string key;
	
		VigenereCipher(string keyword) {
			for (int i = 0; i < keyword.size(); i++) {
				if (keyword[i] >= 'A' && keyword[i] <= 'Z') {
					this->key += keyword[i];
				} else if (keyword[i] >= 'a' && keyword[i] <= 'z'){
					this->key += keyword[i] + 'A' - 'a';
				}
			}
		}
		string encrypt(string str) {
			string result;
			
			for (int i = 0, j = 0; i < str.size(); i++) {
				if (str[i] >= 'a' && str[i] <= 'z') {
					str[i] += 'A' - 'a';
				} else if (str[i] < 'A' || str[i] > 'Z') {
					continue;
				}
				result += (str[i] + key[j] - 2 * 'A')%26 + 'A';
				j = (j+1)%key.size();
			}
			return result;
		}
		
		string decrypt(string str) {
			string result;
			
			for (int i = 0, j = 0; i < str.size(); i++) {
				if (str[i] >= 'a' && str[i] <= 'z') {
					str[i] += 'A' - 'a';
				} else if (str[i] < 'A' || str[i] > 'Z') {
					continue;
				}
				result += (str[i] - key[j] + 26)%26 + 'A';
				j = (j + 1)%key.size();
			}
			return result;
		}
};

int main() {
	VigenereCipher cipher("SKYHILL");
	
	string key = "SKYHILL";
	string mt = "MATEUS";
	string rd = "RODRIGO";
	
	string mtEncrypted = cipher.encrypt(mt);
	string rdEncrypted = cipher.encrypt(rd);
	
	string mtDecrypted = cipher.decrypt(mtEncrypted);
	string rdDecrypted = cipher.decrypt(rdEncrypted);
	
	cout << "Chave usada: "<<key << endl;
	cout << mt << endl;
	cout << "Mateus Encrypted: " << mtEncrypted << endl;
	cout << "Mateus Decrypted: " << mtDecrypted << endl;
	cout << rd << endl;
	cout << "Rodrigo Encrypted: " << rdEncrypted << endl;
	cout << "Rodrigo Decrypted: " << rdDecrypted << endl;
}
