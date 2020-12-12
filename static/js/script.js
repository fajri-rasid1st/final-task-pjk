const flashData = $(".flash-data");

// alert
if (flashData.data("category") == "success") {
	Swal.fire({
		title: "Success",
		icon: flashData.data("category"),
		text: flashData.data("flash"),
		confirmButtonText: "Ok, I got it!",
	});
} else if (flashData.data("category") == "error") {
	Swal.fire({
		title: "Failed",
		icon: flashData.data("category"),
		text: flashData.data("flash"),
		confirmButtonText: "Ok, I got it!",
	});
} else if (flashData.data("category") == "info") {
	Swal.fire({
		title: "Information",
		icon: flashData.data("category"),
		text: flashData.data("flash"),
		confirmButtonText: "Ok, I got it!",
	});
}

// confirm delete
$("#btn-delete").on("click", function (e) {
	e.preventDefault();

	const href = $(this).attr("href");

	Swal.fire({
		title: "Delete Confirm",
		text: "Are you sure you want to delete this post?",
		icon: "question",
		showCancelButton: true,
		confirmButtonColor: "#007BFF",
		confirmButtonText: "Yes, delete it!",
		cancelButtonColor: "#DC3545",
		cancelButtonText: "No, go back!",
	}).then((result) => {
		if (result.isConfirmed) {
			document.location.href = href;
		}
	});
});
