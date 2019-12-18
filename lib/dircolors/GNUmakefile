TARGET:=	dircolors.sh

all: $(TARGET)

$(TARGET): dircolors.src
	gdircolors -b $< > $@

clean distclean:
	rm -f $(TARGET)
