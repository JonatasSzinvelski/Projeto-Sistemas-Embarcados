############################################################################
#
# testepy
#
############################################################################

TESTEPY_VERSION = master
TESTEPY_SITE = $(TOPDIR)/../testepy
TESTEPY_SITE_METHOD = local
TESTEPY_DEPENDENCIES = python-rpi-gpio

define TESTEPY_INSTALL_TARGET_CMDS
	rm -rf  $(TARGET_DIR)/home/buildroot/testepy/testepy*
	mkdir -p $(TARGET_DIR)/home/buildroot/testepy
	cp -R $(@D) $(TARGET_DIR)/home/buildroot/testepy
endef


define TESTEPY_INSTALL_INIT_SCRIPT
	$(INSTALL) -D -m 0755 $(TESTEPY_PKGDIR)/S99Teste $(TARGET_DIR)/etc/init.d/
endef


TESTEPY_POST_INSTALL_TARGET_HOOKS += TESTEPY_INSTALL_INIT_SCRIPT

$(eval $(generic-package))
