'''
dasgoclient -query="dataset=/*/Run2018*17Sep*/MINIAOD"
For A-C
'''


from Samples.Tools.Sample import Sample


DoubleMuon_Run2018A_17Sep2018_v2 = Sample("DoubleMuon_Run2018A_17Sep2018_v2", "/DoubleMuon/Run2018A-17Sep2018-v2/MINIAOD")
DoubleMuon_Run2018B_17Sep2018_v1 = Sample("DoubleMuon_Run2018B_17Sep2018_v1", "/DoubleMuon/Run2018B-17Sep2018-v1/MINIAOD")
DoubleMuon_Run2018C_17Sep2018_v1 = Sample("DoubleMuon_Run2018C_17Sep2018_v1", "/DoubleMuon/Run2018C-17Sep2018-v1/MINIAOD")

DoubleMuon = [
    DoubleMuon_Run2018A_17Sep2018_v2,
    DoubleMuon_Run2018B_17Sep2018_v1,
    DoubleMuon_Run2018C_17Sep2018_v1,
]

MuonEG_Run2018A_17Sep2018_v1 = Sample("MuonEG_Run2018A_17Sep2018_v1", "/MuonEG/Run2018A-17Sep2018-v1/MINIAOD")
MuonEG_Run2018B_17Sep2018_v1 = Sample("MuonEG_Run2018B_17Sep2018_v1", "/MuonEG/Run2018B-17Sep2018-v1/MINIAOD")
MuonEG_Run2018C_17Sep2018_v1 = Sample("MuonEG_Run2018C_17Sep2018_v1", "/MuonEG/Run2018C-17Sep2018-v1/MINIAOD")

MuonEG = [
    MuonEG_Run2018A_17Sep2018_v1,
    MuonEG_Run2018B_17Sep2018_v1,
    MuonEG_Run2018C_17Sep2018_v1,
]

EGamma_Run2018A_17Sep2018_v2 = Sample("EGamma_Run2018A_17Sep2018_v2", "/EGamma/Run2018A-17Sep2018-v2/MINIAOD")
EGamma_Run2018B_17Sep2018_v1 = Sample("EGamma_Run2018B_17Sep2018_v1", "/EGamma/Run2018B-17Sep2018-v1/MINIAOD")
EGamma_Run2018C_17Sep2018_v1 = Sample("EGamma_Run2018C_17Sep2018_v1", "/EGamma/Run2018C-17Sep2018-v1/MINIAOD")

EGamma = [
    EGamma_Run2018A_17Sep2018_v2,
    EGamma_Run2018B_17Sep2018_v1,
    EGamma_Run2018C_17Sep2018_v1,
]

SingleMuon_Run2018A_17Sep2018_v2 = Sample("SingleMuon_Run2018A_17Sep2018_v2", "/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD")
SingleMuon_Run2018B_17Sep2018_v1 = Sample("SingleMuon_Run2018B_17Sep2018_v1", "/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD")
SingleMuon_Run2018C_17Sep2018_v1 = Sample("SingleMuon_Run2018C_17Sep2018_v1", "/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD")

SingleMuon = [
    SingleMuon_Run2018A_17Sep2018_v2,
    SingleMuon_Run2018B_17Sep2018_v1,
    SingleMuon_Run2018C_17Sep2018_v1,
]

MET_Run2018A_17Sep2018_v1 = Sample("MET_Run2018A_17Sep2018_v1", "/MET/Run2018A-17Sep2018-v1/MINIAOD")
MET_Run2018B_17Sep2018_v1 = Sample("MET_Run2018B_17Sep2018_v1", "/MET/Run2018B-17Sep2018-v1/MINIAOD")
MET_Run2018C_17Sep2018_v1 = Sample("MET_Run2018C_17Sep2018_v1", "/MET/Run2018C-17Sep2018-v1/MINIAOD")

MET = [
    MET_Run2018A_17Sep2018_v1,
    MET_Run2018B_17Sep2018_v1,
    MET_Run2018C_17Sep2018_v1,
]

JetHT_Run2018A_17Sep2018_v1 = Sample("JetHT_Run2018A_17Sep2018_v1", "/JetHT/Run2018A-17Sep2018-v1/MINIAOD")
JetHT_Run2018B_17Sep2018_v1 = Sample("JetHT_Run2018B_17Sep2018_v1", "/JetHT/Run2018B-17Sep2018-v1/MINIAOD")
JetHT_Run2018C_17Sep2018_v1 = Sample("JetHT_Run2018C_17Sep2018_v1", "/JetHT/Run2018C-17Sep2018-v1/MINIAOD")

JetHT = [
    JetHT_Run2018A_17Sep2018_v1,
    JetHT_Run2018B_17Sep2018_v1,
    JetHT_Run2018C_17Sep2018_v1,
]


## sum up
allSamples = DoubleMuon + MuonEG + EGamma + SingleMuon + MET + JetHT

