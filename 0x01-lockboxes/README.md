# 0x01. Lockboxes

## Tasks

### 0. Lockboxes
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

	x Prototype: def canUnlockAll(boxes)
	x boxes is a list of lists
	x A key with the same number as a box opens that box
	x You can assume all keys will be positive integers
		x There can be keys that do not have boxes
	x The first box boxes[0] is unlocked
	x Return True if all boxes can be opened, else return False
