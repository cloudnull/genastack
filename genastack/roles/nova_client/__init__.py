# =============================================================================
# Copyright [2013] [Kevin Carter]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
from genastack.common import utils


BIN_PATH = utils.return_rax_dir('bin')


BRANCH = '2.17.0'


PROJECT_URL = 'https://github.com/openstack'
CLIENT = '%s/python-novaclient.git' % PROJECT_URL


BUILD_DATA = {
    'nova_client': {
        'help': 'Install Nova client from upstream, Branch "%s"' % BRANCH,
        'pip_install': [
            'git+%s@%s' % (CLIENT, BRANCH)
        ]
    }
}