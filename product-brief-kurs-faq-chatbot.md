# Product Brief: IBE160 Kursassistent

## Executive Summary

IBE160 Kursassistent er en KI-basert chatbot som hjelper studenter med å finne og forstå informasjon i emnet **IBE160 Programmering med KI**. I stedet for at studenten må lete i forelesningsnotater, oppgavebeskrivelser og andre emneressurser, kan studenten stille et spørsmål med egne ord og få et kort svar basert på en avgrenset kunnskapsbase.

Hvert svar skal så langt det er mulig vise hvilket materiale informasjonen er hentet fra. Studenten kan dermed kontrollere svaret og åpne kilden dersom det er behov for mer sammenheng eller fordypning. Dersom kunnskapsbasen ikke inneholder et godt nok svar, skal kursassistenten si dette tydelig og foreslå hvor studenten kan lete videre.

Første versjon utvikles bare for IBE160. Det gjør det mulig å begrense datamengden, teste kvaliteten systematisk og undersøke hvordan retrieval, språkmodeller og fallback-strategier kan kombineres i et praktisk KI-produkt. Produktet skal ikke erstatte undervisning eller faglig veiledning, men gjøre eksisterende emneinformasjon lettere å finne og bruke.

## The Problem

Studenter må forholde seg til mye informasjon gjennom et kurs, og det kan være tidkrevende å finne akkurat det de trenger. Generelle søkemotorer og AI-verktøy gir tilgang til enorme mengder informasjon, men mye av denne informasjonen er ikke relevant for IBE160. 
Dette kan være spesielt utfordrende for studenter som lærer programmering. De kan ha spørsmål om både kursinnhold og hvordan programmering fungerer, men kan få svært omfattende eller forskjellige svar avhengig av hvor de søker. 
Problemet er derfor ikke nødvendigvis mangel på informasjon, men å finne riktig og relevant informasjon på en enkel måte. 

Når en student har et konkret spørsmål om emnet IBE160 kan typiske situasjoner være:

- En student vil kontrollere hvilke krav som gjelder for en innlevering.
- En student husker at RAG ble gjennomgått, men ikke i hvilken ressurs.
- En student trenger en kort forklaring av et fagbegrep før arbeidet kan fortsette.
- En student vil finne materialet som er mest relevant for et bestemt tema.
- En student er usikker på om en opplysning fortsatt gjelder.

Studentene kan i dag lete manuelt, spørre medstudenter, kontakte faglærer eller bruke en generell chatbot. Manuelt søk tar tid, mens medstudenter ikke nødvendigvis kjenner det riktige svaret. En generell chatbot kan forklare fagbegreper, men har ikke automatisk tilgang til det konkrete innholdet og kravene i IBE160. Den kan derfor gi et generelt eller feilaktig svar med stor språklig sikkerhet.

Konsekvensen er unødvendig leting, usikkerhet og gjentatte spørsmål om informasjon som allerede finnes. Det sentrale problemet er dermed ikke bare tilgang til informasjon, men tilgang til **riktig informasjon i riktig sammenheng**.

## The Solution

IBE160 Kursassistent samler tilgangen til emneinformasjon i et enkelt chatgrensesnitt. Studenten skriver spørsmålet slik det naturlig formuleres, og løsningen finner relevant innhold i den godkjente kunnskapsbasen før svaret utformes.

Et svar skal bestå av:

- en kort og forståelig forklaring
- navn på kilden svaret bygger og kildelenke hvor studenten kan finne innholdet for å kontrolere informasjon.
- lenke eller henvisning til riktig emneressurs når dette er tilgjengelig
- en tydelig beskjed dersom svaret er usikkert eller ufullstendig

Et eksempel kan være:

> **Student:** Hvor kan jeg lese mer om bruk av API-er?
>
> **Kursassistent:** API-er omtales i forelesningsmaterialet om integrasjoner. Der finner du både en introduksjon og eksempler på hvordan et program kan sende og motta data.
>
> **Kilde:** Forelesningsnotat – API-er og integrasjoner.

