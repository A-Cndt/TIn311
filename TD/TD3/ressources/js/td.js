function seeCorrection(nb) {
	var hidden_items = document.getElementById("hidden" + nb);
	var btnText = document.getElementById("ex" + nb);
	
	if (hidden_items.style.display === "none") {
		hidden_items.style.display = "inline";
		btnText.innerHTML = "Cacher la correction";
	} else {
		hidden_items.style.display = "none";
		btnText.innerHTML = "Voir la correction";
	}
}
