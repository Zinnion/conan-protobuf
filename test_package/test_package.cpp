#include <cstdlib>
#include <iostream>

#include "addressbook.pb.h"

int main()
{
	std::cout << "Protobuf library installed and working!!!!\n";

	tutorial::Person p;
	p.set_id(21);
	p.set_name("Zinnion");
	p.set_email("maurodelazeri@github.com");

	std::cout << p.SerializeAsString() << std::endl;;
	return EXIT_SUCCESS;
}
