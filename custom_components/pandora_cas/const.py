from typing import Final

from homeassistant.const import Platform

# Domain data
DOMAIN: Final = "pandora_cas"
PLATFORMS: Final = (
    Platform.BINARY_SENSOR,
    Platform.BUTTON,
    Platform.DEVICE_TRACKER,
    Platform.LOCK,
    Platform.SENSOR,
    Platform.SWITCH,
)

# Global data placeholders
DATA_LISTENERS: Final = DOMAIN + "_listeners"

# Configuration parameters
CONF_COORDINATES_DEBOUNCE: Final = "coordinates_debounce"
CONF_CUSTOM_CURSORS: Final = "custom_cursors"
CONF_CUSTOM_CURSOR_DEVICES: Final = "custom_cursor_devices"
CONF_CUSTOM_CURSOR_TYPE: Final = "custom_cursor_type"
CONF_DISABLE_POLLING: Final = "disable_polling"
CONF_DISABLE_WEBSOCKETS: Final = "disable_websockets"
CONF_FUEL_IS_LITERS: Final = "fuel_is_liters"
CONF_IGNORE_WS_COORDINATES: Final = "ignore_ws_coordinates"
CONF_MILEAGE_CAN_MILES: Final = "mileage_can_miles"
CONF_MILEAGE_MILES: Final = "mileage_miles"
CONF_OFFLINE_AS_UNAVAILABLE: Final = "offline_as_unavailable"
CONF_RPM_COEFFICIENT: Final = "rpm_coefficient"
CONF_RPM_OFFSET: Final = "rpm_offset"
CONF_ENGINE_STATE_BY_RPM: Final = "engine_state_by_rpm"

DEFAULT_COORDINATES_SMOOTHING: Final = 10.0
DEFAULT_CURSOR_TYPE: Final = "default"
DISABLED_CURSOR_TYPE: Final = "disabled"

# Entity & event attributes
ATTR_CARDINAL: Final = "cardinal"
ATTR_COMMAND_ID: Final = "command_id"
ATTR_DEVICE_ID: Final = "device_id"
ATTR_GSM_LEVEL: Final = "gsm_level"
ATTR_KEY_NUMBER: Final = "key_number"
ATTR_PHONE_NUMBER: Final = "phone_number"
ATTR_ROTATION: Final = "rotation"
ATTR_TAG_NUMBER: Final = "tag_number"

# Home Assistant bus event identifiers
EVENT_TYPE_COMMAND: Final = DOMAIN + "_command"
EVENT_TYPE_EVENT: Final = DOMAIN + "_event"
EVENT_TYPE_POINT: Final = DOMAIN + "_point"
