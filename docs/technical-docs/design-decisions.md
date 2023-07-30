---
title: Design Decisions
parent: Technical Docs
nav_order: 5
---

Isabel Kaspar
{: .label }

# Design decisions
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## 01: Aufgaben und Unteraufgaben

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 28-07-2023

### Problem statement

Die zentrale Herausforderung liegt in der Schaffung einer effektiven Aufgabenverwaltungsstruktur, die es den Benutzern ermöglicht, verschiedene Aufgaben anzuzeigen und erfolgreich abzuschließen. Einige Aufgaben können mehrere Subtasks haben, was die Notwendigkeit einer klaren und gut organisierten Aufgabenstruktur betont.

### Decision

Durch die erfolgreiche Umsetzung einer strukturierten Aufgaben- und Unteraufgabenverwaltung auf verschiedenen Seiten unserer Anwendung erhalten Benutzer die Möglichkeit, ihre Bewerbungsunterlagen effizient zu organisieren, ohne dabei den Überblick zu verlieren. Die Aufteilung und Auslagerung von Unteraufgaben in separate Seiten, die verschiedenen Aufgabenkategorien wie "Persönliche Daten", "Akademische Ressourcen" und "Finanzielle Ressourcen" zugeordnet sind, verbessert die Übersichtlichkeit und ermöglicht es den Benutzern, sich auf spezifische Aufgabenbereiche zu konzentrieren. Diese gezielte Einteilung der Aufgaben unterstützt die Benutzer dabei, ihre Bewerbungsprozesse effektiv zu verwalten. Die Entscheidung für diese Struktur wurde in der Entwurfsphase von beiden Teammitgliedern gemeinsam getroffen.

### Regarded options

Eine gemeinsame Ansicht, anstatt die Aufgaben in verschiedene Kategorien zu unterteilen und sie auf einer separaten Seite anzuzeigen. Man könnte für die Webanwendung eine flache Aufgabenliste verwenden, in der alle Aufgaben gleichwertig nebeneinanderstehen. Das hat den Vorteil, dass auch direkt alle relevanten Tasks sichtbar sind und man nicht noch extra auf eine andere Seite navigieren muss.

Wie bei dem Punkt der Übersichtlichkeit kamen wir zu dem Schluss, dass wir den Nutzer nicht verlieren wollen, weil zu viele Tasks auf einmal zu bearbeiten sind. 

## 02: Aufteilung in zwei Parts – Übersichtlichkeit

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 28-07-2023

### Problem statement

Eine einzige Seite mit vielen Tasks kann die Benutzererfahrung beeinträchtigen, da die Benutzer möglicherweise mit zu vielen Informationen überfordert sind und es schwierig sein kann, bestimmte Tasks schnell zu finden und zu bearbeiten.

### Decision

Um die Übersichtlichkeit zu erhöhen und die Benutzererfahrung zu verbessern, wurde die Webanwendung in zwei Parts aufgeteilt. In "Part 1" befinden sich die Tasks, die für den frühen Bewerbungsprozess relevant sind, und in "Part 2" werden die Tasks angezeigt, die für den späteren Verlauf des Bewerbungsprozesses zu erledigen sind. Diese Aufteilung ermöglicht es Benutzern, sich gezielt auf die jeweiligen Phasen des Bewerbungsprozesses zu konzentrieren und erleichtert die effiziente Verwaltung ihrer Tasks. Dadurch wird die Nutzererfahrung verbessert und die Anwendung wird benutzerfreundlicher gestaltet. Diese Entscheidung wurde in der Entwurf-Phase von beiden Teammitgliedern gemeinsam getroffen.

### Regarded options

Die Option, alles auf einer Seite zu haben, wäre mit einer Tabelle denkbar gewesen. 
Tabellenansicht: Statt die Tasks in zwei Parts aufzuteilen, könnte die Webanwendung eine Tabellenansicht verwenden, um die Tasks übersichtlich darzustellen. Benutzer könnten die Tabellenansicht nach ihren Bedürfnissen anpassen und die Anzeigeoptionen auswählen, um nur relevante Informationen anzuzeigen.
Allerdings überwiegt das übergeordnete Ziel der Übersichtlichkeit und der Reduzierung von Gefühlen der Überforderung und von Stress. Der Nutzer soll nicht von Informationen und Aufgaben „erschlagen“ werden. 

