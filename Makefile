# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = setup test run clean

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
all: quimica
	
quimica: main.py
	cp main.py quimica && chmod +x quimica

# In this context, the *.project pattern means "anything that has the .project extension"
clean:
	rm quimica
	rm -rf __pycache__