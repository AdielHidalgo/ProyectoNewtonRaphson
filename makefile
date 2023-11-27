bin/main 	:	src/main.cpp
	c++ src/main.cpp -o bin/main 

run	:	bin/main	
	./bin/main