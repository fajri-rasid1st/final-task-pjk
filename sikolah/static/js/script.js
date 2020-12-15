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

// confirm email send
// $(".btn-email").on("click", function (e) {
// 	e.preventDefault();

// 	Swal.fire({
// 		title: "Konfirmasi Pengiriman",
// 		text: "Anda yakin akan mengirimkan akun untuk pengguna ini?",
// 		icon: "question",
// 		showCancelButton: true,
// 		confirmButtonColor: "#007BFF",
// 		confirmButtonText: "Ya!",
// 		cancelButtonColor: "#DC3545",
// 		cancelButtonText: "Tidak!",
// 		background: "#F0F5F9",
// 	}).then((result) => {
// 		if (result.isConfirmed) {
// 			document.location.href = "/admin/email";
// 		}
// 	});
// });
