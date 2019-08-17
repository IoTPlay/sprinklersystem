# JR: Load this in GitHub/sprinklersystem/code
Import("env")

# access to global construction environment
#print env

# Dump construction environment (for debug purpose)
#print env.Dump()

# append extra flags to global build environment
# which later will be used to build:
# - project source code
# - frameworks
# - dependent libraries
env.Append(CPPDEFINES=[
  "PIO_FRAMEWORK_ARDUINO_ESPRESSIF_SDK22x",
#  "CONTROLLER_SET_ALL",
  "NOTIFIER_SET_NONE",
#  "PLUGIN_SET_ONLY_SWITCH",
  "USES_P001",  # Switch
  "USES_C014",  # Homie Controller
  "USES_P086",  # Homie Receiver
  "USES_P005",  # DHT22
  "USES_P033",  # Dummy Device

  ("WEBSERVER_RULES_DEBUG", "0")
])
