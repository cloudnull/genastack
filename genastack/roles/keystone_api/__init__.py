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


BUILD_DATA = {
    'keystone_api': {
        'help': 'Install Keystone API from upstream',
        'required': [
            'keystone',
            'keystone_client'
        ],
        'init_script': [
            {
                'help': 'Start and stop keystone on boot',
                'init_path': '/etc/init.d',
                'bin_path': BIN_PATH,
                'name': 'keystone',
                'chuid': 'keystone',
                'chdir': '/var/lib/keystone',
                'program': 'keystone-all'
            }
        ]
    }
}
