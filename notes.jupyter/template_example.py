from string import Template

s = 'https://${server}/${z}/${x}/${y}.png'
t = Template(s)
D = { 'server':'openstreetmap.org',
      'x':30,'y':40,'z':10}
      
v = t.substitute(D)
print(v)

'''
https://openstreetmap.org/10/30/40.png
'''