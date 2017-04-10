$(document).ready(function(){
	var WEBSOCKET_ROUTE = "/ws";
	if(window.location.protocol=="http:"){
		var ws = new WebSocket("ws://"+window.location.host+WEBSOCKET_ROUTE);
	}
	
	ws.onopen = function(evt){
		$("#ws-status").html("Connected");
	};

	ws.onclose = function(evt){
		$("#ws-status").html("Disconnected");
	};	

	ws.onmessage = function(evt){};

	$("#led_on").click(function(){
		ws.send("on_13");
	});
	
	$("#led_off").click(function(){
		ws.send("off_13");
	});
});
