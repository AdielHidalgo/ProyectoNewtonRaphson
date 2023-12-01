bin/main 	:	src/main.cpp include/*.hpp
	c++ src/main.cpp -o bin/main -I include

run	:	bin/main	
	./bin/main