usuarios = {
    "1": {"nombre": "luis", "edad": 45, "pais": "españa"},
    "2": {"nombre": "roberto", "edad": 40, "pais": "mexico"},
    "3": {"nombre": "sandra", "edad": 30, "pais": "mexico"},
    "4": {"nombre": "vadim", "edad": 27, "pais": "rusia"}
}

for c in usuarios.keys():
    print(c)

for v in usuarios.values():
    print(v)

for c, v in usuarios.items():
    print(c,"->",v)
    
for id in usuarios:
    print(f"clave: {id}")
    for valor in usuarios[id]:
        print(f"valor: {valor}")

for c in usuarios.keys():
    print(f"clave: {c}")
    for v in usuarios[c].keys():
        print(f"valor: {v}")

for c in usuarios:
    print(f" {c}")
    for v in usuarios[c].values():
        print(f" {v}")

for c in usuarios:
    print(f"{c}")
    for v in usuarios[c].items():
        print(f"{v}")
        