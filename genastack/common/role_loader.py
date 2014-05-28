# =============================================================================
# Copyright [2013] [Kevin Carter]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
import logging
import os
import pkgutil
import imp

import genastack


LOG = logging.getLogger('genastack-engine')


class RoleLoad(object):
    """Load a given Configuration Management role.

    :param config_type: ``str``
    """

    def __init__(self, config_type):
        self.config_type = config_type

    def get_method(self, path, name):
        """Import what is required to run the System.

        :param path:
        :param name:
        """
        to_import = '%s.%s' % (path, name)
        return __import__(to_import, fromlist=[name])

    def validate_role(self):
        """Return True if a role is importable.

        :return: ``bol``
        """
        try:
            self.load_role()
        except genastack.CantContinue:
            return False
        else:
            return True

    def load_all_roles(self, plugin_dir=None):
        if plugin_dir is None:
            plugin_dir = os.path.join(os.getenv('HOME'), 'genastack_roles')

        modules = pkgutil.iter_modules(path=[plugin_dir])
        for loader, name, ispkg in modules:
            if ispkg is True:
                try:
                    module_desc = imp.find_module(name, [plugin_dir])
                    method = imp.load_module(name, *module_desc)
                    LOG.info('Loading Role [ %s ]' % name)
                    yield method.BUILD_DATA
                except Exception as exp:
                    msg = 'role [ %s ] failed to load, error [ %s ]' % (
                        name, exp
                    )
                    LOG.error(msg)
                    raise genastack.CantContinue(msg)

    def load_role(self, plugin_dir=None):
        """Return role dictionary map if it is importable.

        :return: ``dict``
        """
        if plugin_dir is None:
            plugin_dir = os.path.join(os.getenv('HOME'), 'genastack_roles')

        modules = pkgutil.iter_modules(path=[plugin_dir])
        for loader, name, ispkg in modules:
            if ispkg is True:
                try:
                    module_desc = imp.find_module(name, [plugin_dir])
                    method = imp.load_module(name, *module_desc)
                    self.config_type = self.config_type.replace('-', '_')
                    if self.config_type in method.BUILD_DATA:
                        LOG.info('Loading Role [ %s ]' % name)
                        return method.BUILD_DATA[self.config_type]
                except Exception:
                    msg = 'role [ %s ] failed to load correctly' % name
                    LOG.error(msg)
                    raise genastack.CantContinue(msg)
        else:
            msg = 'no role [ %s ] found' % self.config_type
            LOG.warn(msg)
            raise genastack.CantContinue(msg)
