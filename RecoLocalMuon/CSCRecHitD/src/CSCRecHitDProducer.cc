#include <RecoLocalMuon/CSCRecHitD/src/CSCRecHitDProducer.h>
#include <RecoLocalMuon/CSCRecHitD/src/CSCRecHitDBuilder.h>
#include <RecoLocalMuon/CSCRecHitD/src/CSCRecoConditions.h>

#include <FWCore/Framework/interface/Frameworkfwd.h>
#include <FWCore/Framework/interface/EDProducer.h>
#include <FWCore/Framework/interface/Event.h>
#include <FWCore/Framework/interface/MakerMacros.h>
#include <DataFormats/Common/interface/Handle.h>
#include <FWCore/Framework/interface/ESHandle.h>
#include <FWCore/ParameterSet/interface/ParameterSet.h>
#include <FWCore/Utilities/interface/Exception.h>
#include <FWCore/MessageLogger/interface/MessageLogger.h>

#include <Geometry/Records/interface/MuonGeometryRecord.h>

#include <DataFormats/CSCRecHit/interface/CSCRecHit2DCollection.h>
#include <DataFormats/CSCDigi/interface/CSCStripDigiCollection.h>
#include <DataFormats/CSCDigi/interface/CSCWireDigiCollection.h>


CSCRecHitDProducer::CSCRecHitDProducer( const edm::ParameterSet& ps ) : iRun( 0 ) {
	
  stripDigiProducer_ = ps.getParameter<std::string>("CSCStripDigiProducer");
  wireDigiProducer_  = ps.getParameter<std::string>("CSCWireDigiProducer");
  useCalib           = ps.getUntrackedParameter<bool>("CSCUseCalibrations");
  debug              = ps.getUntrackedParameter<bool>("CSCDebug");
  
  recHitBuilder_     = new CSCRecHitDBuilder( ps ); // pass on the Parameter Settings
  recoConditions_    = new CSCRecoConditions( ps ); // access to conditions data

  recHitBuilder_->setConditions( recoConditions_ ); // pass down to who needs access
  
  // register what this produces
  produces<CSCRecHit2DCollection>();

}

CSCRecHitDProducer::~CSCRecHitDProducer()
{
  delete recHitBuilder_;
  delete recoConditions_;
}


void  CSCRecHitDProducer::produce( edm::Event& ev, const edm::EventSetup& setup )
{
  // find the geometry for this event & cache it in the builder
  edm::ESHandle<CSCGeometry> h;
  setup.get<MuonGeometryRecord>().get( h );
  const CSCGeometry* pgeom = &*h;
  recHitBuilder_->setGeometry( pgeom );

  // access conditions data for this event 
  if ( useCalib ) {  
    recoConditions_->initializeEvent( setup ); 
  }
	
  // Get the collections of strip & wire digis from event
  edm::Handle<CSCStripDigiCollection> stripDigis;
  edm::Handle<CSCWireDigiCollection> wireDigis;
  ev.getByLabel(stripDigiProducer_, "MuonCSCStripDigi", stripDigis);
  ev.getByLabel(wireDigiProducer_,  "MuonCSCWireDigi",  wireDigis);

  // Create empty collection of rechits
  std::auto_ptr<CSCRecHit2DCollection> oc( new CSCRecHit2DCollection );


  // Fill the CSCRecHit2DCollection
  recHitBuilder_->build( stripDigis.product(), wireDigis.product(),*oc);


  // Put collection in event
  if (debug) std::cout << "Will output rechits collection to event" << std::endl;
  ev.put( oc );

}

//define this as a plug-in
DEFINE_FWK_MODULE(CSCRecHitDProducer);

