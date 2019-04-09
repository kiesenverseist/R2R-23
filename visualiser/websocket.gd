extends Node

var client = WebSocketClient.new()
var buffer = StreamPeerBuffer.new()

signal robot_updated
signal node_added

func _ready():
	client.connect_to_url("ws://127.0.0.1:8765")
	client.connect("data_received", self, "data_recieved")
	client.connect("connection_established", self, "connection_established")
	client.connect("connection_error", self, "connection_error")
	
	get_tree().create_timer(0.5).connect("timeout", self, "send_data", [{
		"type" : "join",
		"content" : "visualiser"
	}])
	get_tree().create_timer(1).connect("timeout", self, "send_data", [{
		"type" : "robot updated",
		"content" : ""
	}])
	get_tree().create_timer(2.7).connect("timeout", self, "send_data", [{
		"type" : "robot updated",
		"content" : ""
	}])

#warning-ignore:unused_argument
func _process(delta):
	if client.get_connection_status() == WebSocketClient.CONNECTION_DISCONNECTED:
		return
	client.poll()

func send_data(data : Dictionary):
	var msg = JSON.print(data)
	printt("data send", msg)
	client.get_peer(1).put_packet(msg.to_utf8())

func data_recieved():
	var data = client.get_peer(1).get_packet()
	data = (data as PoolByteArray).get_string_from_ascii()
	print("data recieved: %s" % data)
	data = JSON.parse(data).result
	
	match data["type"]:
		"message":
			printt("message", data["content"])
		"robot update":
			emit_signal("robot_updated")
		"node created":
			emit_signal("node_added")
		_:
			print("unknown data type")

func connection_established(protocol = "none"):
	print("Connection succesfull: %s" % protocol)

func conection_error():
	print("connection error'd")