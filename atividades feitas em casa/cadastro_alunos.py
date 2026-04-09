
alunos = {}
idades_unicas_set = set()


def adicionar_aluno(nome, idade, nota):
    alunos[nome] = (idade, nota)
    idades_unicas_set.add(idade)


def listar_alunos():
    for nome, (idade, nota) in alunos.items():
        print(f"{nome} - Idade: {idade}, Nota: {nota}")


def media_notas():
    if not alunos:
        return 0
    total = sum(nota for idade, nota in alunos.values())
    return total / len(alunos)


def aluno_topo():
    return max(alunos, key=lambda nome: alunos[nome][1])


def idades_unicas():
    return idades_unicas_set

adicionar_aluno("Ana", 20, 8.5)
adicionar_aluno("Bruno", 22, 7.0)
adicionar_aluno("Carla", 20, 9.2)

print("Alunos cadastrados:")
listar_alunos()

print(f"Média das notas: {media_notas():.1f}")
print(f"Melhor aluno: {aluno_topo()}")
print(f"Idades únicas: {sorted(idades_unicas())}")