## 03: Blueprints

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 28-07-2023

### Problem statement

Die Herausforderung bestand darin, eine geeignete Struktur für die Flask-Anwendung zu schaffen, um eine klare Trennung von verschiedenen Funktionalitäten zu ermöglichen. Es musste eine Methode gefunden werden, um Routen und Views zu organisieren, die es ermöglichen, verschiedene Teile der Anwendung in getrennten Modulen zu halten.

### Decision

Blueprints wurden gewählt, um eine saubere Strukturierung der Flask-Anwendung zu ermöglichen. Die Verwendung von Blueprints erleichtert die Organisation der verschiedenen Routen und Views in separate Module, wodurch der Code besser strukturiert werden kann. Diese Entscheidung, mit Blueprints zu arbeiten, wurde von uns getroffen, als wir uns Code-Beispiele von zum Beispiel TechWithTim (2023, 29. Januar) angeschaut haben.

### Quellen

Davison, B. (o. D.). Web Development – Blueprints. https://bdavison.napier.ac.uk/web/flask/basics/blueprints/ (zuletzt geprüft: 28.07.2023).

TechWithTim (2023, 29. Januar). Flask-Web-App-Tutorial. GitHub. https://github.com/techwithtim/Flask-Web-App-Tutorial (zuletzt geprüft am 28.07.2023). 


## 04: Datenbankanbindung

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 28-07-2023

### Problem statement

Es ist imperativ, eine geeignete Datenbankanbindung zu wählen, um Aufgaben (Tasks), Notizen und Datumseinträge in der Anwendung zu speichern und zu verwalten. Es muss eine Methode gefunden werden, um mit der Datenbank zu interagieren und Python-Objekte in Datenbankeinträge umzuwandeln und umgekehrt.

### Decision

Die Entscheidung für SQLAlchemy als ORM wurde getroffen, um die Interaktion mit der Datenbank zu vereinfachen und die Datenbankabfragen in Python-Objekte zu übersetzen. Dadurch wird die Datenbankanbindung effizienter und der Code besser lesbar. Die Verwendung von SQLAlchemy ermöglicht eine unkomplizierte Handhabung von Datenbankoperationen und erhöht die Flexibilität bei der Verwaltung der Daten. Auch diese Entscheidung wurde gemeinsam getroffen. 

### Quellen

Eck, A. (2023). Full-Stack Web Dev @ HWR Berlin. HWR Berlin. https://hwrberlin.github.io/fswd/01-python-vscode.html#2-install-visual-studio-code-and-prepare-your-workspace (zuletzt geprüft am 28.07.2023).

Uwase, A. (2021, 8. Februar). Here is the reason why SQLAlchemy is so popular. Medium. https://towardsdatascience.com/here-is-the-reason-why-sqlalchemy-is-so-popular-43b489d3fb00 


## 05: Flash Messages

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 28-07-2023

### Problem statement

Benutzer wollen bzw. sollen über den Status ihrer Aktionen in der Anwendung informiert werden, z.B. wenn eine Aufgabe hinzugefügt, gelöscht oder eine fehlerhafte Eingabe gemacht wurde. Auch beim Registrierungsprozess und Login sind Meldungen wichtig.

### Decision

Die Verwendung von Flash-Nachrichten ermöglicht es, Benutzer über den Status ihrer Aktionen in der Anwendung zu informieren. Sie erhalten so sofortiges Feedback zu ihren Interaktionen, was die Benutzerfreundlichkeit erhöht. 

### Quellen

Nishant, V. (2020, 18. September). Flask flash() method – How to Flash Messages in Flask?. AskPython. https://www.askpython.com/python-modules/flask/flask-flash-method 

TechWithTim (2023, 29. Januar). Flask-Web-App-Tutorial. GitHub. https://github.com/techwithtim/Flask-Web-App-Tutorial (zuletzt geprüft am 28.07.2023).

