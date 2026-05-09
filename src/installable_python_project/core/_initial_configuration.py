from configparser import ConfigParser, SectionProxy

from ._resources import _INITIAL_CONFIGURATION_FILE_PATH

_CONFIG_PARSER: ConfigParser = ConfigParser()
_CONFIG_PARSER.read(_INITIAL_CONFIGURATION_FILE_PATH)


_APP_SECTION: SectionProxy = _CONFIG_PARSER["App"]


_APP_NAME: str = _APP_SECTION["name"]
_APP_AUTHOR: str = _APP_SECTION["author"]
