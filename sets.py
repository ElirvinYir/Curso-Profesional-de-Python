# Elaborar dos sets y realizar la unión(|), la intersección (&), la diferencia(-) y la diferencia simétrica entre ambos(^)

my_set_1 = {"Hola", 5, 87.5, False, 74, 98, 9, "Platzi"}
my_set_2 = {5, 9, "Hello", True, 98, 98, 55.2, 1, "Platzi"}

# unión
    # Une ambos sets y elimia los elementos repetidos, solamente conservando uno si es que está repetido
my_union_set = my_set_1 | my_set_2
print(my_union_set)

# Intersección
    # Resultado de combinar ambos sets pero solamente conservando los elementos que tienen en común
    # Quita todos los elementos que se repitan en el set 1 y sólo conserva los que no se repiten
my_intersection_set = my_set_1 & my_set_2
print(my_intersection_set)

# diferencia
    # Resultado de tomar dos sets, y de uno, quitar todos los elementos que tiene el otro 
my_difference_set = my_set_1 - my_set_2
my_difference_set_2 = my_set_2 - my_set_1
print(my_difference_set)
print(my_difference_set_2)


# diferencia simétrica
    # Contrario de la intersección
    # Resultado de quedarme con los elementos de ambos set pero sin los que se comparten 
my_simetric_difference_set = my_set_1 ^ my_set_2
print(my_simetric_difference_set)