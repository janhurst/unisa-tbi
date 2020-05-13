$("#Seiz").change(function() {
			if ($(this).val() == "1") {
				$('#otherFieldDiv').show();
				$('#SeizOccur').attr('required','');
				$('#SeizLen').attr('required','');
				$('#SeizOccur').attr('data-error', 'This field is required.');
				$('#SeizLen').attr('data-error', 'This field is required.');
			} else {
				$('#otherFieldDiv').hide();
				$('#SeizOccur').removeAttr('required');
				$('#SeizOccur').removeAttr('data-error');				
			}
		});
		$("#Seiz").trigger("change");




$("#HA_verb").change(function() {
			if ($(this).val() == "1") {
				$('#otherFieldDivH').show();
				$('#HASeverity').attr('required','');
				$('#HAStart').attr('required','');
				$('#HASeverity').attr('data-error', 'This field is required.');
				$('#HAStart').attr('data-error', 'This field is required.');
			} else {
				$('#otherFieldDivH').hide();
				$('#HASeverity').removeAttr('required');
				$('#HASeverity').removeAttr('data-error');				
			}
		});
		$("#HA_verb").trigger("change");

$("#Vomit").change(function() {
			if ($(this).val() == "1") {
				$('#otherFieldDivV').show();
				$('#VomitNbr').attr('required','');
				$('#VomitStart').attr('required','');
				$('#VomitLast').attr('required', '');
				$('#VomitNbr').attr('data-error', 'This field is required.');
				$('#VomitStart').attr('data-error', 'This field is required.');
				$('#VomitLast').attr('data-error', 'This field is required.');
			} else {
				$('#otherFieldDivV').hide();
				$('#VomitNbr').removeAttr('required');
				$('#VomitNbr').removeAttr('data-error');				
			}
		});
		$("#Vomit").trigger("change");

$("#Hema").change(function() {
			if ($(this).val() == "1") {
				$('#otherFieldDivHema').show();
				$('#HemaLoc').attr('required','');
				$('#HemaSize').attr('required','');
			
				$('#HemaLoc').attr('data-error', 'This field is required.');
				$('#HemaSize').attr('data-error', 'This field is required.');
				
			} else {
				$('#otherFieldDivHema').hide();
				$('#HemaLoc').removeAttr('required');
				$('#HemaLoc').removeAttr('data-error');				
			}
		});
		$("#Hema").trigger("change");

$("#AMS").change(function() {
			if ($(this).val() == "1") {
				$('#otherFieldDivA').show();
				$('#AMSAgitated').attr('required','');
				$('#AMSSleep').attr('required','');
				$('#AMSRepeat').attr('required', '');
				$('#AMSOth').attr('required', '');
				$('#AMSSlow').attr('required', '');
				$('#AMSAgitated').attr('data-error', 'This field is required.');
				$('#AMSSleep').attr('data-error', 'This field is required.');
				$('#AMSRepeat').attr('data-error', 'This field is required.');
				$('#AMSOth').attr('data-error', 'This field is required.');
				$('#AMSSlow').attr('data-error', 'This field is required.');
			} else {
				$('#otherFieldDivA').hide();
				$('#AMSAgitated').removeAttr('required');
				$('#AMSAgitated').removeAttr('data-error');				
			}
		});
		$("#AMS").trigger("change");

$("#SFxBas").change(function() {
			if ($(this).val() == "1") {
				$('#otherFieldDivB').show();
				$('#SFxBasHem').attr('required','');
				$('#SFxBasOto').attr('required','');
				$('#SFxBasPer').attr('required', '');
				$('#SFxBasRet').attr('required', '');
				$('#SFxBasRhi').attr('required', '');
				$('#SFxBasHem').attr('data-error', 'This field is required.');
				$('#SFxBasOto').attr('data-error', 'This field is required.');
				$('#SFxBasPer').attr('data-error', 'This field is required.');
				$('#SFxBasRet').attr('data-error', 'This field is required.');
				$('#SFxBasRhi').attr('data-error', 'This field is required.');
			} else {
				$('#otherFieldDivB').hide();
				$('#SFxBasHem').removeAttr('required');
				$('#SFxBasHem').removeAttr('data-error');				
			}
		});
		$("#SFxBas").trigger("change");

