from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ui.database import Base

class Case(Base):
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Case %r>' % (self.id)

    # General fields
    DOB = Column(DateTime)
    AgeInMonth = Column(Integer)
    Gender = Column(Integer)
    Ethnicity = Column(Integer)
    Race = Column(Integer)

    # History fields
    InjuryMech = Column(Integer)
    Amnesia_verb = Column(Integer)
    LOCSeparate = Column(Integer)
    LocLen = Column(Integer)
    Seiz = Column(Integer)
    SeizOccur = Column(Integer)
    SeizLen = Column(Integer)
    ActNorm = Column(Integer)

    # Symptoms fields
    HA_verb = Column(Integer)
    HASeverity = Column(Integer)
    HAStart = Column(Integer)
    Vomit = Column(Integer)
    VomitNbr = Column(Integer)
    VomitStart = Column(Integer)
    VomitLast = Column(Integer)
    Dizzy = Column(Integer)

    # Mental Status fields
    Intubated = Column(Integer)
    Paralyzed = Column(Integer)
    Sedated = Column(Integer)
    GCSEye = Column(Integer)
    GCSVerbal = Column(Integer)
    GCSMotor = Column(Integer)
    GCSTotal = Column(Integer)
    AMS = Column(Integer)
    AMSAgitated = Column(Integer)
    AMSSleep = Column(Integer)
    AMSSlow = Column(Integer)
    AMSRepeat = Column(Integer)
    AMSOth = Column(Integer)

    # Examination fields
    SFxPalp = Column(Integer)
    SFxPalpDepress = Column(Integer)
    FontBulg = Column(Integer)
    SFxBas = Column(Integer)
    SFxBasHem = Column(Integer)
    SFxBasRhi = Column(Integer)
    SFxBasOto = Column(Integer)
    SFxBasPer = Column(Integer)
    SFxBasRet = Column(Integer)
    Hema = Column(Integer)
    HemaLoc = Column(Integer)
    HemaSize = Column(Integer)
    Clav = Column(Integer)
    ClavFace = Column(Integer)
    ClavNeck = Column(Integer)
    ClavFro = Column(Integer)
    ClavOcc = Column(Integer)
    ClavPar = Column(Integer)
    ClavTem = Column(Integer)
    NeuroD = Column(Integer)
    NeuroDMotor = Column(Integer)
    NeuroDSensory = Column(Integer)
    NeuroDCranial = Column(Integer)
    NeuroDReflex = Column(Integer)
    NeuroDOth = Column(Integer)
    OSI = Column(Integer)
    OSIExtremity = Column(Integer)
    OSICut = Column(Integer)
    OSICspine = Column(Integer)
    OSIFlank = Column(Integer)
    OSIAbdomen = Column(Integer)
    OSIPelvis = Column(Integer)
    OSIOth = Column(Integer)
    Drugs = Column(Integer)

    # Feedback fields
    Prediction = Column(Integer)
    Evaluation = Column(Integer, nullable=True, default=None)
    Feedback = Column(String(500), nullable=True, default=None)
    DateSubmitted = Column(DateTime, nullable = True, default = datetime.utcnow())
    
    @staticmethod
    def fromForm(caseForm):
        case = Case()
        for formField in caseForm.formFields():
            for field in formField:
                if field.short_name != 'csrf_token':
                    if field.type == 'BooleanField':
                        setattr(case, field.short_name, int(field.data))
                    else:
                        setattr(case, field.short_name, field.data)
        return case