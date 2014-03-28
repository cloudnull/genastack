# =============================================================================
# Copyright [2013] [Kevin Carter]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================

BUILD_DATA = {
    'glance_registry': {
        'help': 'Install Glance-Registry from upstream',
        'required': [
            'python',
            'glance',
            'glance_client'
        ],
        'init_script': [
            {
                'help': 'Start and stop glance on boot',
                'init_path': '/etc/init.d',
                'name': 'glance-registry',
                'chuid': 'glance',
                'chdir': '/var/lib/glance',
                'program': 'glance-registry'
            }
        ]
    }
}
