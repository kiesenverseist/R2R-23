extends Node2D

func _ready():
	pass # Replace with function body.

func move():
	position += Vector2(randi()%12-6, randi()%12-6)