## 06: Flask als Web Framework

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 28-07-2023

### Problem statement

Es muss ein geeignetes Web-Framework für die Entwicklung der Webanwendung gewählt werden, das unseren Anforderungen an Leichtigkeit, Flexibilität und Effizienz entspricht. Wir suchen nach einem Framework, das die Umsetzung der Routing-Funktionalität für die verschiedenen Seiten der Anwendung ermöglicht und eine saubere Strukturierung des Codes ermöglicht.

### Decision

Flask wurde von uns gemeinsam als Web-Framework gewählt, da es eine leichte und flexible Lösung für die Entwicklung von Webanwendungen in Python darstellt. Die Einfachheit von Flask ermöglicht eine effiziente Umsetzung der Routing-Logik, wodurch verschiedene Seiten der Anwendung leicht zugänglich sind. Darüber hinaus erlaubt Flask eine klare Trennung von Code und Präsentation, was zu einer gut strukturierten und leicht wartbaren Anwendung führt.

### Quellen

Eck, A. (2023). Full-Stack Web Dev @ HWR Berlin. HWR Berlin. https://hwrberlin.github.io/fswd/01-python-vscode.html#2-install-visual-studio-code-and-prepare-your-workspace (zuletzt geprüft am 28.07.2023).

Ionos (2023, 03. Januar). Web Development – What is Flask Python? A short Flask framework tutorial. Ionos Digital Guide. https://www.ionos.com/digitalguide/websites/web-development/flask-python/ (zuletzt geprüft am 28.07.2023)

## 07: Flask-Login

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 28-07-2023

### Problem statement

Es ist wichtig, eine effektive Möglichkeit zur Benutzerauthentifizierung und Sitzungsverwaltung in der Webanwendung zu implementieren. Es muss ein geeignetes Tool gefunden werden, das die Sicherheit der Anwendung gewährleistet und es den Benutzern ermöglicht, ihre persönlichen Aufgaben und Notizen zu verwalten, während gleichzeitig unbefugter Zugriff verhindert wird.

### Decision

Flask-Login wurde von uns als Authentifizierungsmechanismus gewählt, um den Anforderungen an Sicherheit und Benutzerfreundlichkeit gerecht zu werden. Mit Flask-Login können Benutzer sich in der Anwendung anmelden und ihre Sitzungen verwalten, was eine personalisierte Aufgaben- und Notizenverwaltung ermöglicht. Durch die Verwendung von Flask-Login wird gewährleistet, dass nur autorisierte Benutzer Zugriff auf die Anwendung haben und ihre persönlichen Daten schützen können. Wir haben beispielsweise an einigen Stellen 'login required' eingesetzt.

### Quellen

PythonBasics (2023). Flask Login Tutorial. https://pythonbasics.org/flask-login/ (zuletzt geprüft am 28.07.2023).

TechWithTim (2023, 29. Januar). Flask-Web-App-Tutorial. GitHub. https://github.com/techwithtim/Flask-Web-App-Tutorial (zuletzt geprüft am 28.07.2023). 


## 08: Individualisierbarkeit und Datenspeicherung durch den Nutzer

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 28-07-2023

### Problem statement

Benutzer haben individuelle Anforderungen an ihre Bewerbungsunterlagen und möchten persönliche Tasks erstellen, um ihre Bewerbungsvorbereitung besser zu organisieren. Es muss eine Möglichkeit geben, personalisierte Aufgaben hinzuzufügen. Gleichzeitig ist es wichtig, eine Methode zu finden, um es Benutzern zu ermöglichen, Informationen zu speichern, indem sie Notizen hinzufügen, und auch Datumsangaben speichern und anzuzeigen, um die Organisation der Bewerbungsunterlagen zu erleichtern.

### Decision

Eine Funktion zur Hinzufügung von persönlichen Tasks wurde in die Webanwendung integriert. Dadurch können Benutzer ihre individuellen Aufgaben erstellen und verwalten, um ihre Bewerbungsunterlagen maßgeschneidert zu organisieren. Die Individualisierbarkeit trägt dazu bei, dass Benutzer die Anwendung effektiv nutzen können, indem sie ihre spezifischen Aufgabenbereiche gezielt verwalten.
Die Möglichkeit, Notizen zu speichern, erlaubt es Benutzern, wichtige Informationen im Zusammenhang mit ihrer Studienbewerbung zu verwalten. Die Funktion zur Datumsangabe bietet eine praktische Möglichkeit, wichtige Termine im Bewerbungsprozess im Auge zu behalten. Durch diese Funktionen kann jeder Benutzer seine Bewerbungsunterlagen individuell gestalten und seine Aufgaben und Termine personalisieren, was zu einer effizienten Organisation führt. Diese Design-Entscheidung wurde in der Entwurf-Phase von beiden Teammitgliedern gemeinsam getroffen.

## 09: Jinja-Templates

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 28-07-2023

### Problem statement

Die Problematik liegt darin, eine effiziente Methode zur Generierung der HTML-Ausgabe der Webanwendung zu finden und gleichzeitig eine saubere Trennung von Code (Python) und Präsentation (HTML) zu gewährleisten.

### Decision

Jinja-Templates wurden von uns gemeinsam gewählt, um die HTML-Ausgabe der Webanwendung zu generieren und eine klare Trennung von Code und Präsentation zu ermöglichen. Die Verwendung von Jinja-Templates erlaubt es, dynamische Inhalte in die HTML-Seiten einzubetten und den Code besser lesbar zu gestalten. Durch diese Vorgehensweise wird eine klare Strukturierung der Präsentationsschicht erreicht.

### Quellen

Eck, A. (2023). Full-Stack Web Dev @ HWR Berlin. HWR Berlin. https://hwrberlin.github.io/fswd/01-python-vscode.html#2-install-visual-studio-code-and-prepare-your-workspace (zuletzt geprüft am 28.07.2023).

Mohajeryami, S. (2023, 10. März). Jinja: The Ultimate Tool for Customizable Python Templates. Medium. https://bootcamp.uxdesign.cc/jinja-the-ultimate-tool-for-customizable-python-templates-deb70089c936 


## 10: Trennung von views.py und auth.py

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 28-07-2023

### Problem statement

Es musste eine Methode gefunden werden, um die Authentifizierungsfunktionen von den Ansichten und Routen der Anwendung zu entkoppeln, um den Code übersichtlicher und besser strukturierbar zu gestalten.

### Decision

Unsere Lösung bestand darin, eine klare Trennung zwischen den verschiedenen Funktionen und Ansichten der Webanwendung (views.py) und der Implementierung der Benutzerauthentifizierung (auth.py) zu schaffen. 
Die Trennung von views.py und auth.py wurde aus Gründen der Modulartigkeit und der besseren Codeorganisation vorgenommen. Indem die Authentifizierungsfunktionen in einem separaten Modul (auth.py) ausgelagert wurden, bleibt views.py auf die spezifischen Seiten-Views, Routen und Anwendungslogik fokussiert. Dadurch wird der Code übersichtlicher und leichter lesbar.

Die Trennung erlaubt auch eine klare Abgrenzung der Verantwortlichkeiten: views.py kümmert sich um die Darstellung und Logik der Webseiten, während auth.py sich ausschließlich um die Authentifizierungsfunktionen kümmert.


### Quellen

TechWithTim (2023, 29. Januar). Flask-Web-App-Tutorial. GitHub. https://github.com/techwithtim/Flask-Web-App-Tutorial (zuletzt geprüft am 28.07.2023). 

## 11: Vertikale Ausrichtung

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 28-07-2023

### Problem statement

Die Benutzeroberfläche der Webanwendung muss auch auf Smartphones und anderen Geräten mit vertikaler Ausrichtung eine angemessene Bedienbarkeit und Lesbarkeit bieten. Die Standard-Darstellung könnte zu unübersichtlich und schwer zu bedienen sein.

### Decision

Die Webanwendung wurde so gestaltet, dass sie eine responsive vertikale Ausrichtung auf verschiedenen Geräten bietet. Dadurch wird die Benutzeroberfläche für Smartphones optimiert, indem sie natürliche vertikale Bildschirmbewegungen berücksichtigt. Die Anpassung der Anwendung an verschiedene Bildschirmgrößen verbessert die Benutzererfahrung und erleichtert die Bedienung auf mobilen Geräten. Auch diese Design-Entscheidung wurde im Entwurf-Prozess getroffen.

### Regarded options

Eine horizontale Ausrichtung ist für Nutzer am Computer eventuell angenehmer, weil sie weniger scrollen müssen. Allerdings können mit einer vertikalen Ausrichtung auch Smartphone-User die Anwendung bequem bedienen, woraus wir geschlossen haben, dass der allgemeine Nutzen mit einer vertikalen Orientierung für mehr Menschen gegeben ist als bei einer horizontalen. 

## 12: Verwendung von Bootstrap – Vereinfachung und effiziente Erstellung von Benutzeroberflächen

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 28-07-2023

### Problem statement

Die Erstellung einer ansprechenden und benutzerfreundlichen Benutzeroberfläche ist entscheidend, aber zeitaufwendig. Es muss eine Möglichkeit gefunden werden, die Gestaltung zu vereinfachen.

### Decision

Bootstrap wurde gewählt, um die Gestaltung der Benutzeroberfläche zu vereinfachen und konsistente Darstellungen auf verschiedenen Geräten sicherzustellen. Die vorgefertigten Stile und Layouts ermöglichen eine schnelle Entwicklung. Die Integration von Bootstrap vereinfacht die Gestaltung der Benutzeroberfläche und spart Zeit bei der Entwicklung. Durch die Anpassung an verschiedene Geräte wird eine gute Benutzererfahrung sichergestellt.

### Regarded options

Eigenes CSS: Anstelle der Verwendung eines CSS-Frameworks wie Bootstrap könnten wir unser eigenes, maßgeschneidertes CSS für die Gestaltung der Benutzeroberfläche verwenden. Dies würde jedoch mehr Zeit und Aufwand erfordern, um die Stile von Grund auf neu zu erstellen.

UI-Bibliotheken: Anstelle eines reinen CSS-Frameworks könnte die Webanwendung eine UI-Bibliothek verwenden.

Die Entscheidung, Bootstrap als Framework zu verwenden, wurde aus mehreren Gründen getroffen.

Zum einen hatten wir keine umfangreiche Erfahrung mit der Erstellung eines eigenen CSS von Grund auf. Die Entwicklung eines maßgeschneiderten CSS hätte einen erheblichen Zeitaufwand erfordert, und die Ressourcen hätten nicht im Verhältnis zum Nutzen gestanden.

Darüber hinaus bietet Bootstrap vorgefertigte Stile und Layouts, die eine schnelle Entwicklung ermöglichen. Da wir ein begrenztes Zeitbudget hatten und eine schnell einsatzbereite Lösung bevorzugten, erschien uns Bootstrap als die beste Wahl. Die Verwendung von Bootstrap half uns dabei, eine ansprechende und konsistente Benutzeroberfläche zu erstellen, die auf verschiedenen Geräten gut funktioniert.

Obwohl es andere UI-Bibliotheken gab, haben wir uns bewusst entschieden, bei Bootstrap zu bleiben. Die bereits vorhandene Integration von Bootstrap in die Webanwendung und die damit verbundene Vertrautheit mit dem Framework waren ausschlaggebende Faktoren. Eine Umstellung auf eine andere UI-Bibliothek hätte zusätzliche Anpassungen und Tests erfordert, was in Anbetracht des Fortschritts der Entwicklung und der begrenzten Ressourcen nicht praktikabel erschien.

### Quellen

Jordana, A. (2023, 19. Mai). What Is Bootstrap?. Hostinger Tutorials. https://www.hostinger.com/tutorials/what-is-bootstrap/#:~:text=It's%20designed%20to%20ease%20the,about%20basic%20commands%20and%20functions. (zuletzt geprüft am 28.07.2023).


---