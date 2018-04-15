// What would be an appropriate (descriptive) comment here (if any)?

function update(update) {
	var fields = ["airline", "counter", "flight", "departure", "destination",
				  "seat-class", "boarding", "gate", "message"];

	for (var n = 0; n < fields.length; n++) {
		var fieldName = fields[n];

		if (update.hasOwnProperty(fieldName)) {
   		div = document.getElementById(fieldName);
   		div.innerText = update[fieldName];
		}
	}
}


window.onload = function() {
	update({
		"airline": "airline: DOGE AIR",
		"counter": "counter #: 13",
		"flight": "flight #: PUP1113",
		// "2018-06-13T13:26:00-07:00"		* import datetime?
		"departure": "departs at: 13:59",
		"destination": "destination: New Orleans",
		"seat-class": "seat class: BUSINESS",
		"boarding": "boarding starts: 13:13",
		"gate": "gate #: B66",
		"message": "some message here",		// maybe/maybe not
	});
}
