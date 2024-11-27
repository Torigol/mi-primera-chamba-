materia = {
   "nombre": "Programación",
   "codigo": "INFO2",
   "profesor": "Mari García",
   "horarios": ["Lunes 9:00-11:00", "Miércoles 9:00-11:00"],
   "creditos": 8,
   "nivel": "Intermedio",
   "prerequisitos": ["Computación 1"],
   "descripcion": "Desarrollo de algoritmos",
}
print (materia[ "profesor"])

alumno = {
    "nombre": "Eder Rodarte",
    "matricula": "A123456789",
    "edad": 17,
    "semestre": "quinto",
    "calificaciones": {
        "Matemáticas": 8.5,
        "Física": 9.0,
        "Programación": 9.5,
        "Química": 8.8,
    },
    "direccion": {
       "calle": "Av. Libertad 456",
       "ciudad": "Ciudad x",
       "codigo_posta": "12345",
    },
    "telefono": "555-12842-816",
    "email": "ale.pvr@example.com"
}
print (alumno ["nombre"])
print (alumno["calificaciones"])
              
print("La calificación del alumno en programación es:")
print(alumno ["calificaciones"] ["Programación"])