engenheiros = {'Joao', 'Nice', 'Sueli', 'Amanda'}
programadores = {'Joao', 'Sofia', 'Rafael', 'Amanda'}
gerentes = {'Nice', 'Sueli', 'Rafael', 'Joao'}
juncao = engenheiros | programadores | gerentes
engprog = engenheiros | programadores
progger = programadores | engenheiros

print (juncao)
print (engprog)
print (progger)
