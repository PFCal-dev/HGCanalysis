import FWCore.ParameterSet.Config as cms

analysis = cms.EDAnalyzer("HGCROIAnalyzer",
                          useStatus3ForGenVertex = cms.untracked.bool(False),
                          g4TracksSource   = cms.untracked.string('g4SimHits'),
                          g4VerticesSource = cms.untracked.string('g4SimHits'),
                          genSource        = cms.untracked.string("genParticles"),
                          genCandsFromSimTracksSource = cms.untracked.string('genCandsFromSimTracks'),
                          genJetsSource    = cms.untracked.string("ak4GenJets"),
                          useSuperClustersAsROIs = cms.untracked.bool(True),
                          superClustersSource = cms.untracked.string("particleFlowSuperClusterHGCEE"),
                          pfJetsSource     = cms.untracked.string("ak4PFJets"),
                          recoVertexSource = cms.untracked.string('offlinePrimaryVertices'),
                          eeSimHitsSource  = cms.untracked.string('HGCHitsEE'),
                          eeRecHitsSource  = cms.untracked.string('HGCEERecHits'),
                          hefSimHitsSource = cms.untracked.string('HGCHitsHEfront'),
                          hefRecHitsSource = cms.untracked.string('HGCHEFRecHits')
                          )