Chatboten skal også kunne håndtere enkle oppfølgingsspørsmål, slik at studenten slipper å gjenta hele sammenhengen. Hvis spørsmålet er uklart, kan den be studenten presisere om spørsmålet gjelder for eksempel teori, prosjektarbeid eller praktisk emneinformasjon.

Dersom relevant dokumentasjon ikke finnes, skal chatboten ikke fylle inn manglende informasjon selv. Den skal forklare at den ikke finner et sikkert svar i emnematerialet og anbefale at studenten kontrollerer emnesiden eller spør faglærer. Den grunnleggende brukerreisen er:

**Spørsmål → emnespesifikt svar → synlig kilde → mulighet for videre lesing**

## What Makes This Different

IBE160 Kursassistent skal ikke konkurrere med generelle språkmodeller på hvor mange temaer den kan svare på. Styrken ligger i en smal og kontrollert oppgave: å hjelpe studenten med informasjon som faktisk finnes i IBE160.

Sammenlignet med vanlig dokumentsøk kan studenten bruke et naturlig spørsmål i stedet for å kjenne riktig filnavn eller nøyaktig begrep. Sammenlignet med en generell chatbot skal svaret være forankret i materialet faglærer har gjort tilgjengelig for emnet.

Løsningen prioriterer derfor:

- **etterprøvbarhet**, fordi studenten kan se kilden
- **avgrensning**, fordi svarene skal bygge på IBE160-materiale
- **åpenhet om usikkerhet**, fordi chatboten skal kunne avstå fra å svare
- **enkel tilgang**, fordi én samtale kan erstatte søk i flere dokumenter
- **testbarhet**, fordi svarene kan sammenlignes med et definert kildemateriale

Det tekniske konkurransefortrinnet er ikke en egen språkmodell. Forskjellen ligger i hvordan retrieval, kildebruk og fallback utformes og testes for ett konkret emne.

## Who This Serves

### Primærbrukere

Primærbrukerne er studenter som tar **IBE160 Programmering med KI**. De kan ha ulik teknisk erfaring, men har til felles at de trenger å finne fram i emneinnholdet mens de arbeider med øvinger eller prosjekt.

En typisk bruker ønsker ikke nødvendigvis et langt svar. Studenten vil raskt vite hva som gjelder, hvor informasjonen kommer fra og hvor det finnes mer materiale. For studenten betyr et vellykket produkt at mindre tid brukes på leting, samtidig som svaret oppleves som mer pålitelig enn et svar uten kilde.

### Sekundærbrukere

Faglærer og eventuelle undervisningsassistenter er sekundærbrukere. De kan få færre gjentatte spørsmål om frister, dokumentplassering og allerede publisert innhold. Spørsmål chatboten ikke klarer å besvare, kan også synliggjøre hvor emnematerialet bør presiseres eller suppleres.

### Ønsket resultat for brukeren

Etter en samtale skal studenten:

1. ha fått et relevant og forståelig svar
2. vite hvilket emnemateriale svaret er basert på
3. kunne åpne riktig ressurs for å lese videre
4. forstå når løsningen ikke har grunnlag for et sikkert svar
5. oppleve et forståelig og sikkert brukergrensesnitt

## Success Criteria

Produktet skal evalueres med et forhåndsdefinert testsett. Testsettet bør inneholde både spørsmål som kan besvares fra kunnskapsbasen, uklare spørsmål og spørsmål som ligger utenfor materialet.

### Svarkvalitet

- Minst **80 % av besvarbare testspørsmål** skal få et relevant svar som samsvarer med kildematerialet.
- Minst **90 % av kildehenvisningene** skal peke til riktig dokument eller ressurs.
- Ved spørsmål uten tilstrekkelig kildedekning skal chatboten unngå å presentere antakelser som fakta i minst **90 % av testtilfellene**.
- Svarene skal kunne spores tilbake til innhold som faktisk finnes i kunnskapsbasen.

