def gerar_slug(titulo):
    slug = titulo.lower().strip() #.strip remove espaços em branco
    slug = slug.replace(" ", "-") #.replace substitui espaços por hífens
    for char in ".,!?;:()[]{}'\"/\\":
        slug = slug.replace(char, "")
    return slug

titulo = input("Título do post: ")
print(f"Slug: {gerar_slug(titulo)}")