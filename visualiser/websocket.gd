extends Node

var client = WebSocketClient.new()
var buffer = StreamPeerBuffer.new()

func _ready():
	client.connect_to_url("ws://127.0.0.1:8765")
	client.connect("data_received", self, "data_recieved")
	client.connect("connection_established", self, "connection_established")
	client.connect("connection_error", self, "connection_error")
	
	get_tree().create_timer(1).connect("timeout", self, "send_data")

#warning-ignore:unused_argument
func _process(delta):
	if client.get_connection_status() == WebSocketClient.CONNECTION_DISCONNECTED:
		return
	client.poll()

func send_data():
	var dat = {
		"type" : "message",
		"content" : "ibi fui"
	}
	dat = JSON.print(dat)
	print(dat)
	buffer.clear()
	buffer.put_data(dat.to_utf8())
	dat = buffer.get_data_array()
	printt(dat.size(), dat.get_string_from_ascii())
	client.get_peer(1).put_packet(dat)

func data_recieved():
	var data = client.get_peer(1).get_packet()
	data = (data as PoolByteArray).get_string_from_ascii()
	print("data recieved: %s" % data)

func connection_established(protocol = "none"):
	print("Connection succesfull: %s" % protocol)

func conection_error():
	print("connection error'd")