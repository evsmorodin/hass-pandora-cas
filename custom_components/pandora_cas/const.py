from typing import Final

DOMAIN: Final = "pandora_cas"
PANDORA_COMPONENTS: Final = (
    "binary_sensor",
    "sensor",
    "switch",
    "lock",
    "device_tracker",
)
DATA_CONFIG: Final = DOMAIN + "_config"
DATA_UPDATERS: Final = DOMAIN + "_updaters"
DATA_DEVICE_ENTITIES: Final = DOMAIN + "_device_entities"
DATA_UPDATE_LISTENERS: Final = DOMAIN + "_update_listeners"
DATA_FINAL_CONFIG: Final = DOMAIN + "_final_config"
CONF_READ_ONLY: Final = "read_only"
CONF_NAME_FORMAT: Final = "name_format"
ATTR_DEVICE_ID: Final = "device_id"
ATTR_COMMAND_ID: Final = "command_id"
ATTR_ATTRIBUTE: Final = "attribute"
ATTR_ATTRIBUTE_SOURCE: Final = "attribute_source"
ATTR_FLAG: Final = "flag"
ATTR_STATE_SENSITIVE: Final = "state_sensitive"
ATTR_FORMATTER: Final = "formatter"
ATTR_INVERSE: Final = "inverse"
ATTR_FEATURE: Final = "feature"
ATTR_DEFAULT: Final = "default"
DEFAULT_NAME_FORMAT: Final = "{device_name} {type_name}"
ATTR_GSM_LEVEL: Final = "gsm_level"
ATTR_DIRECTION: Final = "direction"
ATTR_CARDINAL: Final = "cardinal"
ATTR_KEY_NUMBER: Final = "key_number"
ATTR_TAG_NUMBER: Final = "tag_number"
ATTR_DISABLED_BY_DEFAULT: Final = "disabled_by_default"

CONF_RPM_COEFFICIENT: Final = "rpm_coefficient"
CONF_RPM_OFFSET: Final = "rpm_offset"

DEFAULT_RPM_COEFFICIENT: Final = 1.0
DEFAULT_RPM_OFFSET: Final = 0.0
