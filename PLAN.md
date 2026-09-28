# Utviklingsplan: IBE160 Kursassistent v1

Plan for første versjon av kursassistenten beskrevet i [product-brief-kurs-faq-chatbot.md](product-brief-kurs-faq-chatbot.md): en RAG-chatbot i Python med Streamlit og ChromaDB. Planen er delt i små steg som kan testes hver for seg.

## Tekniske valg

| Del | Valg | Begrunnelse |
|---|---|---|
| Grensesnitt | Streamlit | Enkel chat-UI i ren Python |
| Vektordatabase | ChromaDB (lokal, persistent) | Ingen server å drifte |
| Embeddings | Lokal flerspråklig modell via `fastembed` | Gratis, fungerer på norsk, kjører uten PyTorch (fungerer også på Intel-Mac) |
| Svarmodell | Claude via Anthropic API (`claude-opus-5`) | Godt norsk, følger «svar kun fra kilden» og sier fra når svaret mangler, har innebygde kildehenvisninger (citations) |
| Python | 3.12 | Anthropic-pakken krever 3.10+ |

Svarmodellen ligger bak en egen funksjon, slik at vi kan bytte til en billigere Claude-modell eller teste en lokal modell (Ollama) som sammenligning i evalueringen.

## Mappestruktur

```
app.py                 # Streamlit-grensesnitt
src/ingest.py          # laste dokumenter og dele dem i biter
src/store.py           # ChromaDB-oppsett
src/retrieve.py        # søk og terskel for treff
src/generate.py        # prompt og kall til Claude
src/query_log.py       # anonym logging (ikke logging.py, som kolliderer med Pythons innebygde modul)
data/raw/              # kildedokumenter
data/sources.yaml      # metadata: tittel, lenke, type
eval/testset.yaml      # testspørsmål
eval/run_eval.py
tests/
```

## Stegene

Hvert steg har et tydelig punkt der det er ferdig, og kan testes før vi går videre.

### Fase 0: Grunnmur

**Steg 0: Prosjektoppsett** ✅ Ferdig
- venv med Python 3.12, `requirements.txt`, `.env.example` for API-nøkkelen og `pytest`.
- **Test:** `pytest` kjører, og `streamlit run app.py` viser en side.

**Steg 1: Kunnskapsbase og metadata**
- Legg 5–10 dokumenter i `data/raw/`: forelesningsnotater, oppgavetekster og emneinformasjon.
- Skriv `sources.yaml` med visningsnavn, URL eller sti og dokumenttype for hver fil.
- **Test:** Alle filene har metadata, og alle metadataoppføringene har en fil.

**Steg 2: Testsettet, laget tidlig**
- Skriv 20–30 spørsmål før vi bygger retrieval, så vi måler ærlig.
- Bruk tre typer spørsmål: besvarbare (med forventet kildedokument), uklare og utenfor scope.
- **Test:** Filen lastes og valideres mot et enkelt skjema. Dette er grunnlaget for alle suksesskriteriene i briefen.

### Fase 1: Indeksering

**Steg 3: Laste dokumenter**
- Gjør om PDF og Markdown til ren tekst, med sidetall eller overskrift der det er mulig.
- **Test:** Hvert dokument gir tekst som ikke er tom, og sidetallene er med.

**Steg 4: Dele opp tekst (chunking)**
- Start med rundt 500–800 tegn og litt overlapp. Del gjerne på overskrifter.
- Hver bit arver metadata: kilde, side og seksjon.
- **Test:** Enhetstester på størrelse og overlapp, og på at ingen metadata går tapt.

**Steg 5: Embeddings og ChromaDB**
- Lag embeddings lokalt med `fastembed` og lagre bitene i en persistent Chroma-samling. Bruk stabile ID-er, slik at ny indeksering ikke lager duplikater.
- **Test:** Antall lagrede biter er lik antall biter fra steg 4. Kjører vi indekseringen to ganger, blir antallet det samme.

### Fase 2: Retrieval (uten språkmodell)

**Steg 6: Søkefunksjon**
- `retrieve(spørsmål, k)` returnerer biter med avstand og metadata.
- **Test:** Et lite kommandolinjeverktøy skriver ut treffene for et spørsmål, slik at vi kan se dem manuelt.

**Steg 7: Måle retrieval mot testsettet**
- Mål hit@k: ligger forventet dokument blant de k beste treffene?
- Prøv ulike størrelser på bitene, verdier for k og embedding-modeller her. Det er gratis, fordi alt kjører lokalt.
- **Test:** Et tall vi kan sammenligne mellom forsøk. Mål: minst 90 % hit@5.

