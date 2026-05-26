# Cazador de Contrasenas

Proyecto final del curso de Programacion.

Curso: Programacion  
Codigo: 213023  
Grupo: 382

## Descripcion

Este programa implementa un juego interactivo en Python llamado **Cazador de Contrasenas**. El usuario ingresa la longitud de una contrasena, el sistema genera una clave aleatoria y valida si cumple las reglas de seguridad. Si la contrasena es valida, se abre un cofre positivo y se suman puntos. Si no cumple las reglas o hay un error de entrada, se abre un cofre maldito y se restan puntos.

## Reglas de la contrasena

- Minimo 8 caracteres.
- Al menos una letra mayuscula.
- Al menos una letra minuscula.
- Al menos un numero.
- Al menos un caracter especial.
- No puede tener caracteres repetidos.

## Clases principales

- `Contrasena`: genera y valida contrasenas.
- `Cofre`: representa cofres comunes, raros, legendarios y malditos.
- `JuegoCazador`: controla rondas, puntaje y flujo del juego.

## Como ejecutar

Desde la terminal:

```bash
python juego_cazador_contrasenas.py
```

## Autor

Origen: Daniela  
Nombre: Daniela Fernanda Aguirre Acosta  
Grupo: 382
