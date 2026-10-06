# Tilbakemelding på product brief

| | |
|---|---|
| **Gruppe** | G123 – G123-husomanovic-sandven-viggen |
| **Product brief** | `product-brief-kurs-faq-chatbot.md` (commit `ace56c4`) |
| **Tilbakemelding fra** | Faglærer i IBE160 (utarbeidet med KI-støtte) |
| **Dato** | 2026-10-06 |

Jeg har også sett på `PLAN.md`, `requirements.txt` og `.env.example`, som viser at dere har startet på oppsettet (steg 0).

## Samlet vurdering

- **Godt utgangspunkt.** Gruppen kan gå videre som planlagt.

**Det som er bra:**

1. Problemet er godt konkretisert med sju typiske situasjoner (sjekke krav til en innlevering, finne hvor RAG ble gjennomgått, se om en frist er endret), og brukerreisen «spørsmål → emnespesifikt svar → synlig kilde → videre lesing» er tydelig.
2. Suksesskriteriene er blant de beste jeg har sett: et forhåndsdefinert testsett med besvarbare, uklare og utenfor-scope-spørsmål, og målbare terskler (minst 80 % relevante svar, 90 % riktige kildehenvisninger, 90 % ærlig fallback). Dette kan bli en automatisk evaluering.
3. Scope er stramt og godt begrunnet: ett emne, kontrollert kunnskapsbase og en lang og konkret «OUT»-liste (ingen generell programmeringsassistent, ingen vurdering av studentarbeid, ingen LMS-integrasjon). Planen om å lage testsettet *før* retrieval bygges, er et svært godt grep.

**De viktigste endringene:**

1. Briefen sier ikke hvordan sensor kan kjøre appen uten deres Anthropic-nøkkel. `PLAN.md` velger Claude via API; legg til en plan for demomodus (f.eks. lagrede svar for testsettet eller en enkel modus som bare viser de mest relevante kildeutdragene uten LLM).
2. Avklar hvilke emneressurser som kan ligge i et offentlig repo. Lag kunnskapsbasen av materiale som allerede er offentlig (f.eks. emnebeskrivelsen) eller som dere har lov til å publisere, og beskriv valget.
3. Brukeropplevelses-kriteriene med testbrukere (4 av 5, snitt 4 av 5) er gode, men krever at dere planlegger en brukertest. Sett av tid til den i planen.

## Vanskelighetsgrad og gjennomførbarhet

### Vurdert vanskelighetsgrad

- **Middels**

**Sammenlignbart med:** 7) Kurs-FAQ-chatbot (middels). Briefen er en direkte og godt avgrenset utgave av dette forslaget.

**Begrunnelse:**

| Faktor | Nivå (lav / middels / høy) | Kommentar |
|---|---|---|
| Domenelogikk – hvor mange og hvor kompliserte regler og beregninger må stemme? | Middels | Retrieval-strategi, terskel for treff, fallback-regler og kildehenvisning. Lite tradisjonell forretningslogikk, men mange valg som påvirker kvaliteten. |
| Datamodell – antall entiteter og relasjoner mellom dem | Lav | Dokument, tekstbit (chunk) med metadata, samtale og logg. Ingen brukerdata. |
| Brukere, roller og innlogging | Lav | Ingen innlogging i v1. Én brukerrolle. |
| KI-funksjonalitet i appen, f.eks. kall til språkmodell, prompts i koden og håndtering av usikre svar | Høy | RAG med embeddings, vektordatabase, prompt som begrenser svar til kildene, kildehenvisning, oppfølgingsspørsmål og fallback. Dette er kjernen. |
| Integrasjoner og eksterne tjenester, f.eks. API-er, betaling og e-post | Middels | Anthropic API for svar. Embeddings kjøres lokalt, som er et godt valg. |
| Sanntid, samtidighet eller flere brukere som påvirker hverandre | Lav | Ikke relevant. |
| Filhåndtering, f.eks. opplasting, PDF-lesing og eksport | Middels | Innlesing av PDF og Markdown med sidetall eller overskrift til kunnskapsbasen. Gjøres av gruppen, ikke av brukeren. |
| Sikkerhet og personvern | Lav | Logging uten unødvendige personopplysninger er allerede tatt med. |

**Hva vanskelighetsgraden betyr for dere:**

- _Middels:_ Et godt balansert valg. Pass på at kjerneflyten blir ferdig og stabil før dere legger til mer. Her betyr det: få spørsmål → riktig kilde → svar med henvisning → fallback til å virke og måle seg mot testsettet, før dere bruker tid på oppfølgingsspørsmål og finpuss av grensesnittet.

