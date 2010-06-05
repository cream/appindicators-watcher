simple-client: simple-client.c
	gcc -osimple-client $(shell pkg-config --cflags --libs glib-2.0 appindicator-0.1 dbusmenu-gtk) simple-client.c

clean:
	rm -f simple-client

.phony: clean
