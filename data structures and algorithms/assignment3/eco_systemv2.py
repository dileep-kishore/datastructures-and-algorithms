# Building an ecosystem
import random


class Animal:
	# ._name vs. .name
	def __init__(self, kind, gender, strength):
		self.name = kind
		self.sex = gender
		self.power = strength

	@staticmethod
	def create(kind):
		"""Create a random animal
		:param kind: Species
		"""
		if random.randint(0, 1):
			gender = 'male'
		else:
			gender = 'female'
		strength = random.random()
		return Animal(kind, gender, strength)

	def __add__(self, other):
		if type(self) != type(other):
			raise TypeError
		if self.name == other.name:
			if self.sex == other.sex:
				if self.power > other.power:
					return self
				else:
					return other
			else:
				kid = Animal(0, 0, 0)
				kid.create(self.name)
				return self, other, kid
		else:
			if self.name == 'bear':
				return self
			else:
				return other

	def disp(self):
		"""Displays the attributes of the animal"""
		return self.name, self.sex, self.power


def eco(river_size, time):
	"""Ecosystem simulation
    :rtype : ecosystem list
    :param river_size: size of the ecosystem
    :param time: number of time steps
    """
	random.seed(3)  # Random seed
	actual = int(round(random.gauss(river_size // 2, river_size // 10)))
	print('total population', actual)
	fish_num = random.randint(0, actual)
	print('fish', fish_num)
	bear_num = actual - fish_num
	print('bear', bear_num)
	bear = [Animal(0, 0, 0)] * bear_num
	for i in range(bear_num):
		bear[i] = bear[i].create('bear')
	fish = [Animal(0, 0, 0)] * fish_num
	for i in range(fish_num):
		fish[i] = fish[i].create('fish')

	river = bear + fish + [None] * (river_size - actual)
	random.shuffle(river)
	eco_list = [[]] * (time + 1)
	eco_list[0] = [x for x in river]
	k = []
	for m in river:
		if m is not None:
			k += [m.disp()]
		else:
			k += [None]
	print(k)
	for step in range(time):
		temp_river = [None] * river_size
	# positions of the animals in the river
	pos_list1 = [i for i in range(len(river)) if river[i] is not None]
	print('old pos', pos_list1)
	# New changed positions
	pos_list2 = [elem + random.randint(-1, 1) for elem in pos_list1]
	print('new pos', pos_list2)
	# Animals migrating outside the list
	if pos_list2[0] < 0:
		pos_list2 = pos_list2[1:]
		pos_list1 = pos_list1[1:]
	if pos_list2[-1] > len(river) - 1:
		pos_list2 = pos_list2[:-1]
		pos_list1 = pos_list1[:-1]
	kid_list = []
	for i in range(len(river)):
		ind = [iter for iter, val in enumerate(pos_list2) if val == i]
		# If there is no collision
		if len(ind) == 1:
			temp_river[i] = river[pos_list1[ind[0]]]
		# If two animals collide
		elif len(ind) == 2:
			new = river[pos_list1[ind[0]]] + river[pos_list1[ind[1]]]
			if type(new).__name__ == 'tuple':
				# New animal created and added to list
				kid_list += [new[2]]
				temp_river[pos_list1[ind[0]]] = river[pos_list1[ind[0]]]
				temp_river[pos_list1[ind[1]]] = river[pos_list1[ind[1]]]
			else:
				temp_river[i] = new
		# if three animals collide
		elif len(ind) == 3:
			act = [river[pos_list1[ind[z]]].disp() for z in range(3)]
			if act[0][0] == act[1][0] == act[2][0]:
				# If all animals are of the same species
				if act[0][1] == act[1][1] == act[2][1]:
					# If all the animals are of the same gender
					tem = river[pos_list1[ind[0]]] + river[pos_list1[ind[1]]] + \
					      river[pos_list1[ind[2]]]
					temp_river[i] = tem
				else:
					# Checking which two animals are of the same gender
					if act[0][1] == act[1][1]:
						same = [river[pos_list1[ind[0]]],
						        river[pos_list1[ind[1]]]]
						if same[0].disp()[2] > same[1].disp()[2]:
							temp_river[pos_list1[ind[0]]] = same[0]
						else:
							temp_river[pos_list1[ind[1]]] = same[1]
						nsame = river[pos_list1[ind[2]]]
						temp_river[pos_list1[ind[2]]] = nsame
					elif act[1][1] == act[2][1]:
						same = [river[pos_list1[ind[1]]],
						        river[pos_list1[ind[2]]]]
						if same[0].disp()[2] > same[1].disp()[2]:
							temp_river[pos_list1[ind[1]]] = same[0]
						else:
							temp_river[pos_list1[ind[2]]] = same[1]
						nsame = river[pos_list1[ind[0]]]
						temp_river[pos_list1[ind[0]]] = nsame
					else:
						same = [river[pos_list1[ind[0]]],
						        river[pos_list1[ind[2]]]]
						if same[0].disp()[2] > same[1].disp()[2]:
							temp_river[pos_list1[ind[0]]] = same[0]
						else:
							temp_river[pos_list1[ind[2]]] = same[1]
						nsame = river[pos_list1[ind[1]]]
						temp_river[pos_list1[ind[1]]] = nsame
					new = (same[0] + same[1]) + nsame
					# A new animal is inevitably formed
					kid_list += [new[2]]
			else:
				# Checking which two animals are of the same species
				if act[0][0] == act[1][0]:
					same = [river[pos_list1[ind[0]]], river[pos_list1[ind[1]]]]
					s_ind = [ind[0], ind[1]]
					nsame = river[pos_list1[ind[2]]]
				elif act[1][0] == act[2][0]:
					same = [river[pos_list1[ind[1]]], river[pos_list1[ind[2]]]]
					s_ind = [ind[1], ind[2]]
					nsame = river[pos_list1[ind[0]]]
				else:
					same = [river[pos_list1[ind[0]]], river[pos_list1[ind[2]]]]
					s_ind = [ind[0], ind[2]]
					nsame = river[pos_list1[ind[1]]]
				new = (nsame + same[0]) + same[1]
				if type(new).__name__ == 'tuple':
					kid_list += [new[2]]
					temp_river[pos_list1[s_ind[0]]] = same[0]
					temp_river[pos_list1[s_ind[1]]] = same[1]
				else:
					if same[0].disp()[0] == 'fish':
						temp_river[i] = new
					elif same[0].disp()[2] > same[1].disp()[2]:
						temp_river[i] = same[0]
					elif same[0].disp()[2] < same[1].disp()[2]:
						temp_river[i] = same[1]
	none_list = [e for e in range(len(river)) if temp_river[e] is None]
	kid_pos = random.sample(none_list, len(kid_list))
	# Inserting the babies randomly into the list
	for dummy in range(len(kid_list)):
		temp_river[kid_pos[dummy]] = kid_list[dummy]
	river = [x for x in temp_river]
	eco_list[step + 1] = [x for x in river]
	ecosystem = [0] * (time + 1)
	for step in range(time + 1):
		ecosystem[step] = []
	for creature in eco_list[step]:
		if creature is not None:
			ecosystem[step] += [creature.disp()[0]]
		else:
			ecosystem[step] += [None]
	return ecosystem


if __name__ == '__main__':
	print(eco(15, 10))







