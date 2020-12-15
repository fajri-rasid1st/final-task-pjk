const flashData = $(".flash-data");

// alert
if (flashData.data("category") == "success") {
	Swal.fire({
		title: "Success",
		icon: flashData.data("category"),
		text: flashData.data("flash"),
		confirmButtonText: "Kembali",
		background: "#F0F5F9",
	});
} else if (flashData.data("category") == "error") {
	Swal.fire({
		title: "Failed",
		icon: flashData.data("category"),
		text: flashData.data("flash"),
		confirmButtonText: "Kembali",
		background: "#F0F5F9",
	});
} else if (flashData.data("category") == "info") {
	Swal.fire({
		title: "Information",
		icon: flashData.data("category"),
		text: flashData.data("flash"),
		confirmButtonText: "Kembali",
		background: "#F0F5F9",
	});
}