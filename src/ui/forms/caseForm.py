from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import FormField, BooleanField, IntegerField, StringField, SelectField, DateField, DateTimeField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, NumberRange, Optional
from ui.models.case import Case
from ui.database import db_session
import pytz
from tzlocal import get_localzone

class HideFieldByParentValue(object):
    field_flags = ('hide', )

    def __init__(self, parent):
        self.parent = parent

    def __call__(self, form, field):
        # turn off the hide flag if the parent is non-zero
        if form.data[self.parent] > 0:
            field.flags.hide = False
        # fail validation if the parent is non-zero and this field is 92
        if form.data[self.parent] > 0 and field.data == 92:
            raise ValidationError()

class GeneralInformationForm(FlaskForm):
    DOB = DateField('Date of Birth', format='%d/%m/%Y')

    AgeInMonth = IntegerField('Age (months)', render_kw={'readonly': True}, default=0)

    Gender = SelectField('Gender', coerce=int,
        choices=[
            (-1, 'Select'),
            (1, 'Male'),
            (2, 'Female')
        ],
        validators=[NumberRange(min=1)])

    Ethnicity = SelectField('Ethnicity', coerce=int,
        choices=[
            (-1, 'Select'),
            (1, 'Hispanic'),
            (2, 'Non-Hispanic')
        ],
        default=None,
        validators=[NumberRange(min=1)])

    Race = SelectField('Race', coerce=int,
        choices=[
            (-1, 'Select'),
            (1, 'White'),
            (2, 'Black'),
            (3, 'Asian'), 
            (4, 'American Indian/Alaskan Native'),
            (5, 'Pacific Islander'),
            (90, 'Other')
        ],
        validators=[NumberRange(min=1)])

class HistoryForm(FlaskForm):
    InjuryMech = SelectField('Injury Mechanism', coerce=int,
        choices=[(-1, 'Select'), 
            (1, 'Occupant in motor vehicle collision(MVC)'),
            (2, 'Pedestrian struck by moving vehicle'),
            (3, 'Bike rider struck by automobile'),
            (4, 'Bike collision or fall from bike while riding'),
            (5, 'Other wheeled transport crash'),
            (6, 'Fall to ground from standing/walking/running'),
            (7, 'Walked or ran into stationary object'),
            (8, 'Fall from an elevation'),
            (9, 'Fall down stairs'),
            (10, 'Sports'),
            (11, 'Assault'),
            (12, 'Object Struck head - accidental'),
            (90, 'Other Mechanism'),            
        ],
        validators=[NumberRange(min=1)])

    Amnesia_verb = BooleanField('Does the patient have amnesia?')    

    LOCSeparate = SelectField('Loss of conciousness?', coerce=int,
        choices=[
            (0, 'No'),
            (1, 'Yes'),
            (2, 'Suspected')
        ])

    LocLen = SelectField('Duration of loss of conciousness', coerce=int, render_kw={'class': 'd-none'},
        choices=[
            (92, 'NA'),
            (1, '< 5sec'),
            (2, '5sec - 1min'),
            (3, '1-5min'),
            (4, '>5min')
        ],
        validators=[HideFieldByParentValue('LOCSeparate')])    
    
    Seiz = BooleanField('Post-traumatic seizure?')

    SeizOccur = SelectField('Time of seizure', coerce=int,
        choices=[
            (92, 'N/A'),
            (1, 'Immediately'),
            (2, 'Within 30 mins'),
            (3, 'more than 30 mins')
        ],
        validators=[HideFieldByParentValue('Seiz')])

    SeizLen = SelectField('Seizure duration', coerce=int,
        choices=[
            (92, 'N/A'),
            (1, 'Less than 1 min'),
            (2, '1 to 5 mins'),
            (3, '5 to 15 mins'),
            (4, '> 15 mins')
        ],
        validators=[HideFieldByParentValue('Seiz')])   
    
    ActNorm = BooleanField('Is child acting normally?', default=True)

