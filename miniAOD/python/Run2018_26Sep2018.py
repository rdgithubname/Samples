from Samples.Tools.Sample import Sample

## DoubleMuon
DoubleMuon_Run2018B_26Sep2018               = Sample("DoubleMuon_Run2018B_26Sep2018",               "/DoubleMuon/Run2018B-26Sep2018-v1/MINIAOD")
DoubleMuon_Run2018B_26Sep2018_HEM           = Sample("DoubleMuon_Run2018B_26Sep2018_HEM",           "/DoubleMuon/Run2018B-26Sep2018_HEM-v1/MINIAOD")
DoubleMuon_Run2018B_26Sep2018_HEMmitigation = Sample("DoubleMuon_Run2018B_26Sep2018_HEMmitigation", "/DoubleMuon/Run2018B-26Sep2018_HEMmitigation-v1/MINIAOD")

DoubleMuon = [
    DoubleMuon_Run2018B_26Sep2018,
    DoubleMuon_Run2018B_26Sep2018_HEM,
    DoubleMuon_Run2018B_26Sep2018_HEMmitigation,
]

# MuonEG
MuonEG_Run2018B_26Sep2018               = Sample("MuonEG_Run2018B_26Sep2018",               "/MuonEG/Run2018B-26Sep2018-v1/MINIAOD")
MuonEG_Run2018B_26Sep2018_HEM           = Sample("MuonEG_Run2018B_26Sep2018_HEM",           "/MuonEG/Run2018B-26Sep2018_HEM-v1/MINIAOD")
MuonEG_Run2018B_26Sep2018_HEMmitigation = Sample("MuonEG_Run2018B_26Sep2018_HEMmitigation", "/MuonEG/Run2018B-26Sep2018_HEMmitigation-v1/MINIAOD")

MuonEG = [
    MuonEG_Run2018B_26Sep2018,
    MuonEG_Run2018B_26Sep2018_HEM,
    MuonEG_Run2018B_26Sep2018_HEMmitigation,
]

# EGamma
EGamma_Run2018B_26Sep2018               = Sample("EGamma_Run2018B_26Sep2018",               "/EGamma/Run2018B-26Sep2018-v1/MINIAOD")
EGamma_Run2018B_26Sep2018_HEM           = Sample("EGamma_Run2018B_26Sep2018_HEM",           "/EGamma/Run2018B-26Sep2018_HEM-v1/MINIAOD")
EGamma_Run2018B_26Sep2018_HEMmitigation = Sample("EGamma_Run2018B_26Sep2018_HEMmitigation", "/EGamma/Run2018B-26Sep2018_HEMmitigation-v1/MINIAOD")

EGamma = [ 
    EGamma_Run2018B_26Sep2018,
    EGamma_Run2018B_26Sep2018_HEM,
    EGamma_Run2018B_26Sep2018_HEMmitigation,
]


## sum up
allSamples = DoubleMuon + MuonEG + EGamma

