ehm = [[1,2,3],[2,3,4],[4,3,6]]
show = [sum(i)*2 for i in zip(*ehm)]
err1 = [(x[0]) for x in ehm]
new_lis= [1,2,3,4,5,6,7,8,9,10]
well = [0.0008, 0.0003, 0.005, 0.001, 0.0034, 0.005, 0.0048, 0.0003, 0.0016, 0.003, 0.0017, 0.0039, 0.0004, 0.0013, 0.0014, 0.0021, 0.0025, 0.0015, 0.0044, 0.0005, 0.0003, 0.0016, 0.0015, 0.0005, 0.0007, 0.0019, 0.0015, 0.0022, 0.0015, 0.0, 0.0047, 0.0053, 0.0016, 0.0031, 0.0007, 0.0021, 0.0023, 0.0006, 0.0034, 0.0021, 0.0027, 0.0019, 0.002, 0.0081, 0.0002, 0.0004, 0.0036, 0.0038, 0.0033, 0.0029, 0.0073, 0.0012, 0.0032, 0.0028, 0.0016, 0.0003, 0.004, 0.001, 0.001, 0.0003, 0.0029, 0.0026, 0.0027, 0.0049, 0.0009, 0.0041, 0.0043, 0.0053, 0.0019, 0.002, 0.0042, 0.0014, 0.0062, 0.0032, 0.0006, 0.005, 0.0025, 0.0087, 0.0014, 0.0029, 0.0016, 0.0042, 0.0075, 0.0011, 0.0008, 0.0014, 0.005, 0.0009, 0.0002, 0.001, 0.0014, 0.0008, 0.0018, 0.0007, 0.0018, 0.0014, 0.0012, 0.0063, 0.0009, 0.0014]

def trim_list(lis):
	sorting = sorted(lis)
	del sorting[94:99]
	del sorting[0:5]
	#trimmed = [i for i in sorting if i > sorting[4] and i < sorting[95]]
	return sorting
	#return sorting
eff = [2,5,4,1,6,7,9,3,8,10]
print len(well)
#print sorted(well)

print trim_list(well)
print len(trim_list(well))
#print new_lis[2:8]
#trim_list(eff)
#print ehm
#print err1