class SymptomsForm(FlaskForm):
    
    HA_verb = SelectField('Headache?', coerce=int,
        choices=[
            (0, 'No'),
            (1, 'Yes'),
            (91, 'Pre-verbal / Non-verbal')
        ],
        validators=[])

    HASeverity = SelectField('Severity of headache', coerce=int,
        choices=[
            (92, 'N/A'),
            (1, 'Mild'),
            (2, 'Moderate'),
            (3, 'Severe / Intense')
        ],
        validators=[HideFieldByParentValue('HA_verb')])

    HAStart = SelectField('When did headache start?', coerce=int,
        choices=[
            (92, 'N/A'),
            (1, 'Before head injury'),
            (2, 'Within 1 hour of injury'),
            (3, '1-4 hours after injury'),
            (4, '> 4 hours after injury')
        ],
        validators=[HideFieldByParentValue('HA_verb')])

    Vomit = BooleanField('Vomiting?')    

    VomitNbr = SelectField('How many vomiting episodes?', coerce=int,
        choices=[
            (92, 'N/A'),
            (1, 'Once'),
            (2, 'Twice'),
            (3, 'More than twice')
        ],
        validators=[HideFieldByParentValue('Vomit')])

    VomitStart = SelectField('When did vomiting start?', coerce=int,
        choices=[
            (92, 'N/A'),
            (1, 'Before head injury'),
            (2, 'Within 1 hour of injury'),
            (3, '1-4 hours after event'),
            (4, '> 4 hours after event')
        ],
        validators=[HideFieldByParentValue('Vomit')])

    VomitLast = SelectField('Last episode of vomiting?', coerce=int,
        choices=[
            (92, 'N/A'),
            (1, '< 1 hour before ED evaluation'),
            (2, '1-4 hours before ED evaluation'),
            (3, '> 4 hours before ED evaluation')
        ],
        validators=[HideFieldByParentValue('Vomit')])

    Dizzy = BooleanField('Dizziness?')

class MentalStatusForm(FlaskForm):
    
    Intubated = BooleanField('Patient was intubated?')
    Paralyzed = BooleanField('Patient pharmacologically paralyzed?')
    Sedated = BooleanField('Patient sedated?')

    # GCS    
    GCSEye = SelectField('GCS Eye', coerce=int,
        choices=[
            (4, '4 - Spontaneous'),
            (3, '3 - Verbal'),
            (2, '2 - Pain'),
            (1, '1 - None')
        ])

    GCSVerbal = SelectField('GCS Verbal', coerce=int,
        choices=[
            (5, '5 - Oriented'),
            (4, '4 - Confused'),
            (3, '3 - Inappropriate words'),
            (2, '2 - Incomprehensible sounds'),
            (1, '1 - None'),
        ])

    GCSMotor = SelectField('GCS Motor', coerce=int,
        choices=[
            (6, '6 - Follow commands'),
            (5, '5 - Localizes pain'),
            (4, '4 - Withdraws to pain'),
            (3, '3 - Abnormal flexure posturing'),
            (2, '2 - Abnormal extension posturing'),
            (1, '1 - None')
        ])

    GCSTotal = IntegerField('GCS Total', default=15, render_kw={'readonly': True})
    
    AMS = BooleanField('Any signs of altered mental state?')
    AMSSlow = BooleanField('Slow to respond?', validators=[HideFieldByParentValue('AMS')])
    AMSAgitated = BooleanField('Agitated?', validators=[HideFieldByParentValue('AMS')])
    AMSRepeat = BooleanField('Repetitive questions in ED?', validators=[HideFieldByParentValue('AMS')])
    AMSSleep = BooleanField('Sleepy?', validators=[HideFieldByParentValue('AMS')])
    AMSOth = BooleanField('Other?', validators=[HideFieldByParentValue('AMS')])

