// Javascript used in the Case view to hide fields that are not needed due to a 
// "parent" value excluding them

// update any related fields and hide or show them as needed
// this will also reset any "child" field values
function updateRelated(element, related) {
	related.forEach( function(item, idx) {
		if (element.val() > 0 || element.is(":checked")) {
			// remove the bootstrap display-none CSS
			item.removeClass('d-none')
		} else {
			// add the boostrap display-none CSS
			item.addClass('d-none')
			// set the value of all children selects to NA
			item.find('select').each( function(idx, child) {
				child.value = 92
			})
		}
	})
}

// hook the parent elements
$("#History-LOCSeparate").change(function() {
	updateRelated($(this), [$("#History-LocLen-group")])
})

$("#History-Seiz").change(function() {
	updateRelated($(this), [$("#History-SeizOccur-group")])
})

$("#Symptoms-HA_verb").change(function() {
	updateRelated($(this), [
		$("#Symptoms-HASeverity-group"),
		$("#Symptoms-HAStart-group")
	])
})

$("#Symptoms-Vomit").change(function() {
	updateRelated($(this), [
		$("#Symptoms-VomitNbr-group"),
		$("#Symptoms-VomitStart-group"),
		$("#Symptoms-VomitLast-group")
	])
})

$("#MentalStatus-AMS").change(function() {
	updateRelated($(this), [
		$("#MentalStatus-AMSSlow-group"),
		$("#MentalStatus-AMSAgitated-group"),
		$("#MentalStatus-AMSRepeat-group"),
		$("#MentalStatus-AMSSleep-group"),
		$("#MentalStatus-AMSOth-group")
	])
})

$("#Examination-SFxPalp").change(function() {
	updateRelated($(this), [
		$("#Examination-SFxPalpDepress-group"),
	])
})

$("#Examination-SFxBas").change(function() {
	updateRelated($(this), [
		$("#Examination-SFxBasHem-group"),
		$("#Examination-SFxBasRhi-group"),
		$("#Examination-SFxBasOto-group"),
		$("#Examination-SFxBasPer-group"),
		$("#Examination-SFxBasRet-group")
	])
})

$("#Examination-Hema").change(function() {
	updateRelated($(this), [
		$("#Examination-HemaLoc-group"),
		$("#Examination-HemaSize-group"),
	])
})

$("#Examination-Clav").change(function() {
	updateRelated($(this), [
		$("#Examination-ClavFace-group"),
		$("#Examination-ClavNeck-group"),
		$("#Examination-ClavFro-group"),
		$("#Examination-ClavOcc-group"),
		$("#Examination-ClavPar-group"),
		$("#Examination-ClavTem-group")
	])
})

$("#Examination-NeuroD").change(function() {
	updateRelated($(this), [
		$("#Examination-NeuroDMotor-group"),
		$("#Examination-NeuroDSensory-group"),
		$("#Examination-NeuroDCranial-group"),
		$("#Examination-NeuroDReflex-group"),
		$("#Examination-NeuroDOth-group"),
	])
})

$("#Examination-OSI").change(function() {
	updateRelated($(this), [
		$("#Examination-OSIExtremity-group"),
		$("#Examination-OSICut-group"),
		$("#Examination-OSICspine-group"),
		$("#Examination-OSIFlank-group"),
		$("#Examination-OSIAbdomen-group"),
		$("#Examination-OSIPelvis-group"),
		$("#Examination-OSIOth-group"),
	])
})

// update GCS total
function updateGCSTotal() {
	$("#MentalStatus-GCSTotal").val(parseInt($("#MentalStatus-GCSMotor").val()) 
		+ parseInt($("#MentalStatus-GCSVerbal").val())
		+ parseInt($("#MentalStatus-GCSEye").val())
	)
}
$("#MentalStatus-GCSEye").change(function() {
	updateGCSTotal()
})
$("#MentalStatus-GCSVerbal").change(function() {
	updateGCSTotal()
})
$("#MentalStatus-GCSMotor").change(function() {
	updateGCSTotal()
})

// date picker
$("#General-DOB").datetimepicker({
	format: 'D/M/YYYY',
	debug: true
})
$("#General-DOB-group").addClass("date")
$("#General-DOB").addClass("datetimepicker-input")
$("#General-DOB").attr('data-toggle', 'datetimepicker')
$("#General-DOB").attr('data-target', '#General-DOB')
$("#General-DOB").datetimepicker({
	 format: 'D/M/YYYY',
	 debug: true
})

$("#General-DOB").on("change.datetimepicker", e => {
	dob = moment($("#General-DOB").val(), 'D/M/YYYY')
	now = moment()
	$("#General-AgeInMonth").val(now.diff(dob, 'month'))
})

// set the id field as read only
$("#CaseId").attr('readonly', '')

// if the case id has a value, ensure the URL is correct
console.log($("#CaseId").val())
if ($("#CaseId").val()) {
	window.history.pushState("","", $("#CaseId").val())
}