#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int z_p, a_p, z_t, a_t, z_cn, a_cn;
double dm_p, dm_t, dm_cn, m_p, m_t, m_cn, e_loss, e_exc;
double Rint, Rp, Rt, bass_cm, bass_exc;
double unit = 931.494102;

class Isotope{
	public:
		string Name;
		double Mass_def;
		int A;
		int Z;

	Isotope(string name, double mass_def, int a, int z){
		Name=name;
		Mass_def=mass_def;
		A=a;
		Z=z;
	}
};

int case_insensitive_comp(string s1, string s2){
    transform(s1.begin(), s1.end(), s1.begin(), ::tolower);
    transform(s2.begin(), s2.end(), s2.begin(), ::tolower);
    if(s1.compare(s2) == 0)
        return 1;
    return 0;

}

double excit_to_lab(double e_exc, double m_t, double m_p, double m_cn){
return (e_exc-m_t-m_p+m_cn)*(m_t+m_p)/m_t;
}

double lab_to_excit(double e_p, double m_t, double m_p, double m_cn){
return e_p*m_t/(m_t+m_p)+m_t+m_p-m_cn;
}

double bass_barrier_cm(int a_t, int a_p, int z_t, int z_p){
double Rp = 1.12*pow(a_p,1./3.)-0.94*pow(a_p,-1./3.); // [fm]
double Rt = 1.12*pow(a_t,1./3.)-0.94*pow(a_t,-1./3.); // [fm]
double Rint = Rp+Rt+2.7; // [fm]

return 1.44*z_p*z_t/Rint-Rp*Rt/(Rp+Rt);
}

int main()
{

vector<Isotope> vIsotope
{
	{"208Pb",-21748.5, 208, 82},
	{"48Ca", -44224.868, 48, 20},
	{"256No", 87823, 256, 102},
	{"52Cr", -55419.51, 52, 24},
	{"144Sm", -81965.5, 144, 62},
	{"147Sm", -79266.0, 147, 62},
	{"199Rn", -1560, 199, 86},
	{"201Rn", -4107, 201, 86},
	{"202Rn", -6275, 202, 86},
    {"103Rh", -88031.7, 103, 45},
    {"90Zr", -88772.55, 90, 40},
    {"193At", -67, 193, 85}
};

string projectile;// = "52Cr";
string target;// = "147Sm";
string compound_nucl;// = "199Rn";

cout << "Enter projectile: ";
cin >> projectile;
cout << "Enter target: ";
cin >> target;
cout << "Enter compound nucleus: ";
cin >> compound_nucl;

for (auto& iso : vIsotope){
	if(case_insensitive_comp(projectile, iso.Name.c_str())){
		dm_p = iso.Mass_def;
		a_p = iso.A;
		z_p = iso.Z;
        projectile = iso.Name.c_str();
	}
	if(case_insensitive_comp(target, iso.Name.c_str())){
		dm_t = iso.Mass_def;
		a_t = iso.A;
		z_t = iso.Z;
        target = iso.Name.c_str();
	}
	if(case_insensitive_comp(compound_nucl, iso.Name.c_str())){
		dm_cn = iso.Mass_def;
        compound_nucl = iso.Name.c_str();
	}
}

dm_p=dm_p/1000;
dm_t=dm_t/1000;
dm_cn=dm_cn/1000;

z_cn = z_p+z_t;
a_cn = a_p+a_t;

m_p = a_p*unit+dm_p;
m_t = a_t*unit+dm_t;
m_cn = a_cn*unit+dm_cn;

double e_beam[] = {405, 419, 410};
// double e_beam[] = {220.4, 228.3, 236.2};
// double e_beam[]= {219.0,	222.2,	229.5,	233.6,	236.3,	244.5,	251.4};


for(auto & e_p : e_beam){
    cout << "Excitation energy of " <<projectile <<"(" << e_p << " MeV)"  <<"+" << target << " = " << lab_to_excit(e_p, m_t, m_p, m_cn) << " MeV" << endl;
}
    
bass_cm = 1.44*z_p*z_t/Rint-Rp*Rt/(Rp+Rt);
bass_exc = bass_cm*m_p*m_t/(m_p*m_t)+m_t+m_p-m_cn;
cout << "\nBass barrier (in C. M. frame) = " << bass_barrier_cm(a_t, a_p, z_t, z_p) << " MeV" << endl;
cout << "Bass exc. energy = " << lab_to_excit(bass_barrier_cm(a_t, a_p, z_t, z_p)*m_p*(m_p+m_t)/(m_p*m_t), m_t, m_p, m_cn) << " MeV" << endl;
}