class ExaminationForm(FlaskForm):
    # Palpable Skull Fracture
    SFxPalp = SelectField('Palpable skull fracture', coerce=int,
        choices=[
            (0, 'No'),
            (1, 'Yes'),
            (2, 'Unclear Exam')
        ])

    SFxPalpDepress = BooleanField('Is the fracture depressed?', validators=[HideFieldByParentValue('SFxPalp')])

    FontBulg = BooleanField('Anterior fontanelle bulging?')

    SFxBas = BooleanField('Signs of basilar skull fracture?')
    SFxBasHem = BooleanField('Hemotympanum?', validators=[HideFieldByParentValue('SFxBas')])
    SFxBasRhi = BooleanField('CSF rhinorrhea?', validators=[HideFieldByParentValue('SFxBas')])
    SFxBasOto = BooleanField('CSF otorrhea?', validators=[HideFieldByParentValue('SFxBas')])
    SFxBasPer = BooleanField('Periorbital ecchymoses (Racoon eyes)?', validators=[HideFieldByParentValue('SFxBas')])
    SFxBasRet = BooleanField('Retroauricular ecchymoses (Battle\'s sign)?', validators=[HideFieldByParentValue('SFxBas')])

    Hema = BooleanField('Raised scalp hematoma(s) or swelling(s)?')
    HemaLoc = SelectField('Hematoma location', coerce=int,
        choices=[
            (92, 'N/A'),
            (1, 'Frontal'),
            (2, 'Occipital'),
            (3, 'Parietal/Temporal')
        ],
        validators=[HideFieldByParentValue('Hema')])
    HemaSize = SelectField('Hematoma size', coerce=int,
        choices=[
            (92, 'N/A'),
            (1, 'Small (< 1cm, barely palpable)'),
            (2, 'Medium (1-3cm)'),
            (3, 'Large (>3cm)')
        ],
        validators=[HideFieldByParentValue('Hema')])

    # Trauma above Clavicles
    Clav = BooleanField('Trauma above the clavicles?')
    ClavFace = BooleanField('Trauma to face?', validators=[HideFieldByParentValue('Clav')])
    ClavNeck = BooleanField('Trauma to neck?', validators=[HideFieldByParentValue('Clav')])
    ClavFro = BooleanField('Trauma to scalp-frontal?', validators=[HideFieldByParentValue('Clav')])
    ClavOcc = BooleanField('Trauma to scalp-occipital?', validators=[HideFieldByParentValue('Clav')])
    ClavPar = BooleanField('Trauma to scalp-parietal?', validators=[HideFieldByParentValue('Clav')])
    ClavTem = BooleanField('Trauma to scalp-temporal?', validators=[HideFieldByParentValue('Clav')])
    
    # Neurological deficit
    NeuroD = BooleanField('Neurological deficit?')
    NeuroDMotor = BooleanField('Motor deficit?', validators=[HideFieldByParentValue('NeuroD')])
    NeuroDSensory = BooleanField('Sensory deficit?', validators=[HideFieldByParentValue('NeuroD')])
    NeuroDCranial = BooleanField('Cranial nerve deficit?', validators=[HideFieldByParentValue('NeuroD')])
    NeuroDReflex = BooleanField('Reflexes deficit?', validators=[HideFieldByParentValue('NeuroD')])
    NeuroDOth = BooleanField('Other deficits?', validators=[HideFieldByParentValue('NeuroD')])

    # Other substantial injury
    OSI = BooleanField('Other substantial injuries?')
    OSIExtremity = BooleanField('Injury to Extremity?', validators=[HideFieldByParentValue('OSI')])
    OSICut = BooleanField('Lacerations?', validators=[HideFieldByParentValue('OSI')])
    OSICspine = BooleanField('Injury to C-spine?', validators=[HideFieldByParentValue('OSI')])
    OSIFlank = BooleanField('Injury to Chest/back/flank?', validators=[HideFieldByParentValue('OSI')])
    OSIAbdomen = BooleanField('Injury to Intra-abdominal?', validators=[HideFieldByParentValue('OSI')])
    OSIPelvis = BooleanField('Injury to Pelvis?', validators=[HideFieldByParentValue('OSI')])
    OSIOth = BooleanField('Other injury?', validators=[HideFieldByParentValue('OSI')])

    Drugs = BooleanField('Clinical suspicion for alcohol or drug intoxication?')

class EvaluationForm(FlaskForm):
    Prediction = IntegerField('Prediction', validators=[Optional()])
    Evaluation = SelectField('Evaluation', coerce=int,
        choices=[
            (-1, ''),
            (0, 'TBI Not Found'),
            (1, 'TBI Found')
        ], validators=[Optional()])
    DateSubmitted = DateTimeField('Date', format='%Y-%m-%d %H:%M', validators=[Optional()])
    Feedback = TextAreaField('Feedback', validators=[Optional()])
    
class CaseForm(FlaskForm):

    # some id form fields - not sure if we really need these    
    CaseId = StringField('Case Id')

    General = FormField(GeneralInformationForm, description='General Information')
    History = FormField(HistoryForm, description='History')
    Symptoms = FormField(SymptomsForm, description='Symptoms')
    MentalStatus = FormField(MentalStatusForm, description='Mental Status')
    Examination = FormField(ExaminationForm, description='Examination')

    Evaluation = FormField(EvaluationForm, description='Post Outcome Evaluation and Assessment')

    def createInDatabase(self):
        """ Create a new data from form data  """
        newCase = Case.fromForm(self)
        db_session.add(newCase)
        db_session.commit()

        # update the case id with the autoincrement'ed id from the database
        self.CaseId.data = newCase.id

    def updateInDatabase(self):
        """ Update all values in the database from the form data """
        case = Case.query.filter(Case.id == self.CaseId.data).first()

        for formField in self.formFields():
            for field in formField:
                if field.short_name != 'csrf_token':
                    if field.type == 'BooleanField':
                        setattr(case, field.short_name, int(field.data))
                    else:
                        setattr(case, field.short_name, field.data)

        # force the date
        case.DateSubmitted = datetime.now()
        db_session.commit()

    def readFromDatabase(self, id):
        """ Read all of the form values from the database """
        
        # retrieve the form from the database
        case = Case.query.filter(Case.id == id).first()

        # update stuff :)
        self.CaseId.data = case.id
        
        # fill the data in all the FormFields from the Case object that the database query returned
        for formField in self.formFields():
            for field in formField:
                if field.short_name != 'csrf_token':
                    db_data = getattr(case, field.short_name)
                    if db_data is not None:
                        field.data = db_data

    def formFields(self):
        """ collect all the fields that are of type FormField """
        return [field for field in self if isinstance(field, FormField)]
