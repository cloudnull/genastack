# =============================================================================
# Copyright [2013] [Kevin Carter]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
from genastack import roles


BIN_PATH = roles.return_rax_dir('bin')


BRANCH = 'stable/havana'


PROJECT_URL = 'https://raw.github.com/openstack/keystone/%s' % BRANCH
URL_PATH = '%s/etc' % PROJECT_URL


KEYSTONE_CONF = '%s/keystone.conf.sample' % URL_PATH
KEYSTONE_PASTE = '%s/keystone-paste.ini' % URL_PATH
KEYSTONE_LOGGING = '%s/logging.conf.sample' % URL_PATH
KEYSTONE_POLICY_JSON = '%s/policy.json' % URL_PATH
KEYSTONE_POLICY_JSON_V3API = '%s/policy.v3cloudsample.json' % URL_PATH


BUILD_DATA = {
    'keystone': {
        'help': 'Install Keystone from upstream on Branch "%s"' % BRANCH,
        'required': [
            'python',
            'keystone_client'
        ],
        'directories': [
            {
                'path': '/etc/keystone',
                'user': 'root',
                'group': 'root',
                'mode': 0755
            },
        ],
        'file_create': [
            {
                'path': '/etc/keystone',
                'name': 'keystone.conf',
                'from_remote': KEYSTONE_CONF,
                'user': 'root',
                'group': 'root',
                'mode': 0644
            },
            {
                'path': '/etc/keystone',
                'name': 'keystone-paste.ini',
                'from_remote': KEYSTONE_PASTE,
                'user': 'root',
                'group': 'root',
                'mode': 0644
            },
            {
                'path': '/etc/keystone',
                'name': 'logging.conf.sample',
                'from_remote': KEYSTONE_LOGGING,
                'user': 'root',
                'group': 'root',
                'mode': 0644
            },
            {
                'path': '/etc/keystone',
                'name': 'policy.json',
                'from_remote': KEYSTONE_POLICY_JSON,
                'user': 'root',
                'group': 'root',
                'mode': 0644
            },
            {
                'path': '/etc/keystone',
                'name': 'policy.v3cloudsample.json',
                'from_remote': KEYSTONE_POLICY_JSON_V3API,
                'user': 'root',
                'group': 'root',
                'mode': 0644
            }
        ],
        'pip_install': {
            'pip_bin': '%s/pip' % BIN_PATH,
            'pip_packages': [
                'git+https://github.com/openstack/keystone.git@stable/havana'
            ],
        },
        'packages': {
            'apt': [
                'debhelper',
                'dh-apparmor',
                'docutils-common',
                'libjs-sphinxdoc',
                'libjs-underscore'
            ]
        }
    }
}
