# =============================================================================
# Copyright [2013] [Kevin Carter]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
from cloudlib import parse_ini

# Check to see if our System Config File Exists
CONFIG = parse_ini.ConfigurationSetup(log_name='genastack-system')
ARGS = CONFIG.config_args(section='glance_client')
BRANCH = ARGS.get('branch', 'master')
PROJECT_URL = ARGS['project_url']


BUILD_DATA = {
    'glance_client': {
        'use_system_python': ARGS.get('use_system_python', False),
        'python_venv': {
            'name': 'glance'
        },
        'help': 'Install Glance-Client from upstream, Branch "%s"' % BRANCH,
        'git_install': [
            {
                'name': 'glance_client',
                'project_url': PROJECT_URL,
                'branch': BRANCH
            }
        ],
    }
}
