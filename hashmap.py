class HashMap:

    def __init__(self):
        self.Size = 7
        self.hashmap = [[] for i in range(0, self.Size)]

    def Hash(self, tup):
        if type(tup) == str:
            raise KeyError('key is never a string')
        leftin = tup[0]
        rightin = tup[1]

        def Find_Factor(tup2):
            if type(tup2) == str:
                raise KeyError('key is never a string')
            # print(tuple, 'tuple')
            Left = tup2[0]
            # print(Left, 'left')
            Right = tup2[1]
            # print(Right, 'right')

            fac_list = []
            for i in range(Left):
                fac_list.append(i)

            # print(fac_list)
            Factor = sum(fac_list)

            # print(Factor, 'factor is')
            return Factor

        Factor = Find_Factor(tup)
        Hashval = (leftin + rightin) + Factor
        return Hashval

    def set(self, key, value):
        if type(key) == str:
            raise KeyError('key is never a string')
        if type(key) != tuple:
            raise KeyError
        # as long as I go in order by coordinates, load factor will never be more than 1.
        newtup = key
        hash_key = self.Hash(key)
        # print(hash_key, 'hashkey')

        if hash_key == 0:
            self.hashmap[0] = [(0, 0), 0]
        if len(self.hashmap) - 1 < hash_key or self.hashmap == hash_key:
            # print('too big key')
            self.Size = hash_key + 1
            self.hashmap = self.hashmap + [[] for _ in range(0, (self.Size - len(self.hashmap)))]

        self.hashmap[hash_key] = [(key), value]

    def get(self, key):
        lefty = key[0]
        righty = key[1]
        if righty > lefty:
            raise KeyError
        if type(key) != tuple:
            raise KeyError

        hash_key = self.Hash(key)
        print(hash_key, "hashkey here")
        print(len(self.hashmap),'length hashmap rn')

        for i in self.hashmap:
            if len(i)>2:
                raise KeyError

        if hash_key >= len(self.hashmap):
            raise KeyError
        if len(self.hashmap[hash_key]) == 0:
            raise KeyError
        if self.hashmap[hash_key]:
            value = (self.hashmap[hash_key][1])
            return value

        else:
            raise KeyError


    def capacity(self):
        cap = (self.Size)
        # print(self.Size)

        # print(len(self.hashmap))
        return cap


    def clear(self):

        self.Size = 7
        self.hashmap = [[] for i in range(0, self.Size)]

    def size(self):
        count_size = 0
        for i in self.hashmap:
            if len(i) != 0:
                count_size +=1
        return count_size

    def keys(self):
        keylist = []
        for i in self.hashmap:
            if len(i) !=0:
                keylist.append(i[0])
        return keylist

    def remove(self,key):

        length = len(self.hashmap)
        print(length,'length')
        hash_val = self.Hash(key)
        print(hash_val,'hashval')
        if hash_val >= length:
            return
        for i in self.hashmap:
            # print(i)

            if len(i) !=0 and i[0][0]<i[0][1]:
                return
        if self.hashmap[hash_val]:
            self.hashmap[hash_val]= []













H = HashMap()
# print(H.hashmap)
# print(H.Hash((3,1)),'hash testing')
# print(H.size,'size right now')
# print(H.hashmap)
(H.set((0, 0), 0))
(H.set((1, 0), 100))
(H.set((1, 1), 100))
(H.set((2, 0), 150))
(H.set((2, 1), 300))
(H.set((2, 2), 150))
H.set((3, 0), 175)

H.set((3, 1), 425)
H.set((3, 2), 425)
H.set((3, 3), 425)
H.set((4, 0), 425)
H.set((4, 1), 425)
#
# H.set((4,2),625)
# H.set((5, 1), 700)

# print(H.size,'size right last')
# print(H.hashmap)
# H.set((7, 5), 600)
print(H.hashmap)
print(H.remove((2,0)))
print(H.hashmap)


# print(H.get((1,1)))
# print(H.get((3,2)))
# print(H.get((4,3)

# print(H.get((2,1)))
# print(H.get((2,3)))

