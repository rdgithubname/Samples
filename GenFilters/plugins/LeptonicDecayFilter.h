#ifndef LeptonicDecayFilter_h
#define LeptonicDecayFilter_h


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"

class LeptonicDecayFilter : public edm::EDFilter {
public:
  explicit LeptonicDecayFilter(const edm::ParameterSet &);
  ~LeptonicDecayFilter() override;

  bool filter(edm::Event &, const edm::EventSetup &) override;

private:
  edm::EDGetTokenT<reco::GenParticleCollection>   genParticlesToken_;
  //edm::EDGetTokenT<LHEEventProduct>   lheEventToken_;

  int minLeptonicWs_;
  int minLeptonicZs_;

};
#endif