$("#SFxPalp").change(function() {
			if ($(this).val() == "1") {
				$('#otherFieldDivS').show();
				$('#SFxPalpDepress').attr('required','');
				$('#SFxPalpDepress').attr('data-error', 'This field is required.');
				
			} else {
				$('#otherFieldDivS').hide();
				$('#SFxPalpDepress').removeAttr('required');
				$('#SFxPalpDepress').removeAttr('data-error');				
			}
		});
		$("#SFxPalp").trigger("change");
$("#Clav").change(function() {
			if ($(this).val() == "1") {
				$('#otherFieldDivClav').show();
				$('#ClavFace').attr('required','');
				$('#ClavNeck').attr('required','');
				$('#ClavFro').attr('required', '');
				$('#ClavOcc').attr('required', '');
				$('#ClavPar').attr('required', '');
				$('#ClavTem').attr('required', '');
				$('#ClavFace').attr('data-error', 'This field is required.');
				$('#ClavNeck').attr('data-error', 'This field is required.');
				$('#ClavFro').attr('data-error', 'This field is required.');
				$('#ClavOcc').attr('data-error', 'This field is required.');
				$('#ClavPar').attr('data-error', 'This field is required.');
				$('#ClavTem').attr('data-error', 'This field is required.');
			} else {
				$('#otherFieldDivClav').hide();
				$('#ClavFace').removeAttr('required');
				$('#ClavFace').removeAttr('data-error');				
			}
		});
		$("#Clav").trigger("change");

$("#NeuroD").change(function() {
			if ($(this).val() == "1") {
				$('#otherFieldDivNeuroD').show();
				$('#NeuroDMotor').attr('required','');
				$('#NeuroDSensory').attr('required','');
				$('#NeuroDCranial').attr('required', '');
				$('#NeuroDReflex').attr('required', '');
				$('#NeuroDOth').attr('required', '');
				$('#NeuroDMotor').attr('data-error', 'This field is required.');
				$('#NeuroDSensory').attr('data-error', 'This field is required.');
				$('#NeuroDCranial').attr('data-error', 'This field is required.');
				$('#NeuroDReflex').attr('data-error', 'This field is required.');
				$('#NeuroDOth').attr('data-error', 'This field is required.');
			} else {
				$('#otherFieldDivNeuroD').hide();
				$('#NeuroDMotor').removeAttr('required');
				$('#NeuroDMotor').removeAttr('data-error');				
			}
		});
		$("#NeuroD").trigger("change");

$("#OSI").change(function() {
			if ($(this).val() == "1") {
				$('#otherFieldDivOSI').show();
				$('#OSIExtremity').attr('required','');
				$('#OSICut').attr('required','');
				$('#OSICspine').attr('required', '');
				$('#OSIFlank').attr('required', '');
				$('#OSIAbdomen').attr('required', '');
				$('#OSIPelvis').attr('required', '');
				$('#OSIOth').attr('required', '');
				$('#OSIExtremity').attr('data-error', 'This field is required.');
				$('#OSICut').attr('data-error', 'This field is required.');
				$('#OSICspine').attr('data-error', 'This field is required.');
				$('#OSIFlank').attr('data-error', 'This field is required.');
				$('#OSIAbdomen').attr('data-error', 'This field is required.');
				$('#OSIPelvis').attr('data-error', 'This field is required.');
				$('#OSIOth').attr('data-error', 'This field is required.');
			} else {
				$('#otherFieldDivOSI').hide();
				$('#OSIExtremity').removeAttr('required');
				$('#OSIExtremity').removeAttr('data-error');				
			}
		});
		$("#OSI").trigger("change");