**Steg 8: Relevansterskel for fallback**
- Finn en avstandsgrense der svake treff regnes som «ingen treff».
- **Test:** Spørsmål utenfor scope havner under terskelen, og besvarbare spørsmål havner over den.

### Fase 3: Generering

**Steg 9: Prompt og kall til Claude**
- Systemprompten skal si tre ting: svar bare fra kildene, svar kort og på norsk, og si tydelig fra når kildene ikke er nok.
- Hver bit sendes som et eget dokument med `citations` slått på, slik at API-et returnerer nøyaktig hvilken tekst og kilde hver påstand bygger på.
- **Test:** Kall funksjonen med faste, håndskrevne kilder. Svaret skal ha sitater. Uten kilder skal svaret være en fallback.

**Steg 10: Koble retrieval og generering**
- Kjeden blir `answer(spørsmål) → {svar, kilder, usikker: bool}`.
- Kildene hentes fra sitatene i svaret og slås opp i `sources.yaml` for tittel og lenke. Det gir sporbarhet.
- Hvis terskelen fra steg 8 ikke nås, returneres fallback direkte uten kall til Claude.
- **Test:** Kjør hele kjeden fra kommandolinjen på 5 spørsmål av hver type.

### Fase 4: Grensesnitt

**Steg 11: Enkel chat i Streamlit**
- Bruk `st.chat_input` og `st.chat_message`, og strøm svaret slik at teksten vises mens den skrives.
- Vis kildene under svaret med navn og lenke. Gi usikre svar et tydelig visuelt merke.
- Hold øye med svartiden, som skal være under 20 sekunder.
- **Test:** Manuell sjekkliste: spørsmål, svar, kilde som kan klikkes, og fallback som vises tydelig.

**Steg 12: Oppfølgingsspørsmål**
- Skriv oppfølgingsspørsmålet om til et selvstendig spørsmål ved hjelp av samtalehistorikken før retrieval. For eksempel blir «Hva med fristen for den?» til «Hva er fristen for oblig 2?».
- **Test:** 3–5 par av spørsmål og oppfølgingsspørsmål i testsettet. Sjekk at det omskrevne spørsmålet gir riktig treff.

**Steg 13: Uklare spørsmål**
- Når treffene spriker over flere dokumenttyper, eller spørsmålet er veldig kort, ber boten om presisering: gjelder det teori, prosjekt eller praktisk info?
- **Test:** De uklare spørsmålene i testsettet gir et presiseringsspørsmål.

### Fase 5: Logging og evaluering

**Steg 14: Anonym logging**
- `src/query_log.py` logger tidsstempel, spørsmål, ID-er og avstander for treffene, svar, om svaret var fallback, og svartid. Ikke bruker-ID eller IP.
- Bruk JSONL eller SQLite.
- **Test:** Én samtale gir riktige loggposter uten personopplysninger.

**Steg 15: Evalueringsskript**
- Kjør hele testsettet gjennom `answer()` og regn ut tre tall:
  - riktig kildedokument (mål: 90 %)
  - riktig fallback utenfor scope (mål: 90 %)
  - relevans for besvarbare spørsmål (mål: 80 %), vurdert manuelt eller med en språkmodell som dommer
- Hver kjøring koster litt API-bruk. Kjør den bevisst, ikke ved hver endring.
- Valgfritt: kjør testsettet også mot en lokal modell via Ollama som sammenligning.
- **Test:** Skriptet lager en rapport. Resultatene lagres i repoet, slik at vi kan dokumentere forbedringer.

**Steg 16: Brukertest**
- La 5 testbrukere prøve løsningen uten veiledning, og spør dem om påstanden «Det var enkelt å finne informasjonen jeg trengte» på en skala fra 1 til 5.
- **Test:** Kriteriene fra briefen: minst fire av fem finner fram, og snittet er minst 4.

## Milepæler

- **Milepæl A (steg 0–8):** Retrieval er målt og fungerer, uten språkmodell. Dette er det viktigste fundamentet.
- **Milepæl B (steg 9–11):** Minimal chatbot med kilder og fallback. Dette er første versjon vi kan vise fram.
- **Milepæl C (steg 12–16):** Samtalekontekst, logging og dokumentert evaluering.

Steg 1–2 (data og testsett) og steg 3–5 (indeksering) kan gjøres parallelt av ulike gruppemedlemmer.
