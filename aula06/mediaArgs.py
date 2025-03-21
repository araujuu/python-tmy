def soma(a:float,b:float,*args) -> float:
    valores = [a,b] + list(args)
    return sum(valores)

def media(nota1:float, nota2:float, *args) -> float:
    return soma(nota1, nota2, *args) / (len(args)+2)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


print("a media das notas é igual a: ", media(nota1,nota2, nota3))