
from pathlib import Path
import sys

TARGETS = [
    "data/consultar-olinda-bi.json",
    "data/Relatorio_IPES_Escolas.csv",
    "data/Sistec_Cursos_Tecnicos_ativos_120922.csv",
    "data/microdados_censo_escolar_2024/dados/microdados_ed_basica_2024.csv",
    "data/microdados_censo_escolar_2024/dados/suplemento_cursos_tecnicos_2024.csv",
]

def read_text_head(p: Path, n=50):
    # Try UTF-8 then Latin-1
    for enc in ("utf-8", "latin-1"):
        try:
            with p.open("r", encoding=enc, errors="replace") as f:
                lines = []
                for i, line in enumerate(f):
                    if i >= n:
                        break
                    lines.append(line.rstrip("\n"))
                return enc, lines
        except Exception as e:
            last_err = e
    raise last_err

def main():
    base = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    print(f"Base dir: {base.resolve()}")
    for rel in TARGETS:
        p = base / rel
        print("\n" + "="*90)
        print(f"FILE: {p}")
        if not p.exists():
            print("  -> NOT FOUND")
            continue
        try:
            enc, head = read_text_head(p, n=50)
            print(f"  -> Encoding used: {enc}")
            print("-- first 50 lines (raw) --")
            for ln in head:
                print(ln)
        except Exception as e:
            print(f"  -> Error reading file: {e}")

if __name__ == "__main__":
    main()
