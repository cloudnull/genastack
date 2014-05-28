# =============================================================================
# Copyright [2013] [Kevin Carter]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
__author__ = "Kevin Carter"
__contact__ = "kevin.carter@rackspace.com"
__email__ = "kevin.carter@RACKSPACE.COM"
__copyright__ = "2013 All Rights Reserved"
__version__ = "0.0.3"
__status__ = "BETA"
__url__ = "https://github.com/cloudnull/genastack"
__appname__ = "genastack"
__license__ = 'GNU General Public License v3 or later (GPLv3+)'
__description__ = 'Install Openstack from source in an Automated fashion'
__urlinformation__ = ""


class CantContinue(Exception):
    """Exception class when the application can't continue."""
    pass

