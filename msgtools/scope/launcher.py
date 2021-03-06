import pkg_resources
import collections

def info():
    LauncherInfo = collections.namedtuple('LauncherInfo', ['icon_text', 'program_name', 'icon_filename'])
    return LauncherInfo('scope', 'msgscope', pkg_resources.resource_filename('msgtools', 'scope/scope.png'))
