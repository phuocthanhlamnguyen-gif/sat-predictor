.PHONY: run package clean install

CC = gcc
FILE = main.c
FILEPY = main.py
BIN = binary/mathlib.so
PYTOOLS = numpy 

# Default target builds the shared library
all: $(BIN)

$(BIN): $(FILE)
	touch report.sp
	mkdir -p binary
	$(CC) -shared -o $(BIN) $(FILE) -lm

run: $(BIN)
	python3 -m venv venv
	. venv/bin/activate && python3 $(FILEPY)

package:
	mkdir -p package
	tar -czvf package/code.tar.gz --exclude=venv --exclude=package --exclude=binary *
	# (Optional: include binary/ in tar by removing '--exclude=binary' if you want it packaged)

clean:
	rm -rf venv binary package venv *.sp

install: 
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install $(PYTOOLS)