# Building an ecosystem
import random
class animal:
    # ._name vs. .name
    def __init__(self, kind, gender, strength):
        self.name = kind
        self.sex = gender
        self.power = strength

    def create(self, kind):
        '''Create a random animal'''
        if random.randint(0, 1):
            gender = 'male'
        else:
            gender = 'female'
        strength = random.random()
        new_animal = animal(kind, gender, strength)
        return new_animal


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
                kid = animal(0, 0, 0)
                kid.create(self.name)
                return self, other, kid
        else:
            if self.name == 'bear':
                return self
            else:
                return other

    def disp(self):
        '''Displays the attributes of the animal'''
        return self.name, self.sex, self.power


def eco(river_size, time):
    '''Ecosystem simulation'''
    random.seed(4)
    actual = int(round(random.gauss(river_size // 2, river_size // 10)))
    print('total population', actual)
    fish_num = random.randint(0, actual)
    print('fish', fish_num)
    bear_num = actual - fish_num
    print('bear', bear_num)
    bear = [animal(0, 0, 0)] * bear_num
    for i in range(bear_num):
        bear[i] = bear[i].create('bear')
    fish = [animal(0, 0, 0)] * fish_num
    for i in range(fish_num):
        fish[i] = fish[i].create('fish')
    river = bear + fish + [None] * (river_size - actual)
    random.shuffle(river)
    eco_list = [[]] * (time + 1)
    eco_list[0] = [x for x in river]
    k = []
    for m in river:
        if m != None:
            k += [m.disp()[0]]
        else:
            k+= [None]
    print(k)
    for step in range(time):
        temp_river = [None] * river_size
        pos_list1 = [i for i in range(len(river)) if river[i] != None]
        print('old pos', pos_list1)
        pos_list2 = [elem + random.randint(-1, 1) for elem in pos_list1]
        print('new pos', pos_list2)
        if pos_list2[0] < 0:
            pos_list2 = pos_list2[1:]
            pos_list1 = pos_list1[1:]
            temp_river[0] = None
        if pos_list2[-1] > len(river)-1:
            temp_river[-1] = None
            pos_list2 = pos_list2[:-1]
            pos_list1 = pos_list1[:-1]
        kid_list = []
        for i in range(len(river)):
            ind = [iter for iter, val in enumerate(pos_list2) if val == i]
            print(ind)
            if len(ind) == 1:
                tem = river[pos_list1[ind[0]]]
                if pos_list1[ind[0]] not in pos_list2:
                    river[pos_list1[ind[0]]] = None
                river[i] = tem
            elif len(ind) == 2:
                print(river)
                new = river[pos_list1[ind[0]]] + river[pos_list1[ind[1]]]
                print(river[pos_list1[ind[0]]].disp(), river[pos_list1[ind[1]]].disp())
                print(new.disp())
                if type(new).__name__ == 'tuple':
                    kid_list += [new[2]]
                else:
                    if pos_list1[ind[0]] not in pos_list2:
                        river[pos_list1[ind[0]]] = None
                    if pos_list1[ind[1]] not in pos_list2:
                        river[pos_list1[ind[1]]] = None
                    river[i] = new
                    print(river)
            elif len(ind) == 3:
                act = [river[pos_list1[ind[z]]].disp() for z in range(3)]
                if act[0][0] == act[1][0] == act[2][0]:
                    if act[0][1] == act[1][1] == act[2][1]:
                        tem = river[pos_list1[ind[0]]] + river[pos_list1[ind[1]]] + river[pos_list1[ind[2]]]
                        river[pos_list1[ind[0]]] = None
                        river[pos_list1[ind[1]]] = None
                        river[pos_list1[ind[2]]] = None
                        river[i] = tem
                    else:
                        if act[0][1] == act[1][1]:
                            same = [river[pos_list1[ind[0]]], river[pos_list1[ind[1]]]]
                            if same[0].disp()[2] > same[1].disp()[2]:
                                river[pos_list1[ind[1]]] = None
                            else:
                                river[pos_list1[ind[0]]] = None
                            nsame = river[pos_list1[ind[2]]]
                        elif act[1][1] == act[2][1]:
                            same = [river[pos_list1[ind[1]]], river[pos_list1[ind[2]]]]
                            if same[0].disp()[2] > same[1].disp()[2]:
                                river[pos_list1[ind[2]]] = None
                            else:
                                river[pos_list1[ind[1]]] = None
                            nsame = river[pos_list1[ind[0]]]
                        else:
                            same = [river[pos_list1[ind[0]]], river[pos_list1[ind[2]]]]
                            if same[0].disp()[2] > same[1].disp()[2]:
                                river[pos_list1[ind[2]]] = None
                            else:
                                river[pos_list1[ind[0]]] = None
                            nsame = river[pos_list1[ind[1]]]
                        new = (same[0] + same[1]) + nsame
                        kid_list += [new[2]]
                else:
                    if act[0][0] == act[1][0]:
                        same = [river[pos_list1[ind[0]]], river[pos_list1[ind[1]]]]
                        s_ind = [ind[0], ind[1]]
                        nsame = river[pos_list1[ind[2]]]
                        river[pos_list1[ind[2]]] = None
                    elif act[1][0] == act[2][0]:
                        same = [river[pos_list1[ind[1]]], river[pos_list1[ind[2]]]]
                        s_ind = [ind[1], ind[2]]
                        nsame = river[pos_list1[ind[0]]]
                        river[pos_list1[ind[0]]] = None
                    else:
                        same = [river[pos_list1[ind[0]]], river[pos_list1[ind[2]]]]
                        s_ind = [ind[0], ind[2]]
                        nsame = river[pos_list1[ind[1]]]
                        river[pos_list1[ind[1]]] = None
                    new = (nsame + same[0]) + same[1]
                    if type(new).__name__ == 'tuple':
                        kid_list += [new[2]]
                    else:
                        if same[0].disp()[0] == 'fish':
                            river[i] = nsame
                        elif same[0].disp()[2] > same[1].disp()[2]:
                            river[i] = same[0]
                        elif same[0].disp()[2] < same[1].disp()[2]:
                            river[i] = same[1]
                        river[pos_list1[s_ind[0]]] = None
                        river[pos_list1[s_ind[1]]] = None
        none_list = [i for i in range(len(river)) if river[i] == None]
        kid_pos = random.sample(none_list, len(kid_list))
        for i in range(len(kid_list)):
            river[kid_pos[i]] = kid_list[i]
        eco_list[step + 1] = [x for x in river]
    ecosystem = [0] * (time + 1)
    for step in range(time + 1):
        ecosystem[step] = []
        for creature in eco_list[step]:
            if creature != None:
                ecosystem[step] += [creature.disp()[0]]
            else:
                ecosystem[step] += [None]
    return ecosystem


a = animal('bear', 'male', 0.1)
b = animal('fish', 'female', 0.2)
c = animal('bear', 'female', 0.5)
d = animal('bear', 'male', 0.3)
g = [animal(0, 0, 0)] * 2
g[0] = g[0].create('fish')
g[1] = g[1].create('bear')
e = (c + b) + (a + d)


print(eco(10, 1))








