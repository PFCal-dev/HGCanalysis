import FWCore.ParameterSet.Config as cms

process.hgcSimHitsAnalyzer = cms.EDAnalyzer("HGCSimHitsAnalyzer",
                                            saveGenParticles = cms.untracked.bool(True),
                                            genSource        = cms.untracked.string("genParticles"),
                                            saveG4           = cms.untracked.bool(True),
                                            g4TracksSource   = cms.untracked.string('g4SimHits'),
                                            g4VerticesSource = cms.untracked.string('g4SimHits'),
                                            saveTkExtrapol   = cms.untracked.bool(True),
                                            trackSource      = ms.untracked.string('generalTracks'),
                                            geometrySource   = cms.untracked.vstring('HGCalEESensitive','HGCalHESiliconSensitive',  'HGCalHEScintillatorSensitive'),
                                            hitCollections   = cms.untracked.vstring('HGCHitsEE',       'HGCHitsHEfront',           'HGCHitsHEback'               ),
                                            digiCollections  = cms.untracked.vstring('HGCDigisEE',      'HGCDigisHEfront',          'HGCDigisHEback'              )
                                            )
