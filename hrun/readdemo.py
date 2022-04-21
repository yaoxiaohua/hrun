import yaml
import hrun

fp = open('demo.yml','r',encoding='utf-8')
f = fp.read()
print(f)

d = yaml.load(f) #yaml.load(f)
print(d)




fp.close()