### Brukeropplevelse

- Minst fire av fem testbrukere skal klare å finne fram til riktig emneinformasjon uten veiledning i hvordan dokumentene er organisert.
- Testbrukerne skal gi løsningen et gjennomsnitt på minst **4 av 5** på påstanden «Det var enkelt å finne informasjonen jeg trengte».
- Et standardsvar skal normalt vises innen 20 sekunder under testing.
- Brukerne skal oppfatte det som tydelig når svaret er usikkert eller kunnskapsbasen mangler informasjon.

### Prosjektets læringsresultat

Prosjektgruppen skal gjennom utvikling og testing kunne vise praktisk forståelse av:

- bruk av en språkmodell i en applikasjon
- oppbygging og klargjøring av en kunnskapsbase
- retrieval-strategi og valg av relevant kontekst
- kildehenvisninger i genererte svar
- håndtering av usikkerhet og spørsmål utenfor scope
- systematisk evaluering av et KI-basert produkt

## Scope

### IN – Første versjon

Første versjon skal omfatte:

1. **Ett emne**  
   Chatboten skal bare dekke IBE160 Programmering med KI.

2. **En kontrollert kunnskapsbase**  
   Gruppen velger ut og klargjør et begrenset sett med forelesningsnotater, oppgavebeskrivelser, emneinformasjon og andre godkjente ressurser.

3. **Spørsmål med naturlig språk**  
   Studenten skal kunne formulere spørsmål uten å kjenne dokumentnavn eller nøyaktige søkeord.

4. **Korte svar med kilde**  
   Løsningen skal gi et konsist svar og vise hvilket materiale som er brukt.

5. **Enkel samtalekontekst**  
   Chatboten skal kunne forstå relevante oppfølgingsspørsmål i samme samtale.

6. **Fallback ved manglende svar**  
   Løsningen skal være tydelig når den ikke finner tilstrekkelig informasjon, og vise brukeren til et egnet neste steg.

7. **Testing og enkel logging**  
   Spørsmål, treff og svar kan registreres uten unødvendige personopplysninger, slik at gruppen kan evaluere kvaliteten.

### OUT – Ikke i første versjon

Første versjon skal ikke:

- dekke andre emner eller hele studieprogrammet
- hente svar fritt fra internett
- fungere som en generell programmeringsassistent
- skrive komplette innleveringer eller eksamensbesvarelser
- vurdere studentarbeid, gi karakter eller avgjøre om en besvarelse er godkjent
- erstatte faglærer ved individuelle eller formelle spørsmål
- ha avansert personalisering, talegrensesnitt eller egen mobilapplikasjon
- være fullt integrert med skolens læringsplattform

Disse grensene skal gjøre første versjon mulig å gjennomføre, dokumentere og teste innenfor eksamensprosjektets tidsramme.

## Vision

Hvis IBE160 Kursassistent gir relevante og etterprøvbare svar, kan løsningen i løpet av to til tre år utvides i dybden til en betalt løsning med boken Agentic programming with Claude code i kunnskapsbasen. Eller at den utides utvides trinnvis til flere emner. Hvert emne kan ha en egen kvalitetssikret kunnskapsbase, mens studenten bruker ett felles grensesnitt.

En videreutviklet studieassistent kan forstå hvilket emne spørsmålet gjelder, søke på tvers av godkjente ressurser og tilpasse videre lesing til studentens behov. Den kan for eksempel foreslå relevante forelesningsnotater, lage korte kontrollspørsmål eller hjelpe studenten med å repetere et tema. Slike funksjoner bør først innføres når kvaliteten på informasjons søket er dokumentert.

Den langsiktige visjonen er en pålitelig inngang til studiehverdagen som hjelper studenten fra **å finne informasjon** til **å arbeide aktivt med den**. Løsningen skal fortsatt bygge på synlige kilder og tydelige grenser, slik at økt funksjonalitet ikke går på bekostning av tillit.
