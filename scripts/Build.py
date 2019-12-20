import subprocess
import shutil
import os

# Setting general environment variables
# Path variables for tools that are local to the build environment
PATH_AS45 = "C:/BrAutomation/AS45/"
PATH_AS = "C:/BrAutomation/AS/"
PATH_PVI45 = "C:/BrAutomation/PVI/V4.5/"
PATH_TEMP = "C:/BuildEngine/Temp/"
PATH_SCRIPTS = "C:/BuildEngine/Scripts/"
PATH_CHROME = "C:/Program Files (x86)/Google/Chrome/Application/"

# Project specific variables
PATH_PROJECT = os.environ["WORKSPACE"] + '/'
NAME_PROJECT = "CITest.apj"
NAME_HMI = "ci-test"
CONFIG = "ARsim"
CPU = "PC"
AR_VERSION = "D4.52"
AR_VERSION_STRING = "D0452"
CONFIG_ID = "ci-test"
CONFIG_VERSION = "1.0.0"

# Support functions
def Build():
	argList = []
	# C:\BrAutomation\AS45\Bin-en\BR.AS.Build.exe
	argList.append(PATH_AS45 + "Bin-en/BR.AS.Build.exe")
	# ***
	argList.append(PATH_PROJECT + NAME_PROJECT)
	# -c Config1
	argList.append("-c")
	argList.append(CONFIG)
	# -buildMode "Rebuild"
	argList.append("-buildMode")
	argList.append("Rebuild")
	# -all
	argList.append("-all")
	# -simulation
	argList.append("-simulation")
	subprocess.run(argList)
	
def CreateRUC():
	argList = []
	# C:\BrAutomation\AS45\Bin-en\BR.AS.RUCPackageCreator.exe
	argList.append(PATH_AS45 + "Bin-en/BR.AS.RUCPackageCreator.exe")
	# -o ***.zip
	argList.append("-o")
	argList.append(PATH_TEMP + "RUCPackage.zip")
	# -include ***
	argList.append("-include")
	argList.append(PATH_PROJECT + "Binaries/" + CONFIG + "/" + CPU + "/")
	# -f ***.lst
	argList.append("-f")
	argList.append(PATH_PROJECT + "Binaries/" + CONFIG + "/" + CPU + "/Transfer.lst")
	# -systemDirectory ***
	argList.append("-systemDirectory")
	argList.append(PATH_AS + "System/" + AR_VERSION_STRING + "/SG4/IA32/")
	# -d ***
	argList.append("-d")
	argList.append(PATH_PROJECT + "Temp/Transfer/" + CONFIG + "/" + CPU + "/FilesToTransfer/")
	# -configurationId ***
	argList.append("-configurationId")
	argList.append(CONFIG_ID)
	# -configurationVersion *.*.*
	argList.append("-configurationVersion")
	argList.append(CONFIG_VERSION)
	# -v **.**
	argList.append("-v")
	argList.append(AR_VERSION)
	# -S AR000
	argList.append("-S")
	argList.append("AR000")
	# -moduleSystem SAFE
	argList.append("-moduleSystem")
	argList.append("SAFE")
	# -OrderNumber ***
	argList.append("-OrderNumber")
	argList.append(CPU) # *** evidently this has to be the name of the PLC folder in the Configuration ***
	# -loggerModuleSize 819200
	argList.append("-loggerModuleSize")
	argList.append("819200")
	# -userPartitionSize 0
	argList.append("-userPartitionSize")
	argList.append("0")
	# -RuntimeType ARSim
	argList.append("-RuntimeType")
	argList.append("ARSim")
	# -compatibleCpuCode ARSim
	argList.append("-compatibleCpuCode")
	argList.append("")
	# -C "/IF=COM1 /BD=57600 /PA=2 /IT=20 /RS=0 /RT=1000 /AM=*"
	argList.append("-C")
	argList.append("/IF=COM1 /BD=57600 /PA=2 /IT=20 /RS=0 /RT=1000 /AM=*")
	subprocess.run(argList)
	
def StopARSim():
	print("Stopping ARSim...")
	try:
		subprocess.run(PATH_TEMP + "Simulation/ar000stop.exe")
	except OSError as e:
		print("No ARSim running.")
	
def RefreshTempFolder():
	print("Recreating simulation folder...")
	# Try to delete the folder and all of its contents
	try:
		shutil.rmtree(PATH_TEMP)
	except OSError as e:
		print("No temp folder present.")
	# Recreate the folder
	os.mkdir(PATH_TEMP)
	
def OfflineInstall():
	print("Initiating offline install...")
	argList = []
	# C:\BrAutomation\PVI\V4.5\PVI\Tools\PVITransfer\PVITransfer.exe
	argList.append(PATH_PVI45 + "PVI/Tools/PVITransfer/PVITransfer.exe")
	# -automatic
	argList.append("-automatic")
	# ***.pil
	argList.append("-" + PATH_SCRIPTS + "OfflineInstall.pil")
	# -consoleOutput 
	# argList.append("-consoleOutput")
	subprocess.run(argList)	

# STEP 1: First we stop the ARsim instance if it's running
StopARSim()

# STEP 2: Next we refresh the existing simulation folder by deleting and recreating it (empty)
# RefreshTempFolder()	
	
# STEP 3: Build the project for simulated target
Build()

# STEP 4: Create RUC package
CreateRUC()

print("Done")

