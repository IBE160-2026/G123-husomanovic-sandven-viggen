# G123 — DVR

Gruppeprosjekt i **IBE160 Programmering med KI** ved Høgskolen i Molde, høsten 2026 (15 studiepoeng).

Repoet inneholder gruppens applikasjon og dokumentasjon av utvikling, testing og kvalitetssikring med KI.

## Medlemmer

- Djani Husomanovic
- Ronja Flack Sandven
- Vilde G Viggen
- Majlinda Gjika

## Kom i gang

Krever Python 3.10 eller nyere (vi bruker 3.12). Har du ikke det, kan du bruke [uv](https://docs.astral.sh/uv/):

```bash
pip install --user uv          # eller se uv-dokumentasjonen
uv python install 3.12
uv venv --python 3.12 .venv
uv pip install --python .venv -r requirements.txt
```

Med vanlig Python 3.12:

```bash
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Kopier `.env.example` til `.env` og legg inn din egen `ANTHROPIC_API_KEY`.

```bash
.venv/bin/pytest                 # kjør testene
.venv/bin/streamlit run app.py   # start appen
```
