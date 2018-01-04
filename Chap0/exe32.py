hairs = ['brown','blond','red']
eyes = ['brown','blue','green']
weights = [1,2,3,4]
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies','dimws',3,'quarters']
for number in the_count:
	print "this is count %d" % number
	
# same as above
for fruit in fruits:
	print "A fruit of type: %s " % fruit

# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

elements = []
for i in range(0,6):
	print "adding %d to the list."% i
	elements.append(i)

for i in elements:
	print "Element was:%d" % i
	