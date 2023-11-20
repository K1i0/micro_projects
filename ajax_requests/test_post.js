$.ajax({
	url: '/index.php',
	method: 'post',
	dataType: 'html',
	data: {text: 'Текст'},
	success: function(data){
		alert(data);
	}
});