with open('./frase1.txt') as text:
    r  = text.readlines()
print(r)

with open('./frase1.txt') as text:
    for linhas in text:
        print(linhas)
        
        
with open('./frase2.txt','w') as text:
    text.write('Olá a todos!!')