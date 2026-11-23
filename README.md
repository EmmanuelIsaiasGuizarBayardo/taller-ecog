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

| Archivo en `img/` | Fuente | Licencia o permiso |
|---|---|---|
| `miller2012_fig1.jpg`, `miller2012_fig2.jpg`, `miller2012_fig3.jpg`, `miller2012_fig13.jpg` | Miller et al. (2012), *PLoS Computational Biology*, 8(9), e1002655, Figs. 1, 2, 3 y 13. https://doi.org/10.1371/journal.pcbi.1002655 | CC BY |
| `miller2010_fig1.jpg`, `miller2010_fig2.jpg`, `miller2010_fig3.jpg`, `miller2010_fig5.jpg` | Miller et al. (2010), *PNAS*, 107(9), 4430–4435, Figs. 1, 2, 3 y 5. https://doi.org/10.1073/pnas.0913697107 | Sin licencia abierta. Aviso del artículo: “Freely available online through the PNAS open access option”. PNAS permite usar sus figuras sin pedir permiso con fines no comerciales y educativos, citando la fuente |

Las figuras de PNAS se reproducen solo con fines educativos no comerciales. Quedan fuera de las
licencias MIT y CC BY 4.0 de este repositorio, y su uso no implica aval de los autores, de PNAS ni
de la National Academy of Sciences.

## Licencia

| Qué | Licencia |
|---|---|
| Código: celdas del cuaderno y `tools/` | MIT (`LICENSE`) |
| Texto didáctico del cuaderno | CC BY 4.0, salvo las figuras de terceros |
| Datos del Release `data-v1` | CC BY-SA 4.0, de Miller (2019) |
| Figuras en `img/` | La de su fuente, que no siempre es abierta; ver "Figuras" |

Para citar el taller, GitHub genera la referencia desde `CITATION.cff` con el botón
**Cite this repository**.

## Para quien mantiene el taller

El cuaderno del alumno se deriva del cuaderno del instructor, que no se publica:

```
uv run tools/make_student.py privado/taller_ecog_instructor.ipynb notebooks/taller_ecog_alumno.ipynb
```

uv instala `nbformat` solo para esa corrida, según la cabecera del script.
