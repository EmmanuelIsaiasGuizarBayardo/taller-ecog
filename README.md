# Taller: procesamiento de señales intracraneales (ECoG) con Python

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EmmanuelIsaiasGuizarBayardo/taller-ecog/blob/main/notebooks/taller_ecog_alumno.ipynb)

Taller práctico de neuroingeniería clínica: espectro de potencia, modelo 1/f, envolvente de alta
frecuencia, mapeo funcional y decodificación con registros ECoG de pacientes.

**Para empezar:** haz clic en *Open in Colab* y ejecuta las celdas en orden. Los datos se
descargan solos desde el *Release* `data-v1` de este repositorio.

## Datos

- Miller, K. J. (2019). *A library of human electrocorticographic data and analyses*. Stanford Digital
  Repository. https://purl.stanford.edu/zk881ps0522 (licencia CC BY-SA 4.0).
- Artículo descriptivo: Miller, K. J. (2019). *Nature Human Behaviour, 3*(11), 1225–1235.
  https://doi.org/10.1038/s41562-019-0678-3
- `motor_imagery.npz` y `fingerflex.npz` (Release `data-v1`) son la versión curada por Neuromatch
  Academy, tal como se obtuvo de su OSF. Se redistribuyen con atribución y bajo la misma licencia
  (CC BY-SA 4.0); cualquier adaptación de los datos debe conservarla.

## Figuras

Figuras de Miller et al. (2012) bajo licencia CC BY; figuras de Miller et al. (2010), PNAS,
reproducidas con fines educativos no comerciales citando la fuente.

## Licencia

| Qué | Licencia |
|---|---|
| Código: celdas del cuaderno y `tools/` | MIT (`LICENSE`) |
| Texto didáctico del cuaderno | CC BY 4.0 |
| Datos del Release `data-v1` | CC BY-SA 4.0, de Miller (2019) |
| Figuras en `img/` | La de su fuente; ver "Figuras" |

Para citar el taller, GitHub genera la referencia desde `CITATION.cff` con el botón
**Cite this repository**.

## Para quien mantiene el taller

El cuaderno del alumno se deriva del cuaderno del instructor, que no se publica:

```
uv run tools/make_student.py privado/taller_ecog_instructor.ipynb notebooks/taller_ecog_alumno.ipynb
```

uv instala `nbformat` solo para esa corrida, según la cabecera del script.
