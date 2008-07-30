import FWCore.ParameterSet.Config as cms

from DQM.EcalBarrelMonitorTasks.EBBeamCaloTask_cfi import *
from DQM.EcalBarrelMonitorTasks.EBBeamHodoTask_cfi import *
from DQM.EcalBarrelMonitorTasks.EBClusterTask_cfi import *
from DQM.EcalBarrelMonitorTasks.EBCosmicTask_cfi import *
from DQM.EcalBarrelMonitorTasks.EBIntegrityTask_cfi import *
from DQM.EcalBarrelMonitorTasks.EBLaserTask_cfi import *
from DQM.EcalBarrelMonitorTasks.EBOccupancyTask_cfi import *
from DQM.EcalBarrelMonitorTasks.EBPedestalOnlineTask_cfi import *
from DQM.EcalBarrelMonitorTasks.EBPedestalTask_cfi import *
from DQM.EcalBarrelMonitorTasks.EBStatusFlagsTask_cfi import *
from DQM.EcalBarrelMonitorTasks.EBTestPulseTask_cfi import *
from DQM.EcalBarrelMonitorTasks.EBTimingTask_cfi import *
from DQM.EcalBarrelMonitorTasks.EBTriggerTowerTask_cfi import *

ecalBarrelOccupancyTask.enableCleanup = True
ecalBarrelIntegrityTask.enableCleanup = True

ecalBarrelStatusFlagsTask.enableCleanup = True

ecalBarrelCosmicTask.enableCleanup = True
ecalBarrelLaserTask.enableCleanup = True
ecalBarrelPedestalOnlineTask.enableCleanup = True
ecalBarrelPedestalTask.enableCleanup = True
ecalBarrelTestPulseTask.enableCleanup = True

ecalBarrelTriggerTowerTask.enableCleanup = True
ecalBarrelTimingTask.enableCleanup = True

ecalBarrelBeamHodoTask.enableCleanup = True
ecalBarrelBeamCaloTask.enableCleanup = True

ecalBarrelClusterTask.enableCleanup = True

