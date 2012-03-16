// Return the BMI for specified weight and height
function bmi (weight, height) {
	return weight / Math.pow(height,2);
}

// Return the healthy weight range as a tuple
function hwr (height) {
	return [Math.pow(height,2)*18.5, Math.pow(height,2)*24.9]
}

// Return the basal metabolic rate for a specific age group and gender in MJ
// Man = 0
// Woman = 1
function bmr ( age , gender, weight ) {
	if (gender == 0) {
		if (age <= 30) return 0.063*weight + 2.896;
		else return 0.048*weight + 3.653;
	} else {
		if (age <= 30) return 0.062*weight + 2.036;
		else return 0.034*weight + 3.538;
	}
}

// Return the Expected Energy Requirement (EER) 
function eer ( bmr, af) {
	return bmr * af * 1000;
}

// Recommended protein per day (in grams)
function rp (weight, gender) {
	if (gender == 0) {
		return 0.84 * weight;
	} else {
		return 0.64 * weight;
	}
}

// Recommended total fat (in grams)
function rtf (bmr, af) {
	return 0.3*eer(bmr,af)/37;
}

// Recommended saturated fat (in grams)
function rsf (bmr, af) {
	return 0.08*eer(bmr,af)/37;
}

// Recommended carbohydrates (in grams)
function rch (bmr, af) {
	return 0.6*eer(bmr,af)/16;
}

// Recommended Sodium in mg
function rs () {
	return 6000;
}
