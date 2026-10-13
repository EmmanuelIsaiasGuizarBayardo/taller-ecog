"""Deriva el notebook de alumno a partir del de instructor (fuente única).

Uso (desde la raíz del repo):
    python tools/make_student.py privado/taller_ecog_instructor.ipynb notebooks/taller_ecog_alumno.ipynb

Convenciones:
- ``### BEGIN SOLUTION`` / ``### END SOLUTION``: el bloque se elimina.
- ``# STUDENT: <código>``: se convierte en ``<código>``.
- Markdown con ``<!-- INSTRUCTOR -->``: desde el marcador hasta el final de la celda se elimina;
  si la celda queda vacía, se borra completa.
- Se limpian salidas y contadores de ejecución.
"""
from __future__ import annotations

import re
import sys

import nbformat as nbf

INSTRUCTOR_TAG = "<!-- INSTRUCTOR -->"
SOLUTION_RE = re.compile(r"[ \t]*### BEGIN SOLUTION.*?### END SOLUTION[ \t]*\n?", re.S)
STUDENT_RE = re.compile(r"^([ \t]*)# STUDENT: ?(.*)$", re.M)


def strip_markdown(src: str) -> str | None:
    """Quita los bloques de instructor; si la celda queda vacía devuelve None."""
    if INSTRUCTOR_TAG not in src:
        return src
    keep = src.split(INSTRUCTOR_TAG)[0].rstrip()
    return keep or None


def strip_code(src: str) -> str:
    src = SOLUTION_RE.sub("", src)
    return STUDENT_RE.sub(r"\1\2", src)


def main(src_path: str, dst_path: str) -> None:
    nb = nbf.read(src_path, as_version=4)
    out = []
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            new = strip_markdown(cell.source)
            if new is None:
                continue
            cell.source = new
        elif cell.cell_type == "code":
            cell.source = strip_code(cell.source)
            cell.outputs, cell.execution_count = [], None
        out.append(cell)
    nb.cells = out
    leftovers = [c.source for c in out if "SOLUTION" in c.source or INSTRUCTOR_TAG in c.source]
    assert not leftovers, "Quedaron marcadores sin procesar"
    nbf.write(nb, dst_path)
    print(f"{dst_path}: {len(out)} celdas")


if __name__ == "__main__":
    main(*sys.argv[1:3])
