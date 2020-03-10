window.onload = function(){
    var hw = document.getElementById('AddFile');
    hw.addEventListener('click', function(){
        alert("aa");
        var dialog = document.getElementById('dialog_Window');
		dialog.style.display = "block";
    });
	
	var cancel = document.getElementById("upload_cancel_button");
	cancel.addEventListener("click", function(){
		var dialog = document.getElementById('dialog_Window');
		dialog.style.display = "None";
	});
}