OS:=		$(shell uname -s)

ifeq ($(OS),Darwin)
  TARGET_DIR:=	$(HOME)/Library
else
  TARGET_DIR:=	$(HOME)/lib
endif

NO_INSTALL:=	GNUmakefile
FILES:=		$(filter-out $(NO_INSTALL),$(wildcard *))

TARGETS:=	$(addprefix $(TARGET_DIR)/,$(FILES))

all: $(TARGETS)

$(TARGETS):
	@[ -d "$(TARGET_DIR)" ] || mkdir "$(TARGET_DIR)"
	rm -fr "$@"
	ln -s "$(CURDIR)/$(notdir $@)" "$@"

clean:
	rm -f $(TARGETS)

# vim:set noet sw=8 ts=8:
