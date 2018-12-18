# MetFilter Analysis Recommendations according to https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2

def getFilterCut( year, isData=False, ignoreJSON=False ):
    if year == 2016:
        filters             = [ "Flag_goodVertices" ]                         # primary vertex filter
        filters            += [ "Flag_globalSuperTightHalo2016Filter" ]       # beam halo filter
        filters            += [ "Flag_HBHENoiseFilter" ]                      # HBHE noise filter
        filters            += [ "Flag_HBHENoiseIsoFilter" ]                   # HBHEiso noise filter
        filters            += [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ]   # ECAL TP filter
#        filters            += [ "Flag_BadPFMuonFilter" ]                      # Bad PF Muon Filter
#        filters            += [ "Flag_BadChargedCandidateFilter" ]            # Bad Charged Hadron Filter
        if isData:
            filters        += [ "Flag_eeBadScFilter" ]                        # ee badSC noise filter (data only)

    elif year == 2017:
        filters             = [ "Flag_goodVertices" ]                         # primary vertex filter
        filters            += [ "Flag_globalSuperTightHalo2016Filter" ]       # beam halo filter
        filters            += [ "Flag_HBHENoiseFilter" ]                      # HBHE noise filter
        filters            += [ "Flag_HBHENoiseIsoFilter" ]                   # HBHEiso noise filter
        filters            += [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ]   # ECAL TP filter
        filters            += [ "Flag_BadPFMuonFilter" ]                      # Bad PF Muon Filter
        filters            += [ "Flag_BadChargedCandidateFilter" ]            # Bad Charged Hadron Filter
        filters            += [ "ecalBadCalibReducedMINIAODFilter" ]          # ECAL bad calibration filter update (neeeds to be re-run on miniAOD)
        if isData:
            filters        += [ "Flag_eeBadScFilter" ]                        # ee badSC noise filter (data only)

    elif year == 2018:
        filters             = [ "Flag_goodVertices" ]                         # primary vertex filter
        filters            += [ "Flag_globalSuperTightHalo2016Filter" ]       # beam halo filter
        filters            += [ "Flag_HBHENoiseFilter" ]                      # HBHE noise filter
        filters            += [ "Flag_HBHENoiseIsoFilter" ]                   # HBHEiso noise filter
        filters            += [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ]   # ECAL TP filter
        filters            += [ "Flag_BadPFMuonFilter" ]                      # Bad PF Muon Filter
        filters            += [ "Flag_BadChargedCandidateFilter" ]            # Bad Charged Hadron Filter
        filters            += [ "ecalBadCalibReducedMINIAODFilter" ]          # ECAL bad calibration filter update (neeeds to be re-run on miniAOD)
        if isData:
            filters        += [ "Flag_eeBadScFilter" ]                        # ee badSC noise filter (data only)

    if isData:
        filters            += [ "weight>0" ]
        if not ignoreJSON:
            filters        += [ "jsonPassed>0" ]

    return "&&".join(filters)
