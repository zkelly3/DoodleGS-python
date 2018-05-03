from functools import reduce
import operator
import random
class Thing:
	def __init__(self, name, typ):
		self.name = name
		self.typ = typ
		self.had = False
	def __str__(self):
		return '%s(%s)'%(self.name, self.typ)

things = reduce(operator.add, [list(map(lambda x: Thing(x, "human"), ['baby', 'teenager', 'adult', 'genius', 'student', 'expert'])),
								list(map(lambda x: Thing(x, "action"), ['live', 'play', 'study', 'work', 'eat', 'sleep'])),
								list(map(lambda x: Thing(x, "technology"), ['computer', 'television', 'book', 'nova', 'game', 'Internet', 'puzzle', 'event', 'art'])),
								list(map(lambda x: Thing(x, "adjective"), ['brave', 'fat', 'scary', 'new', 'scifi', 'cute', 'hard', 'famous', 'impossible', 'danger'])),
								list(map(lambda x: Thing(x, "game"), ['snoozleberg', 'steppenwolf', 'arcane', 'cncartoon', 'grow',
																		'Gturtle', 'submachine', 'dismantle', 'escape', 'block',
																		'Gdetective', 'adventure', 'chess', 'find', 'offergame', 'life'])),
								list(map(lambda x: Thing(x, "GS"), ['GS', 'pheion', 'members', 'BT', 'dylan', 'rolfuson', 'people', 'chat', 'article'])),
								list(map(lambda x: Thing(x, "puzzle"), ['turtle', 'logic', 'law','dimension', 'quickask', 'moving', 'creation', 'riddle', 'detective', 'illusion', 'wordart'])),
								list(map(lambda x: Thing(x, "event"), ['treasure', 'Egrow', 'Mevent', 'Eescape'])),
								list(map(lambda x: Thing(x, "bad"), ['kid', 'LQpuzzle', 'minigame', 'advertisement', 'rudeword']))
								])

things = dict(map(lambda x: (x.name, x), things))
things['baby'].had = True
things['live'].had = True
	
print("Your goal is to create the elements in GS.")
print("If you don't know what to type, type \"help\" to know more.")

merge = { tuple(sorted(("baby", "live"))): ("eat", "sleep"),
			tuple(sorted(("baby", "eat"))): ("teenager", ),
			tuple(sorted(("teenager", "live"))): ("play", "study"),
			tuple(sorted(("baby", "study"))): ("genius", ),
			tuple(sorted(("teenager", "study"))): ("student", ),
			tuple(sorted(("teenager", "eat"))): ("adult", ),
			tuple(sorted(("adult", "live"))): ("work", ),
			tuple(sorted(("adult", "eat"))): ("fat", ),
			tuple(sorted(("fat", "eat"))): ("scary", ),
			tuple(sorted(("student", "study"))): ("expert", ),
			tuple(sorted(("teenager", "play"))): ("game", ),
			tuple(sorted(("play", "study"))): ("computer", ),
			tuple(sorted(("computer", "play"))): ("game", ),
			tuple(sorted(("expert", "work"))): ("book", ),
			tuple(sorted(("computer", "book"))): ("nova", ),
			tuple(sorted(("nova", "student"))): ("pheion", "snoozleberg"),
			tuple(sorted(("pheion", "game"))): ("GS", ),
			tuple(sorted(("adult", "sleep"))): ("brave", ),
			tuple(sorted(("pheion", "GS"))): ("members", ),
			tuple(sorted(("genius", "GS"))): ("BT", ),
			tuple(sorted(("computer", "expert"))): ("Internet", ),
			tuple(sorted(("pheion", "work"))): ("new", ),
			tuple(sorted(("new", "GS"))): ("puzzle", ),
			tuple(sorted(("puzzle", "GS"))): ("turtle", ),
			tuple(sorted(("brave", "game"))): ("steppenwolf", ),
			tuple(sorted(("scary", "game"))): ("arcane", ),
			tuple(sorted(("pheion", "puzzle"))): ("logic", ),
			tuple(sorted(("logic", "new"))): ("law", ),
			tuple(sorted(("members", "game"))): ("event", ),
			tuple(sorted(("members", "computer"))): ("dylan", ),
			tuple(sorted(("expert", "play"))): ("art", ),
			tuple(sorted(("members", "art"))): ("rolfuson", ),
			tuple(sorted(("new", "game"))): ("offergame", ),
			tuple(sorted(("adult", "play"))): ("television", ),
			tuple(sorted(("television", "game"))): ("cncartoon", ),
			tuple(sorted(("television", "new"))): ("scifi", ),
			tuple(sorted(("scifi", "game"))): ("submachine", ),
			tuple(sorted(("baby", "play"))): ("cute", ),
			tuple(sorted(("cute", "game"))): ("grow", ),
			tuple(sorted(("game", "turtle"))): ("Gturtle", ),
			tuple(sorted(("Internet", "GS"))): ("famous", ),
			tuple(sorted(("famous", "GS"))): ("people", ),
			tuple(sorted(("people", "GS"))): ("PROB", ("chat", ), ("chat", ), ("chat", ), ("chat", ), ("kid", )),
			tuple(sorted(("steppenwolf", "game"))): ("life", ),
			tuple(sorted(("life", "game"))): ("adventure", ),
			tuple(sorted(("puzzle", "game"))): ("chess", ),
			tuple(sorted(("rolfuson", "game"))): ("find", ),
			tuple(sorted(("scary", "adult"))): ("danger", ),
			tuple(sorted(("danger", "game"))): ("dismantle", ),
			tuple(sorted(("danger", "logic"))): ("detective", ),
			tuple(sorted(("detective", "game"))): ("Gdetective", ),
			tuple(sorted(("danger", "puzzle"))): ("escape", ),
			tuple(sorted(("rolfuson", "puzzle"))): ("dimension", ),
			tuple(sorted(("live", "puzzle"))): ("quickask", ),
			tuple(sorted(("baby", "puzzle"))): ("creation", ),
			tuple(sorted(("chat", "puzzle"))): ("riddle", ),
			tuple(sorted(("rolfuson" ,"event"))): ("hard", ),
			tuple(sorted(("creation", "puzzle"))): ("moving", ),
			tuple(sorted(("creation", "riddle"))): ("wordart", ),
			tuple(sorted(("hard", "event"))): ("treasure", ),
			tuple(sorted(("rolfuson" ,"event"))): ("Eescape", ),
			tuple(sorted(("event", "members"))): ("Mevent", ),
			tuple(sorted(("kid", "puzzle"))): ("LQpuzzle", ),
			tuple(sorted(("kid", "game"))): ("minigame", ),
			tuple(sorted(("members", "treasure"))): ("article", ),
                        tuple(sorted(("grow", "event"))): ("Egrow", ),
                        tuple(sorted(("creation", "dimension"))): ("illusion", ),
                        tuple(sorted(("pheion", "sleep"))): ("impossible", ),
                        tuple(sorted(("pheion", "play"))): ("impossible", ),
			tuple(sorted(("kid", "article"))): ("PROB", ("advertisement", ), ("advertisement", ), ("advertisement", ), ("advertisement", ), ("rudeword", )),
			tuple(sorted(("chess", "game"))): ("block", )
}
type_map = dict(map(lambda x: (x, []), ("human", "action", "technology", "adjective", "game", "GS", "puzzle", "event", "bad")))
for i in things.values():
    type_map[i.typ].append(i)
