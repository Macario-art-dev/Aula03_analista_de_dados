nome = input("Nome: ")
salario = float(input("Salário bruto: ").replace(",","."))
if(salario >= 3000 ):
    inss = salario*0.11
elif(salario >= 2000):
    inss = salario*0.09
else:
    inss = salario*0.08
if(salario >= 2000 ):
    vale_transporte = salario*0.06
else:
    vale_transporte = salario*0.05
if(salario >= 3000 ):
    bonus=  300
else:
    bonus =  200    
if(salario >= 3000 ):
    cargo = "Acionista"
elif(salario >= 2000):
    cargo = "Gerente"
else:
    cargo = "vedendor"
salariol = salario - (inss + vale_transporte) + bonus 
print(f"Nome: {nome}")
print(f"Salário Bruto: {salario:.2f}".replace(".",","))
print(f"INSS: {inss:.2f}".replace(".",","))
print(f"Vale transporte: R$ {vale_transporte:.2f}:".replace(".",","))
print(f"Bônus: {bonus:.2f}".replace(".",","))
print(f"Cargo: {cargo}")
print(f"Salário liquido: {salariol:.2f}".replace(".",","))