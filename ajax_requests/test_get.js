$.ajax({
	url: '/index.php',         /* Куда пойдет запрос */
	method: 'get',             /* Метод передачи (post или get) */
	dataType: 'html',          /* Тип данных в ответе (xml, json, script, html). */
	data: {text: 'Текст'},     /* Параметры передаваемые в запросе. */
	success: function(data){   /* функция которая будет выполнена после успешного запроса.  */
		alert(data);            /* В переменной data содержится ответ от index.php. */
	}
});

$.ajax({
	url: '/json.php',
	method: 'get',
	dataType: 'json',
	success: function(data){
		alert(data.text);    /* выведет "Текст" */
		alert(data.error);   /* выведет "Ошибка" */
	}
});

//Чтобы включить синхронный режим нужно добавить параметр async: false.
var text = '';
 
$.ajax({
	url: '/index.php',
	method: 'get',
	dataType: 'html',
	async: false,
	success: function(data){
		text = data;
	}
});
 
alert(text); /* В переменной будет результат из index.php. */
let oid = '91d8e48e-f1e4-164d-8d1d-4ed4adda50ef'
$.ajax({
	url: '/rest/data/entity/' + oid,         /* Куда пойдет запрос */
	method: 'get',             /* Метод передачи (post или get) */
	dataType: 'json',          /* Тип данных в ответе (xml, json, script, html). */
	success: function(data){   /* функция которая будет выполнена после успешного запроса.  */
		console.log(data);
	}
});