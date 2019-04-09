extends Node2D

func _ready():
	$Websocket.connect("robot_updated", self, "robot_updated")

func robot_updated():
	$Robot.move()