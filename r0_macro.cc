#include <iostream>
#include <cmath>

using namespace std;

int main()
{
 int A_pro, A_tar, A_cn, Z_pro, Z_tar, Z_cn;
 double A_pro_13, A_tar_13, A_cn_13, R_pro, R_tar, C_pro, C_tar, R_null;
 
 cout << "Enter A of projectile: ";
 cin >> A_pro;
 cout << "Enter Z of projectile: ";
 cin >> Z_pro;
 cout << "Enter A of target: ";
 cin >> A_tar;
 cout << "Enter Z of target: ";
 cin >> Z_tar;
 
 A_cn = A_pro + A_tar;
 Z_cn = Z_pro + Z_tar;

 A_pro_13 = pow(A_pro, 1.0/3.0); 
 A_tar_13 = pow(A_tar, 1.0/3.0);
 A_cn_13 = pow(A_cn, 1.0/3.0);
 
 R_pro = 1.28*A_pro_13 + 0.8/A_pro_13 - 0.76;
 R_tar = 1.28*A_tar_13 + 0.8/A_tar_13 - 0.76;
 C_pro = R_pro - 1.0/R_pro;
 C_tar = R_tar - 1.0/R_tar;
 
 R_null = (C_pro + C_tar)/(A_pro_13 + A_tar_13);
 
 cout << "r0=" << R_null << endl;

 return 0; 
}
