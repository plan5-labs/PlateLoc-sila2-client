import time
import sys
import yaml

from pathlib import Path

from plateloc_controller import Client as PlateLocClient
from plateloc_controller.generated.plateloccontroller import CommandIsRunning, NotInitialized, CommandExecutionAborted, InstrumentErrorOccurred, InvalidInstrumentStatusError

with open("config.yml", 'r') as file:
    config = yaml.safe_load(file)

host, port, cert = config["PlateLoc"]["host"], config["PlateLoc"]["port"], config["PlateLoc"]["cert_path"]
print(f"Connect to PlateLoc Server. host: {host} port: {port} cert file: {cert}")
plateloc_client = PlateLocClient(host, port, root_certs=Path(cert).read_bytes())

#region StartCycle command
print("StartCycle command start!")
start_cycle_instance = plateloc_client.PlateLocController.StartCycle()
while not start_cycle_instance.done:
    time.sleep(1)
    print("StartCycle command is still running...")
print("StartCycle command complete!")

try:
    start_cycle_instance.get_responses()
    print("StartCycle succeeded.")
except CommandIsRunning:
    print("Command is running.")
    sys.exit()
except NotInitialized:
    print("PlateLoc is not initialized.")
    sys.exit()
except CommandExecutionAborted:
    print("Command execution aborted for some reasons.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region StopCycle command
print("StopCycle command start!")
stop_cycle_instance = plateloc_client.PlateLocController.StartCycle()
while not stop_cycle_instance.done:
    time.sleep(1)
    print("StopCycle command is still running...")
print("StopCycle command complete!")

try:
    stop_cycle_instance.get_responses()
    print("StopCycle succeeded.")
except NotInitialized:
    print("PlateLoc is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region SetSealingTime command
print("SetSealingTime command start!")
try:
    set_sealing_time_response = plateloc_client.PlateLocController.SetSealingTime(3)
    print("SetSealingTime command complete!")
    print("SetSealingTime succeeded.")
except NotInitialized:
    print("PlateLoc is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region SetSealingTemperature command
print("SetSealingTemperature command start!")
try:
    set_sealing_temperature_response = plateloc_client.PlateLocController.SetSealingTemperature(150)
    print("SetSealingTemperature command complete!")
    print("SetSealingTemperature succeeded.")
except NotInitialized:
    print("PlateLoc is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region Reset command
print("Reset command start!")
reset_instance = plateloc_client.PlateLocController.StartCycle()
while not reset_instance.done:
    time.sleep(1)
    print("Reset command is still running...")
print("Reset command complete!")

try:
    reset_instance.get_responses()
    print("Reset succeeded.")
except NotInitialized:
    print("PlateLoc is not initialized.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region EnumerateProfiles command
print("EnumerateProfiles command start!")
try:
    enumerate_profiles_response = plateloc_client.PlateLocController.EnumerateProfiles()
    print("EnumerateProfiles command complete!")
    print(f"EnumerateProfiles succeeded. Profiles: {', '.join(enumerate_profiles_response.ProfileNames)}")
except NotInitialized:
    print("PlateLoc is not initialized.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region SealingTemperature property
try:
    print(f"Current sealing temperature: {plateloc_client.PlateLocController.SealingTemperature.get()}")
except NotInitialized:
    print("PlateLoc is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region SealingTime property
try:
    print(f"Current sealing time: {plateloc_client.PlateLocController.SealingTime.get()}")
except NotInitialized:
    print("PlateLoc is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region ActualTemperature property
try:
    print(f"Current actual temperature: {plateloc_client.PlateLocController.ActualTemperature.get()}")
except NotInitialized:
    print("PlateLoc is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region CycleCount property
try:
    print(f"Current cycle count: {plateloc_client.PlateLocController.CycleCount.get()}")
except NotInitialized:
    print("PlateLoc is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region FirmwareVersion property
try:
    print(f"Firmware version: {plateloc_client.PlateLocController.FirmwareVersion.get()}")
except NotInitialized:
    print("PlateLoc is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region Version property
try:
    print(f"Version: {plateloc_client.PlateLocController.Version.get()}")
except NotInitialized:
    print("PlateLoc is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region Status property
print("Subscribe Status property start.")
print(f"Current status: {plateloc_client.PlateLocController.Status.get()}")
status_subscription = plateloc_client.PlateLocController.Status.subscribe()

print("New status:")
status_subscription.add_callback(print)

time.sleep(5)

status_subscription.cancel()
print("Subscribe Status property complete.")
#endregion