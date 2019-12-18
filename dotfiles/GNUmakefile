NO_INSTALL:=	GNUmakefile
FILES:=		$(filter-out $(NO_INSTALL),$(wildcard *))

PAT_TARGETS:=	$(addprefix $(HOME)/,$(patsubst %,.%,$(FILES)))
ZSH_TARGETS:=	$(HOME)/.zprofile $(HOME)/.zshrc
TARGETS:=	$(PAT_TARGETS) $(ZSH_TARGETS)

all: $(TARGETS)

$(PAT_TARGETS):
	rm -fr "$@"
	ln -s "$(CURDIR)/$(patsubst .%,%,$(notdir $@))" "$@"

$(HOME)/.zprofile:
	rm -fr "$@"
	ln -s "$(CURDIR)/profile" "$@"

$(HOME)/.zshrc:
	rm -fr "$@"
	ln -s "$(CURDIR)/bashrc" "$@"

clean:
	rm -f $(TARGETS)

# vim:set noet sw=8 ts=8:
