
### The Python Solution

### Here is the code you would write using **BeautifulSoup** (to parse the HTML) and **Pandas** (to build the table). 

```python
from bs4 import BeautifulSoup
import pandas as pd

# 1. Load your raw HTML block (assigned to a variable for this example)
html_data = """

Meest relevant

Bright
@BrightNL•342K abonnees
Bright is vol van vernieuwing. Altijd op zoek naar het vernuft in technologie, design en style. Abonneer en zet de bel aan 🔔 dan mis je geen enkele video! Kijk ook op https://www.bright.nl voor al onze artikelen VOLG ons op Facebook https://www.facebook.com/bright.nl Instagram https://www.instagram.com/bright_nl Twitter https://www.twitter.com/bright TikTok https://bit.ly/tiktokbright LUISTER onze podcast: https://linktr.ee/brightnl

Geabonneerd

AVK Training & Coaching
@avktraining•1,39K abonnees
Maak je organisatie Digitaal Vitaal® met AVK - Een totaalaanpak bij slimmer werken! AVK Training & Coaching is dé partner die jouw organisatie van digitale chaos naar ‘Digitaal Vitaal’ brengt. Waar andere aanbieders alleen softwaretraining geven, zorgt AVK voor een totaalbegeleiding bij échte gedragsverandering, blijvende verbetering en up to date kennis. "Als AVK staan we iedere dag met veel energie voor het stimuleren, inspireren en motiveren, om het allerbeste uit jou als professional, jouw team en daardoor jouw organisatie te halen." Uit onze jarenlange ervaring hebben wij kunnen concluderen dat met extra begeleiding het werken op kantoor sneller, slimmer en leuker kan worden, met als gevolg dat de medewerkers meer werk verrichten in een kortere tijd en dit ook met veel meer plezier en toewijding doen. Meer informatie: www.avk.nl

Geabonneerd

aSquarednSquared
@AsquaredNsquared•28 abonnees
Subscribe. Puur voor educatieve doeleinden (Trust me, twin)

Geabonneerd

Michael Pilarczyk
@TheRealMisterMindset•106K abonnees
www.michaelpilarczyk.nl ----- Reacties kun je posten onder de video’s. Ik vind het leuk om iets van je te horen. ----- Michael Pilarczyk is auteur en spreker op het gebied van bewustzijn, zelfontwikkeling, zingeving, mentale gezondheid en persoonlijk succes. In de afgelopen jaren heeft hij meer dan honderdduizend mensen geholpen om meer plezier, rust, succes en geluk te ervaren in hun leven. Michael is samen met zijn vrouw Cindy oprichter van de Mastermind Academy en de Meditation Moments app. Duizenden mensen komen naar zijn events, de Meditation Moments app wordt door honderdduizenden mensen gebruikt en hij verkocht meer dan 500.000 boeken.

Geabonneerd

lioneducatie
@lioneducatie•14K abonnees
Welkom bij Lioneducatie! Wij zijn er voor iedereen die Nederlands wil leren, ongeacht je niveau. Of je nu net begint met het leren van de taal of je vaardigheden wilt verbeteren, wij staan voor je klaar! Bij Lioneducatie bieden we: NT2-onderwijs: Speciaal voor mensen die Nederlands als tweede taal leren. VMBO-onderwijs: Toegankelijke lessen voor scholieren en volwassenen. Elke week plaatsen we een nieuwe les op ons kanaal, zodat je op een leuke en effectieve manier je Nederlands kunt verbeteren. Onze lessen zijn helder, praktisch en geschikt voor alle leeftijden. Heb jij een onderwerp waar je meer over wilt leren? Laat het ons weten in de reacties! We luisteren graag naar jouw ideeën en passen onze lessen aan op jouw behoeften. Blijf verbonden met Lioneducatie Website: https://www.lioneducatie.nl/ Instagram: https://www.instagram.com/lioneducatie.nl/ #NederlandsLeren #NT2 #DutchLessons #DutchForBeginners #NederlandsA1 #NederlandsA2 #NederlandsB1 #NederlandsB2

Geabonneerd

Luisterverhalen
@Luisterverhalen-ZoC•1,36K abonnees
Verhalen voor volwassenen om te beluisteren. De verhalen hebben verschillende onderwerpen. Zo is er een playlist met verhalen over gezondheid, natuur, hobby en gezelligheid. De verhalen worden voorgelezen zodat ze ook geschikt zijn voor mensen met een visuele beperking.

Geabonneerd

Cartoon Network Nederland
@CartoonNetworkBEN•244K abonnees
Welkom op het officiële Cartoon Network Benelux YouTube-kanaal, de plek waar je grappige video’s kunt bekijken en clips met titelsongs, liedjes en interactieve gameplay uit De Wonderlijke Wereld van Gumball, Craig van de Kreek, Teen Titans Go!, Wat Beren Leren, Wat babyberen leren, Ben 10, Tijd voor Avontuur, Clarence, Regular Show, Steven Universe en nog veel meer. Er valt veel te lachen, dus schrijf je in op het kanaal om iedere week nieuwe video’s te ontdekken. In Nederland en Vlaanderen kun je Cartoon Network ontvangen op de volgende zendernummers: KPN 19, Ziggo 307, UPC 501, Telenet 600, Proximus 131, Canal Digitaal 43, Delta 250, Caiway 122, Glashart 190, TV Vlaanderen 41, Numericable 141 en Tele2. Je kunt alle series en films van Cartoon Network ook vinden op HBO Max: https://geoip.turner-apps.com/hbomax Schermlezers worden ondersteund.

Geabonneerd

Luke Barousse
@LukeBarousse•625K abonnees
What's up, Data Nerds! I'm Luke, a data analyst who loves making tutorials. ❓ If you have a question, drop a comment in any video. 📩 Email is for business inquiries only, please.

Geabonneerd

History Hustle Nederlands
@HistoryHustleNederlands•62,7K abonnees
Op dit Nederlandstalige kanaal vind je video's over geschiedenis.

Geabonneerd

Jeff
@Jeffslootz•479 abonnees
Ik deel momenten uit mijn leven die waardevol voor je kunnen zijn of gewoon leuk en inspirerend 💫 Daarnaast ben ik een groot dier en natuurliefhebber en zet ik me hiervoor in 🐸 🦎🦆 Enjoy de video’s en abonneren is liefde!🙏🏼 Good vibez only 💫 Love, Jeff

Geabonneerd

Trimbos-instituut
@trimbos-instituut•1,4K abonnees
Het Trimbos-instituut zet zich met kennis en innovatie actief in voor het verbeteren van de mentale gezondheid in Nederland en daarbuiten.

Geabonneerd

NOS op 3
@nosop3•594K abonnees
NOS op 3 geeft uitleg bij het nieuws, in duidelijke taal. Doen we hier op YouTube, maar ook op Insta, TikTok en in de podcast Lang verhaal kort. Abonneer je op ons kanaal en praat mee in de comments. Heb je vragen, stel ze vooral in de comments. En als je een onderwerp hebt waar wij in jouw ogen écht een video over moeten maken, deel die dan! Vinden we leuk. Hou je dan wel even hieraan: 1) Blijf beschaafd en respectvol 2) Speel niet onnodig op de man 3) Reageer inhoudelijk, off-topic reacties verwijderen we 4) Zelfpromotie of spam halen we ook weg.

Geabonneerd

Zichtbaar in werk
@zichtbaarinwerk9800•26 abonnees
Zichtbaar in Werk is hét landelijke informatie- en adviespunt voor iedereen die betrokken is bij werken met een visuele beperking. Als informatie- en adviespunt zijn we vraagbaak in brede zin, zolang het specifiek gaat over werken met een visuele beperking. Informatie over werk zoeken en werken met een visuele beperking maken we centraal toegankelijk: op één plek, eenduidig en deskundig. Onze doelgroepen: 1 Mensen met een visuele beperking die werk zoeken of werk hebben en zoeken naar mogelijkheden om werk te behouden 2. (Potentiële) werkgevers 3. Arbeidsbemiddelaars en -begeleiders vanuit gemeentes, UWV, opleidingen, re-integratieorganisaties en arbodiensten

Geabonneerd

Ik leer Nederlands_S B
@ikleernederlands_seydobasmaci•29,6K abonnees
NEDERLANDS LEREN - LEARN DUTCH! Vergeet zeker niet te abonneren! SUBSCRIBE IF YOU LIKE !. لا تنس الاشتراك! • 🚀 Snel en leuk Nederlands leren? Je bent hier op de juiste plek! #nederlands #nederlandsleren #learndutch #dutch #ภาษาดัตช์ #荷兰语 #荷蘭文 #нидерландский #オランダ語 #เรียนภาษาดัตช์ #hollandaca #네덜란드어를 #holandés #Ολλανδικά #هلندی #ডাচ #холандски #荷兰语 #siamani #ලන්දේසි #holandčina #டச்சு #ڈچ #האלענדיש #ჰოლანდიური #डच #네덜란드 사람 #հոլանդերեն #holenderski #डच #olandeză #ලන්දේසි #டச்சு #ภาษาดัตช์ #డచ్ #ሆላንዳዊ #xidachini #holandi #האלענדיש #ჰოლანდიური #डच #네덜란드 사람 #english #ziman #viralvideo #shorts #video #هلندی nederlands leren,oefenen nl, dutch with kim,learn dutch with bart, jufmnt2,learn dutch academy, learn dutch advanced,learn dutch alphabet,learn dutch a1,learn dutch audio,learn dutch at home,learn dutch bart de pau,learn dutch b1,learn dutch belgium,learn dutch bart,learn dutch beginner,learn dutch with dutchpod101,learn dutch easy,learn dutch grammar bart de pau,

Geabonneerd

Universiteit van Nederland
@UniversiteitvanNL•287K abonnees
Wij zetten de nieuwsgierigheid van heel Nederland aan. Hier delen de beste wetenschappers van Nederland gratis hun kennis met jou. De Universiteit van Nederland is een stichting met als missie om wetenschap toegankelijk te maken voor iedereen. We werken samen de Nederlandse universiteiten en samen zorgen we ervoor dat je wekelijks gratis kunt leren van de beste docenten van het land. Tips en feedback zijn welkom! Al onze video's vallen onder de Creative Commons-licentie (CC BY). Deel onze colleges dus zo veel als je wil (door ze te embedden via YouTube), maar vergeet onze naam zeker niet te vermelden.

Geabonneerd

Learnit Training
@LearnitTrainingNL•4,3K abonnees
Welkom bij Learnit, dé specialist in maatwerktrainingen door heel Nederland. Met meer dan 300 trainingen, afgestemd op de unieke leerdoelen van deelnemers, zorgen onze hoogopgeleide trainers voor optimale resultaten. We trainen op locaties door het hele land en bieden ook 'incompany trainingen' aan. Abonneer je op ons YouTube-kanaal voor regelmatige updates en leerzame content!

Geabonneerd

True Sage
@TrueSageJourney•39,1K abonnees
trying to understand myself—and the world around me, a bit better, one idea at a time. Support the channel: https://ko-fi.com/truesage Join my Patreon: https://patreon.com/TrueSage?utm_medium=unknown&utm_source=join_link&utm_campaign=creatorshare_creator&utm_content=copyLink

Geabonneerd

ThinkingWest
@ThinkingWest•73,2K abonnees
Reviving the Great Conversation in the Digital Age. We talk about the Great Books, ideas that built that West, and ask the big questions. Hosted by Christian and Adam of Thinkingwest.com. Visit the website at: https://thinkingwest.com/ SUBSCRIBE to keep in touch.

Geabonneerd

Oefenen.nl
@Oefenennlwelerenaltijd•57,7K abonnees
Welkom op het YouTube kanaal van Oefenen.nl. Wil je op de hoogte blijven van onze video's? Abonneer je dan op ons kanaal. Je ontvangt video's over taal, rekenen, internetten en omgaan met geld. Of over werk, gezondheid en opvoeding. En over mensen die oefenen met onze programma's. Oefenen.nl is dé plek waar je je basiskennis en vaardigheden kunt verbeteren. Ga naar www.oefenen.nl

Geabonneerd

Nederlands Debat Instituut
@debatinstituut•4,91K abonnees
Het Nederlands Debat Instituut streeft naar de verdere ontwikkeling van de debatcultuur in Nederland. * Wij verzorgen jaarlijks meer dan driehonderd trainingen op het gebied van mondelinge overtuigingskracht. * Daarnaast leveren wij meer dan tweehonderd keer per jaar dagvoorzitters en gespreksleiders voor congressen en andere bijeenkomsten. * Op dit kanaal vindt u onze showreels, overtuig-, vergader- en evenementen-tips, speeches en registraties van waar we actief waren. * Vind je onze videos interessant en wil je regelmatig vergader- en overtuigtips ontvangen? Abonneer je dan op ons kanaal

Geabonneerd

Kahan Data Solutions
@KahanDataSolutions•57,6K abonnees
Helping small data teams build reliable, modern data architectures.

Geabonneerd

Techgrounds
@Techgrounds_NL•1,58K abonnees
IT'er worden? Maar wat dan? Ontdek jouw mogelijkheden in de IT-wereld! En het leukste? Stichting Techgrounds is bijna altijd gratis voor deelnemers!

Geabonneerd

BİZ BİZE HOLLANDACA
@bizbizehollandaca•2,85K abonnees

Geabonneerd

Meditation Moments
@MeditationMomentsApp•133K abonnees
Meditation Moments is dé Nederlandse meditatie-app voor meer rust in je hoofd. Download de Meditation Moments app via de App Store of Google Play Store.

Geabonneerd

Goesting in Taal
@goestingintaal•2,91K abonnees
LEER VLAAMS MET SOFIE ✨De place to be om meer te leren over informeel Belgisch Nederlands✨ 👉 Voel je EINDELIJK op je gemak in informele conversaties met native speakers!

Geabonneerd

SerpentScience
@SerpentScience•8,53K abonnees
Contact: Serpentscience@gmail.com

Geabonneerd

Leermij
@leermij•892 abonnees
Leermij.com heeft als doel om jou met meer zelfvertrouwen video's te laten produceren, die jouw business laten groeien. We leren je met kracht presenteren en strategische video's te produceren, zonder alle overbodige technische blabla. Snel, efficiënt en luchtig

Geabonneerd

LibriVox Audiobooks
@LibriVoxAudiobooks•267K abonnees
Welcome to the Official LibriVox YouTube Channel! 🎧📚 Explore one of the best libraries of complete audiobooks on YouTube, featuring works that are now in the public domain, free for everyone to enjoy. Our Mission LibriVox is dedicated to making all public domain books available for free in audio format on the internet. Learn more about our mission at LibriVox's About Page. Channel Highlights Chapter Selection: Each audiobook includes chapter links in the video description to make resuming easy and enjoyable. Playlists by Author & Genre: Discover our carefully categorized playlists for easy browsing by author or genre. Subscribe to stay updated when new audiobooks are released! Support Us LibriVox audiobooks are created and made available through the support of our volunteers and donors. Visit LibriVox for more, or consider donating at LibriVox Donations to help us continue sharing free, public domain audiobooks with the world. Enjoy your listening adventure with LibriVox! 🎙️📖

Geabonneerd

A Day In History
@ADayInHistoryOfficial•849K abonnees
A Day In History brings to you the unsaid, weird, and ugly parts of history that are not taught in textbooks, along with some more hopeful sections of our past. With so much misinformation everywhere, our aim is to shed light on some of history's most suppressed but factual events.

Geabonneerd

De Militaire Show
@TheMilitaryShow_nl•5,39K abonnees
Welkom op het officiële kanaal van @TheMilitaryShow in het Nederlands! Wij brengen je dagelijks de laatste updates over het Amerikaanse leger en wereldwijd defensienieuws. Ontdek diepgaande analyses van moderne oorlogsvoering, nieuwe technologieën en strategische operaties. Abonneer je op het kanaal, like onze video's en deel ze met anderen. Vergeet niet de meldingen in te schakelen zodat je nooit een update van de frontlinie mist. Jouw steun helpt ons om hoogwaardige militaire content te blijven leveren. Dit kanaal is gelokaliseerd, gedubd en gemonetiseerd door Linguana. Ontdek een kosteloze, risicovrije manier om meer kijkers te bereiken en je omzet te vergroten: www.linguana.com Sponsoraanvragen voor dit en onze andere kanalen: advertising@linguana.com

Geabonneerd

Benjamin | Crypto Universiteit
@CryptoUniversiteit•9,68K abonnees
Als Crypto Trader heb ik jaren verloren door support/resistance, indicators en andere onzin. Ik leerde ik hoe de markt écht beweegt. Op m'n kanaal leg ik je uit hoe! #Crypto #Bitcoin #Altcoins #Investeren #Beleggen #Nederland

Geabonneerd

Universiteit van Vlaanderen
@UniversiteitvanVlaanderen•64,2K abonnees
Bij de Universiteit van Vlaanderen delen wetenschappers de meest spannende wetenschappelijke inzichten en ontdekkingen. Elke donderdag een nieuwe podcast, elke zondag een nieuwe video! Check zeker ook www.universiteitvanvlaanderen.be Veel kijk- en luisterplezier!

Geabonneerd

Nederlands op kantoor - Learn Dutch at work
@nederlandsopkantoor•4,32K abonnees
💪BOOST je Nederlands op kantoor en maak indruk op je collega´s! 🤓Hier leer je nuttige woordenschat die je op het werk kan gebruiken. Ik geef je praktische voorbeeldzinnen voor diverse gesprekssituaties in vergaderingen, workshops, presentaties, ... 🤓doelgroep: professionals met een intermediair niveau (minimum B1+) 🧑‍🏫over mij: Al meer dan 10 jaar geef ik les aan medewerkers uit verschillende bedrijven (banken, verzekering, IT, administratie, HR, ...) Daarnaast werk ik deeltijds als opleidingsverantwoordelijke bij een grote multinational. Mijn eigen bedrijfservaring is een meerwaarde tijdens mijn lessen. 👉Ik beheer een oefenplatform met 2 modules: 1 voor grammatica en 1 voor zakelijke woordenschat. Je vindt er meer dan 270 oefeningen die ik geschreven heb. Het is een e-learning de luxe: niet alleen krijg je bij elke oefening de oplossing, je hebt ook de mogelijkheid om me vragen te stellen! 👉link oefenplatform: https://www.buymeacoffee.com/businessdutch/membership

Geabonneerd

thefallenpoet
@FallenPoet•21,6K abonnees
My Poetry Book ⤵️ Poet & Artist🎨 "𝑶𝒏𝒆 𝑴𝒖𝒔𝒕 𝑭𝒂𝒍𝒍, 𝑰𝒏 𝑶𝒓𝒅𝒆𝒓 𝑻𝒐 𝑹𝒊𝒔𝒆" 400k Souls on Instagram, 100k Souls On Tiktok. Subscribe If You Enjoy My Poetry :)

Geabonneerd

Terra X History
@TerraXHistory•1,38 mln. abonnees
Bei TERRA X History bekommt Ihr jeden Sonntag spannende Videos zu den Themen Geschichte, Archäologie, und Zeitgeschichte – natürlich werbefrei und kostenlos. Produziert wird der Kanal vom ZDF in Zusammenarbeit mit objektiv media. Neue Dokumentationen von Terra X gibt es immer sonntags um 19:30 Uhr im ZDF oder mittwochs in der ZDF-Mediathek unter terra-x.de. Das Kanal-Team diskutiert gerne mit Euch in den Kommentaren und beantwortet Eure Fragen. Auch über Feedback freuen wir uns. Wenn ihr Euch direkt an die Redaktion wenden möchtet, schickt uns bitte eine Mail an die unten angegebene Adresse. Um für alle eine gute Diskussionsatmosphäre zu schaffen, gilt auf unserem Kanal eine Netiquette. Diese findet Ihr hier: https://kurz.zdf.de/TXNettiq/ Gerne können unsere Videos auf Webseiten eingebettet werden, wenn dort auf Terra X verwiesen wird.

Geabonneerd

Dai Carter: Missie Mentale Kracht
@DaiCarterPodcast•4,02K abonnees
Wil jij mentaal sterker worden en meer uit jezelf halen? 💪 In Missie Mentale Kracht gaat Dai Carter – voormalig Special Forces-operator en bekend van Kamp van Koningsbrugge – elke week in gesprek met topsporters, wetenschappers en inspirerende denkers over mentale weerbaarheid, discipline en persoonlijke groei. Of je nu beter wilt presteren in sport, werk of het dagelijks leven: hier vind je praktische tools, inspirerende verhalen en mentale strategieën om jouw mindset te versterken. 🧠 Leer omgaan met druk, falen en tegenslag. 💥 Ontdek wat mentale kracht écht betekent. 💬 En train jouw veerkracht – stap voor stap. 👉 Abonneer je op Missie Mentale Kracht en bouw mee aan een sterker hoofd én lichaam. 📲 Volg ook de community op Instagram & TikTok: @daicarter.podcast

Geabonneerd

Consumentenbond
@consumentenbond•59,3K abonnees
Welkom bij de Consumentenbond op YouTube! Hier vind je handige tips, eerlijke reviews en onafhankelijk advies, zodat jij de beste keuze kunt maken. Abonneer je en mis geen enkele video! Heb je een vraag of wil je advies? Laat een reactie achter onder onze video’s. We lezen mee en helpen je graag verder! Meer weten? Ga naar consumentenbond.nl

Geabonneerd

International Poetry Forum
@InternationalPoetryForum•2,61K abonnees
The International Poetry Forum is a historic reading series founded in Pittsburgh, PA, in 1966. A 501(c)(3) nonprofit organization, the International Poetry Forum has hosted readings and educational programs by 800+ performers from 50+ countries, including one Princess, one Queen, nine Nobel Laureates, 14 Academy Award recipients, 28 U.S. Poets Laureate, and 40+ Pulitzer Prize winners. Alumni include greats like Seamus Heaney, Gwendolyn Brooks, Mary Oliver, Tennessee Williams, Jorge Luis Borges, W.H. Auden, Kurt Vonnegut, Chinua Achebe, Derek Walcott, Lawrence Ferlinghetti, Terrance Hayes, Naomi Shihab Nye, Emily Wilson, Joyce Carol Oates, Billy Collins, James Earl Jones, Gregory Peck, Anthony Hopkins, Danny Glover, Lucille Clifton, The Clancy Brothers, Judy Collins, Brooke Shields, Princess Grace of Monaco, and Queen Noor of Jordan.

Geabonneerd

Vrije Universiteit Brussel
@VUBrussel•5,8K abonnees
Live and learn with us at the greenest university in Europe's capital city. Check www.vub.be. #WeAreVUB #DeWereldHeeftJeNodig

Geabonneerd

Samuel Wagar
@samuelwagar•3,88K abonnees

Geabonneerd

Betweters
@Betweterspodcast•4,18K abonnees
Abonneer als je leergierig of ambitieus bent :) Ons doel is eenvoudig: leren. We willen zoveel mogelijk kennis en inzicht opdoen door in de gedachten van anderen te duiken. Verwacht elke maandag een nieuwe aflevering!

Geabonneerd

mehdio debugs
@mehdio•5,9K abonnees
I’m a data geek who’s passionate about Big data, Data Science, Web App, and Music. With more than 7 years of experience in the data domain, this channel is a place where I share what I learned from my journey so far. I'll hope you find it interesting and... fun. Because learning should be fun! See you in the comments!

Geabonneerd

Jochum van Weert
@WtInformatica•335 abonnees
Jochum van Weert (Wt) is informaticadocent op het Stedelijk Gymnasium van 's-Hertogenbosch (https://informatica.sgdb.nl) Wt maakt instructievideos die aansluiten bij opdrachten en onderwerpen uit de informaticalessen (VWO). Soms zijn filmpjes onderdeel van een opdracht, maar vaak zijn het algemene lessen en extra uitleg over informatica onderwerpen. Deze zijn niet alleen nuttig voor leerlingen, maar voor iedereen die meer over Informatica wil weten. Wt houdt van Python, hardrock en appeltaart. Zijn ultieme doel is om de wereld informatica te leren vanuit een hangmat. Dit Youtube kanaal is onderdeel van dat meesterplan.

Geabonneerd

Basis Programmeren
@basisprogrammeren•5 abonnees

Geabonneerd

Nederlands leren
@NederlandslerenZoC•23,8K abonnees
Korte video's waarin op eenvoudige wijze de basis van de Nederlandse taal wordt geleerd. Iedere video is een aparte les, je kunt deze in je eigen tempo online bekijken. De video's zijn bedoeld voor anderstaligen. Mensen die Nederlands als 2e taal leren. Door de video's te bekijken kun je Nederlands leren lezen, schrijven, spreken en verstaan.

Geabonneerd

Learn German with Lengura
@lengura•103K abonnees
You finally found the right place to learn and understand German 🎓💡. Welcome to Lengura! Henry and the Lengura team will make learning German super easy for you ✨! We have developed a unique and innovative teaching method so that you can finally understand the German grammar, improve your vocabulary and speak better in your next conversation. Subscribe to the channel and turn on notifications! This way you will never miss any of our new and valuable videos. You want to learn perfect German? We have helped thousands of students to accomplish this goal. In our highly effective online German course we will teach you all the necessary grammar with easy and structured explanations and then show you in specifically prepared dialogues how you can correctly use it in your next conversation. You will be able to put the theory into practice and speak German correctly! Check out all the information under the following link and start improving your German right now ✅: https://lengura.de

Geabonneerd

Programmieren lernen
@Programmierenlernen•296K abonnees
Du interessierst dich für eine Weiterbildung zum Programmierer? Dann bist du auf diesem Kanal genau richtig! Mit unseren maßgeschneiderten Coachings bilden wir dich zu einem gefragten und gut bezahlten Programmierer weiter, der mühelos einen Job findet. Du willst Programmierer werden? Informiere dich auf: developerakademie.com Impressum: Developer Akademie GmbH Tassiloplatz 25 81541 München HRB 269921, AG München Geschäftsführung: Manuel Thaler, Junus Ergin E-Mail: info@developerakademie.com USt-Idnr: DE348348674 Zugelassener Träger nach dem Recht der Arbeitsförderung. Zugelassen durch die fachkundige Stelle der TÜV Rheinland Cert GmbH – von der Deutschen Akkreditierungsstelle (DAkkS) akkreditierte Zertifizierungsstelle (Zertifikatsnummer: 01 600 2000730 https://www.certipedia.com/certificates/01+600+2000730)

Geabonneerd

BEYONDER | Deutschland
@beyonder_de•379 abonnees
Wir sind BEYONDER. Wir bauen Software für komplexe Prozesse – sicher, individuell und skalierbar. Auf diesem Kanal teilen wir echte Einblicke in Software-Projekte, Automation, KI-Einsatz und die Realität hinter Digitalisierungsversprechen. Für Entscheider, die Standardsoftware hinterfragen. 👉 https://beyonder.eu/de

Geabonneerd

The Morpheus Tutorials
@TheMorpheusTutorials•271K abonnees
Ein Kanal rund um das Thema Informatik und Programmieren mit über 2000 Videos! Ob Python, Java oder Webdev oder doch Hacken und theoretische Informatik - es ist alles da! Für Wünsche bin ich jederzeit offen, also schreibt einfach Kommentare bzw besucht meine Academy: https://bootstrap.academy/ Zu mir: Ich, Cedric oder Morpheus (sucht's euch aus) habe einen Master in allgemeiner Informatik mit Schwerpunkten Machine Learning und IT-Sicherheit und bilde mich in meiner Freizeit ständig weiter, daher auch nicht ganz unwissend in all den Informatik-Themen. Impressum: Cedric Mössner c/o RA Matutis Berliner Straße 57 14467 Potsdam Für Kooperationen, Auftritte und Co: morpheus@espmedia.de Für alles andere: kontakt@the-morpheus.de (bitte KEINE sensiblen Daten teilen!) Telefon: +49 7631 9759 803 Verantwortlich für redaktionelle Inhalte Cedric Mössner Umsatzsteuer-Identifikationsnummer DE327206699 Datenschutz/Privacy: https://the-morpheus.de/privacy_socialmedia.html

Geabonneerd

Sprich mit! – Shadowing Deutsch
@ShadowingDeutsch•19K abonnees
Trainiere dein Sprechen mit echten Shadowing-Übungen. Hör zu, sprich mit – laut, klar und ohne Angst. Jeden Tag ein bisschen. Ohne Grammatikstress. Shadowing auf Deutsch für alle, die endlich sprechen wollen.

Geabonneerd

Niederländisch mit Ziko van Dijk
@ZikovanDijk•8,65K abonnees
Dit is het kanaal van Dr. Ziko van Dijk. Hier praat ik over Nederland in het Duits en over Duitsland in het Nederlands, over taal, land en volk. Ik ben een Duitser die al heel lang in Nederland woont.

Geabonneerd

Ruhe der Zeit
@RuheDerZeit•19,2K abonnees
Hi. Ich bin Tommy. Ich liebe Geschichten, die uns zum Nachdenken bringen. Geschichten über das, was war, und was wir daraus heute noch lernen können. Hier nehme ich dich mit auf eine nächtliche Zeitreise: 📜 Historische Ereignisse 🌍 Vergessene Kulturen 🧠 Menschliche Abgründe & kleine Weisheiten 🎧 Perfekt zum Einschlafen, Abschalten oder Träumen. Wenn du magst, begleite mich. Abonniere den Kanal und finde deine Ruhe in der Zeit.

Geabonneerd

Caleb Curry
@codebreakthrough•727K abonnees
Programming Made Fun and Simple High quality tutorials that are fun, educational, and easy to follow. Teaching programming is my passion! I find joy in making complex material easy to understand. I've decided that it is only right to upload videos of great quality and value. Here you will find videos on C++, JavaScript, C, database design, SQL, and more! As a side note, many videos contain cringey and random stories...you've been warned. As an Amazon Associate I earn from qualifying purchases. Business inquiries: hello@calebcurry.com

Geabonneerd

De Perfecte Podcast
@DePerfectePodcast•248 abonnees
De Perfecte Podcast is een reeks gesprekken en interviews met makers, kenners en liefhebbers van de beste strip van het Westelijk halfrond: Suske en Wiske. Je hoort achtergrondverhalen vanuit Studio Vandersteen en achtergrondverhalen bij de avonturen die Willy Vandersteen, Paul Geerts, Marc Verhaegen en Luc Morjaeu en Peter van Gucht onze helden lieten beleven. En daarbij vind je op dit YouTube kanaal video's en beeldmateriaal rondom de podcast zelf. Voor meer informatie kan je terecht op www.deperfectepodcast.nl

Geabonneerd


"""

# 2. Initialize BeautifulSoup to parse the HTML tree
soup = BeautifulSoup(html_data, 'html.parser')

# This list will hold our parsed records before we make a table
parsed_records = []

# 3. Find every main row in the table
# Looking at the HTML, each day is wrapped in a <tr> with this specific class
daily_rows = soup.find_all('tr', class_='travel-history-table__row')

for row in daily_rows:
    # --- A. Extract the Date ---
    date_cell = row.find('td', class_='travel-history-table__scan-event-date')
    date_text = date_cell.text.strip() if date_cell else None
    
    # --- B. Extract the Events for that Date ---
    # One date can have multiple events (like Arriving, then Departing).
    # We find all event blocks within the current row.
    events = row.find_all('div', class_='travel-history__scan-event')
    
    for event in events:
        # Extract Time (It's typically the first simple <span> in the event block)
        time_text = event.find('span').text.strip() if event.find('span') else None
        
        # Extract Status (Conveniently, FedEx tagged this with id="status")
        status_element = event.find('span', id='status')
        status_text = status_element.text.strip() if status_element else None
        
        # Extract Location (It's stored in the last div with regular font weight)
        location_divs = event.find_all('div', class_='fdx-u-fontweight--regular')
        location_text = location_divs[-1].text.strip() if location_divs else None
        
        # Append the clean dictionary to our list
        parsed_records.append({
            'Raw_Date': date_text,
            'Time': time_text,
            'Status': status_text,
            'Location': location_text
        })

# 4. Transform into a Table using Pandas
df = pd.DataFrame(parsed_records)

# 5. Clean up the Data Types (Crucial for Data Engineering!)
# Remove the day of the week (e.g., "Saturday, ") to easily parse the date
df['Clean_Date'] = df['Raw_Date'].str.split(', ').str[-1]

# Combine Date and Time into a single, highly queryable Datetime object
df['Timestamp'] = pd.to_datetime(df['Clean_Date'] + ' ' + df['Time'])

# Drop the old messy columns and reorder for a clean final table
final_table = df[['Timestamp', 'Status', 'Location']]

print(final_table)
```
