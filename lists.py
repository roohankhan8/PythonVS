# Lists

colleges = ['Delhi', 'Formen', 'Adamjee']
colleges.append('Bufferzone')
colleges.insert(2, 'DJ')
colleges.remove('DJ')


print(colleges[0])

colleges[0] = 'Islamia'
print(colleges[0])

print(colleges[1:5] + ['NED'] )

print(len(colleges))
print(max(colleges))
print(min(colleges))
