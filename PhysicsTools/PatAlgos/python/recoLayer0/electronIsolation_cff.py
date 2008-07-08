import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaIsolationAlgos.egammaIsoDeposits_cff import *
from RecoEgamma.EgammaIsolationAlgos.egammaSuperClusterMerger_cfi import *
from RecoEgamma.EgammaIsolationAlgos.egammaBasicClusterMerger_cfi import *

# define module labels for old (tk-based isodeposit) POG isolation
patAODElectronIsolationLabels = cms.VInputTag(
        cms.InputTag("eleIsoDepositTk"),
        cms.InputTag("eleIsoDepositEcalFromHits"),
        cms.InputTag("eleIsoDepositHcalFromHits"),
     #  cms.InputTag("eleIsoDepositEcalFromClusts"),       # try these two if you want to compute them from AOD
     #  cms.InputTag("eleIsoDepositHcalFromTowers"),       # instead of reading the values computed in RECO
      # cms.InputTag("eleIsoDepositEcalSCVetoFromClust"), # somebody might want this one for ECAL instead
)

# read and convert to ValueMap<IsoDeposit> keyed to Candidate
patAODElectronIsolations = cms.EDFilter("MultipleIsoDepositsToValueMaps",
    collection   = cms.InputTag("pixelMatchGsfElectrons"),
    associations = patAODElectronIsolationLabels,
)

# re-key ValueMap<IsoDeposit> to Layer 0 output
layer0ElectronIsolations = cms.EDFilter("CandManyValueMapsSkimmerIsoDeposits",
    collection   = cms.InputTag("allLayer0Electrons"),
    backrefs     = cms.InputTag("allLayer0Electrons"),
    commonLabel  = cms.InputTag("patAODElectronIsolations"),
    associations = patAODElectronIsolationLabels,
)

# selecting POG modules that can run on top of AOD
eleIsoDepositAOD = cms.Sequence( eleIsoDepositTk * eleIsoDepositEcalFromClusts * eleIsoDepositHcalFromTowers)

# sequence to run on AOD before PAT
patAODElectronIsolation = cms.Sequence(
        ## egammaSuperClusterMerger *  ## Not needed and no longer working (can't find input data)
        ## egammaBasicClusterMerger *  ## Not needed any more
        ## eleIsoDepositAOD *          ## Not needed any more, we use values from RECO
        patAODElectronIsolations)

# sequence to run after the PAT cleaners
patLayer0ElectronIsolation = cms.Sequence(layer0ElectronIsolations)

