num = input('Enter a number (decimal or integer): ')
# type your code here
sf = num.replace(".", "")
sf = sf.strip().lstrip("0")
sf = len(sf)

# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')