def combine(ele1, ele2):
	ok = lambda x: x in things and things[x].had
	if not ok(ele1) or not ok(ele2):
		print("Invalid combination")
		return
	else:
		res = ()
		if tuple(sorted((ele1, ele2)))in merge.keys():
			res = merge[tuple(sorted((ele1, ele2)))]
			if res[0] == "PROB":
				res = random.choice(res[1:])
		else:
			print("Invalid combination")
		for i in res:
			if things[i].had == True:
				print("Ah ha! You created " + things[i].name + " again!")
			else:
				things[i].had = True
				print("You created a new element " + things[i].name + "!")

while True:
	strs = input().split()
	if len(strs) > 3 or len(strs) < 1:
		print("If you don't know what to type, type \"help\" to know more.")
	elif len(strs) == 1:
		if strs[0] == "help":
			print("check - show types you've created")
			print("check [typename] - show elements in this type that you've created")
			print("combine [element1] [element2] - combine two elements")
			print("help - show this help")
			print("progress - show how good you've done so far")
			print("progress [typename] - show the number of elements you've created and the total number in this type")
		elif strs[0] == "check":
			for typ in set(map(lambda x: x.typ, filter(lambda x: x.had, things.values()))):
				print(typ)
		elif strs[0] == "progress":
			types = len(set(map(lambda x: x.typ, filter(lambda x: x.had, things.values()))))
			elements = len(list(filter(lambda x: x.had, things.values())))
			print("types: " + str(types) + "/" + str(len(type_map)))
			print("elements: " + str(elements) + "/" + str(len(things)))
		else:
			print("Invalid input")
			print("If you don't know what to type, type \"help\" to know more.")
	elif len(strs) == 2:
		if strs[0] == "check":
			if strs[1] not in set(map(lambda x: x.typ, filter(lambda x: x.had, things.values()))):
				print("Invalid check")
			else:
				for i in type_map[strs[1]]:
					if i.had == True:
						print(i.name)
		elif strs[0] == "progress":
			if strs[1] not in set(map(lambda x: x.typ, filter(lambda x: x.had, things.values()))):
				print("Invalid progress check")
			else:
				count = 0
				for i in type_map[strs[1]]:
					if i.had == True:
						count = count + 1
				print(strs[1] + ": " + str(count) + "/" + str(len(type_map[strs[1]])))
		else:
			print("Invalid input")
			print("If you don't know what to type, type \"help\" to know more.")
	else:
		if strs[0] == "combine":
			combine(strs[1], strs[2])
		else:
			print("Invalid input")
			print("If you don't know what to type, type \"help\" to know more.")