### Gjennomførbarhet med BMAD og Claude Code

Dere skal planlegge med BMAD (product brief → PRD → arkitektur → epics og stories) og implementere med Claude Code. Vurderingen under tar hensyn til at det må være tid til hele denne flyten, og til testing, retting og README til slutt.

| Spørsmål | Vurdering (OK / risiko / stor risiko) | Kommentar |
|---|---|---|
| **Tid og omfang** – kan v1 realistisk bli ferdig og stabil i løpet av semesteret, med tid til flere iterasjoner? | OK | Sju avgrensede punkter i «IN» og en trinnvis plan. Realistisk for tre personer. |
| **BMAD-flyten** – er briefen konkret nok til at PRD, arkitektur og stories kan lages uten store hull, og blir det overkommelig mange stories? | Risiko | Briefen er konkret nok. Men `PLAN.md` er laget direkte fra briefen uten PRD, arkitektur og stories. Sørg for at BMAD-dokumentene også kommer på plass, slik at sporbarheten fra plan til kode blir synlig. |
| **Egnet for Claude Code** – bruker løsningen en vanlig, godt dokumentert teknologistakk som Claude Code håndterer godt, eller krever den nisjeteknologi, spesialmaskinvare eller mye manuell konfigurasjon? | OK | Python, Streamlit, ChromaDB og fastembed er godt dokumentert og kjører lokalt. |
| **Kontroll på KI-ens arbeid** – kan gruppen selv avgjøre om koden gjør det riktige? Krever domenet kunnskap gruppen ikke har, f.eks. avanserte beregninger eller fagregler, så er det vanskelig å kvalitetssikre. | OK | Dere kjenner emnet selv og kan avgjøre om svar og kilde stemmer. Testsettet med forventet kildedokument gjør kontrollen systematisk. |
| **Testbarhet** – finnes det tydelige regler og forventede resultater som tester kan skrives mot? | OK | Svært godt: testsett med forventet kilde og målbare terskler, i tillegg til enhetstester per steg i planen. |
| **Kjørbar for sensor** – kan appen kjøres lokalt etter README, uten gruppens nøkler, betalte kontoer eller egen infrastruktur? | Risiko | Alt unntatt svarmodellen kjører lokalt, og `.env.example` finnes. Men uten nøkkel får sensor ingen svar. Planlegg demomodus eller beskriv tydelig hvordan sensor bruker egen nøkkel. |
| **Avhengigheter og kostnader** – krever løsningen betalte API-er, f.eks. språkmodeller, og finnes det en plan for kostnad, testmodus eller mock-data? | Risiko | `PLAN.md` velger en av de dyreste modellene. Evaluering med 20–30 spørsmål mange ganger koster. Vurder en billigere modell som standard, og at svarfunksjonen kan byttes, slik planen allerede legger opp til. |

**Konklusjon om gjennomførbarhet:**

- **Gjennomførbart som beskrevet.**

**Forslag til justering av omfang eller vanskelighetsgrad:**

1. Legg inn en «uten LLM»-modus som viser de mest relevante kildeutdragene med henvisning. Den gjør appen kjørbar for alle, og den er nyttig som sammenligning i evalueringen (hva tilfører språkmodellen?).
2. Bruk sammenligningen mellom modeller (Claude-modeller og eventuelt Ollama) som en del av evalueringen. Det løfter prosjektet innenfor middels uten å utvide omfanget.

## Hvorfor product brief er viktig for mappen

Product brief er utgangspunktet for PRD, arkitektur, stories og til slutt koden. Del 1 av mappen vurderes blant annet på om sensor kan følge en sporbar vei fra plan til ferdig app. Den vurderes også på om appen gjør det dere har beskrevet, om den er testet, om den er godt designet, og om den kan kjøres etter README. Et uklart, for stort eller for lite brief gjør alt dette vanskeligere senere. Det er mye enklere å rette nå enn sent i semesteret.

## 1. Gjennomgang av briefens deler

