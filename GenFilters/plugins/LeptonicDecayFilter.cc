#include "Samples/GenFilters/plugins/LeptonicDecayFilter.h"
#include <iostream>

using namespace edm;
using namespace std;

LeptonicDecayFilter::LeptonicDecayFilter(const edm::ParameterSet& iConfig): 
  genParticlesToken_(consumes<reco::GenParticleCollection>(iConfig.getParameter<InputTag>("src"))),
  //lheEventToken_(consumes<LHEEventProduct>(iConfig.getParameter<InputTag>("src"))),
  minLeptonicWs_ (iConfig.getParameter<int>("minLeptonicWs")),
  minLeptonicZs_ (iConfig.getParameter<int>("minLeptonicZs")){
    }

LeptonicDecayFilter::~LeptonicDecayFilter() {}

bool LeptonicDecayFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  int nleptonicWs(0), nleptonicZs(0);

  // read genParticles
  Handle<reco::GenParticleCollection> genParsHandle;
  //iEvent.getByLabel(src_, genParsHandle);

  iEvent.getByToken(genParticlesToken_, genParsHandle);

  vector<reco::GenParticle> genPars = *genParsHandle;

  for (uint32_t ig = 0; ig < genPars.size(); ig++) {

    reco::GenParticle gp = genPars.at(ig);

    if (abs(gp.pdgId()) == 11 or abs(gp.pdgId()) == 13 or abs(gp.pdgId()) == 15) {
        if (abs(gp.mother(0)->pdgId())==24) {
            nleptonicWs++;
            continue;
        }
        if (abs(gp.mother(0)->pdgId())==23 and gp.pdgId()>0) {
            nleptonicZs++;
            continue;
        }
        //cout<<gp.pdgId()<<" "<<gp.status()<<" "<<gp.numberOfMothers()<<" "<<gp.mother(0)<<" "<<gp.mother(0)->pdgId()<<endl;
    }
  }
    //if (gp.numberOfDaughters()!=2) continue;
//    if (abs(gp.pdgId()) == 24) {
//        cout<<gp.pdgId()<<" "<<gp.numberOfDaughters()<<" "<<gp.daughter(0)<<" "<<gp.daughter(1)<<endl;
////        if (( abs(gp.daughter(0)->pdgId())>=11 ) and ( abs(gp.daughter(0)->pdgId())<= 16)) {
////            nleptonicWs++;
////            continue;
////        }
//    }
//    if (abs(gp.pdgId()) == 23) {
//        cout<<gp.pdgId()<<" "<<gp.numberOfDaughters()<<" "<<gp.daughter(0)<<" "<<gp.daughter(1)<<endl;
////        if (( abs(gp.daughter(0)->pdgId())>=11 ) and ( abs(gp.daughter(0)->pdgId())<= 16)) {
////            nleptonicZs++;
////            continue;
////        }
//    }
//  }

//  Handle<LHEEventProduct> lhe;
//  iEvent.getByToken(lheEventToken_, lhe);
//
//  const lhef::HEPEUP hepeup_ = lhe->hepeup();
//
//  const int nup_ = hepeup_.NUP;
//  const std::vector<int> idup_ = hepeup_.IDUP;
//  const std::vector<std::pair<int, int> > mothup_ = hepeup_.MOTHUP;
//  const std::vector<lhef::HEPEUP::FiveVector> pup_ = hepeup_.PUP;
//
//  for (unsigned int icount = 0; icount < (unsigned int)nup_; icount++) {
//    if (std::abs(idup_[icount]) == 13) {
//      if (mothup_[icount].first != 0) {
//        if (idup_[mothup_[icount].first - 1] == 23) {
//          nleptonicZs++;
//        }
//        if (abs(idup_[mothup_[icount].first - 1]) == 24) {
//          nleptonicWs++;
//        }
//      }
//    }
//  }

 // cout<<endl;
  //cout<<"W/Z"<<nleptonicWs<<" "<<nleptonicZs<<endl;

  return ( nleptonicWs >= minLeptonicWs_ ) and (nleptonicZs >= minLeptonicZs_);

}
//define this as a plug-in
DEFINE_FWK_MODULE(LeptonicDecayFilter);
