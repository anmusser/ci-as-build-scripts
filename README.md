
# ci-as-build-scripts
Scripts for automating Automation Studio builds and installs

## Settings for Build.py

> 👉 It is suggested to first ceate a RUC package inside Automation Studio to have it generate the core settings you will need.

Inside Automation Studio go to Project -> Export to Runtime Utility Center, enter a .zip path, and wait for it to export.

Inside the created zip you will find **ProjectInformation.xml** (shown below)

Additionally, this will create the **Transfer.pil** next to your zip file which will contain your connection string.

As the XML below shows, you will not get every value needed by **BR.AS.RUCPackageCreator.exe**, but this will help with the less documented values.

```xml
<?xml version="1.0" encoding="utf-8"?>
<ProjectInformation>
	<ConfigurationID>MyProject_Config1</ConfigurationID>
	<ConfigVersion>1.0.0</ConfigVersion>
	<CPUType>xPC31xx</CPUType>
	<CompatibleCpuCode>5APC3100.KBU3-000</CompatibleCpuCode>
	<OrderNumber>5APC3100.KBU3-000</OrderNumber>
	<RuntimeType>AR Embedded</RuntimeType>
	<ARVersion>A4.73</ARVersion>
	<BRModuleSystem>SAFE</BRModuleSystem>
	<UserPartitionSize>524288000</UserPartitionSize>
	<LoggerModulesSize>1843200</LoggerModulesSize>
	<InstallstickZipPrefix>APCEFI</InstallstickZipPrefix>
</ProjectInformation>

```

Searching the **B&R Help Explorer** for **Creating an RUC package from the command line** will detail the remaing values