| Del av brief | Status | Kommentar |
|---|---|---|
| Executive Summary – er det klart hva appen er, og hvilket problem den løser? | OK | Tydelig: en chatbot for IBE160 som svarer kort med kilde fra en avgrenset kunnskapsbase, og sier fra når den ikke vet. |
| The Problem – er problemet konkret, med reelle situasjoner og brukere? | OK | Sju konkrete situasjoner og en god forklaring av hvorfor generelle chatboter ikke løser problemet. |
| The Solution – beskriver løsningen brukeropplevelsen, ikke bare teknologi? | OK | Beskriver svarets innhold og et konkret eksempel på en dialog, uten teknologi. |
| What Makes This Different – er vurderingen ærlig og realistisk? | OK | Ærlig: ingen egen språkmodell, forskjellen ligger i retrieval, kildebruk og fallback for ett emne. |
| Who This Serves – er primærbrukerne tydelige, og vet vi hva de trenger? | OK | IBE160-studenter som primær og faglærer som sekundær, med fem konkrete ønskede resultater. |
| Success Criteria – kan kriteriene faktisk sjekkes eller testes? | OK | Målbare terskler mot et testsett. «Innen 20 sekunder» og brukertest-kriteriene krever at dere planlegger hvordan de måles. |
| Scope – er det klart hva som er med i første versjon, og hva som ikke er det? | OK | Tydelig og godt avgrenset. |
| Vision – henger visjonen sammen med resten uten å blåse opp omfanget? | Juster | Flere emner og kontrollspørsmål er greit som visjon. En betalt løsning med en kommersiell bok i kunnskapsbasen reiser spørsmål om opphavsrett; formuler det heller som en mulighet som krever avklaring. |

## 2. Utgangspunkt for del 1 av mappen

Punktene følger kriteriene i sensorveiledningen for del 1. Vektene i parentes viser hvor mye hvert kriterium teller i del 1.

| Kriterium i del 1 | Hva briefen bør legge til rette for | Status | Kommentar |
|---|---|---|---|
| **1. Prosess og KI-styring** (30 %) | Brief som er presis nok til at PRD og stories kan bygges direkte på den, slik at krav kan spores fra brief til kode. | Juster | Briefen er presis, og `PLAN.md` med testbare steg er et godt arbeidsdokument. Men BMAD-flyten (PRD, arkitektur, epics og stories) er hoppet over. Lag dem, gjerne med `PLAN.md` som grunnlag, og lagre prompts og KI-økter. Bruk også mer beskrivende commit-meldinger enn «push». |
| **2. Funksjonalitet og omfang** (20 %) | Realistisk omfang for gruppen og semesteret: en tydelig kjerneflyt som kan bli ferdig og stabil, og nok innhold til å vise reell funksjonalitet. | OK | Tydelig kjerneflyt og et realistisk omfang med nok innhold. |
| **3. Kvalitetssikring og testing** (15 %) | Suksesskriterier og funksjoner som er konkrete nok til å bli testtilfeller. | OK | Testsett, målbare terskler og en evalueringsscript i planen. Svært godt grunnlag. |
| **4. Design og brukeropplevelse** (10 %) | Tydelige brukere og brukssituasjoner som designet kan bygges rundt, gjerne med de viktigste skjermbildene eller flytene skissert. | Juster | Tydelig bruker og flyt. Streamlit gir et enkelt utgangspunkt; planlegg hvordan kilder, usikkerhet og fallback vises tydelig i grensesnittet. |
| **5. Kodekvalitet og arkitektur** (10 %) | Teknologivalg som er begrunnet og ikke mer komplekse enn appen trenger. | OK | Teknologivalgene i `PLAN.md` er begrunnet og enkle (lokal vektordatabase og lokale embeddings), med en tydelig modulstruktur. |
| **6. README og kjørbarhet** (10 %) | Løsning som andre kan kjøre lokalt uten betalte kontoer, og uten tilgang til gruppens egne tjenester og nøkler. | Juster | Alt kjører lokalt bortsett fra svarmodellen. Legg til demomodus og en tydelig README med oppsett av egen nøkkel. |
| **7. Ryddighet i repoet** (5 %) | En plan for hvor hemmeligheter, testdata og dokumentasjon skal ligge. | Juster | `.env.example` og en tydelig mappestruktur er på plass. Flytt briefen og planen til en egen dokumentasjonsmappe når PRD og arkitektur kommer, og avklar hvilket emnemateriale som kan ligge i `data/raw/` i et offentlig repo. |

## 3. Neste steg for gruppen

1. Lag PRD, arkitektur og stories med BMAD ut fra briefen og `PLAN.md`, slik at sporbarheten fra brief til kode blir tydelig.
2. Legg til en demomodus eller «kun kilder»-modus og beskriv i README hvordan sensor kjører appen med og uten egen nøkkel.
3. Velg kunnskapsbasen bevisst ut fra hva som kan publiseres, og lag testsettet før retrieval, slik planen sier.

Oppdater product brief i repoet når dere har gjort endringene, slik at historikken viser hvordan planen utviklet seg. Det er en del av prosessen sensor ser etter.
