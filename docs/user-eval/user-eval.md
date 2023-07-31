---
title: User Evaluation
nav_order: 3
---

Lasse Schmidt und Isabel Kaspar
{: .label }

# User evaluation
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>


## 01: Registrierungsprozess

### Meta

Status
: **In Bearbeitung** - Abgeschlossen - Überholt

Aktualisiert am
: 31-07-2023

### Ziel

Von welchen Punkten auf der Website kann der User sich registrieren? Wie ist der Ablauf bei der Registrierung? Gibt es Unannehmlichkeiten bei dem Registrierungsprozess?

### Methode

Die Methode besteht darin, so vorzugehen, als wäre ich (Isabel, eigentlich die Rolle der Entwicklerin) in der Rolle des Users mit Erfahrungswerten einer Person, die sich bereits auf anderen Websites registriert hat und mit dem grundsätzlichen Prozess vertraut ist.  
### Ergebnisse

Der Start der Registrierung verläuft so, dass sich der User auf der Homepage bzw. Landing Page befindet. Hier hat er die Optionen, entweder über den Sign Up-Button auf der Seite zu gehen oder die Navigationsleiste dafür zu verwenden. Er hat also zwei Wege, die ihm zur Verfügung stehen, um die Registrierung zu beginnen. 
Der Ablauf der Registrierung ist sehr simpel. Es sind lediglich Name, E-Mail-Adresse und Passwort gefragt. Diese Eingaben sind schnell getan. 
Eine Unannehmlichkeit besteht allerdings. Wenn der Nutzer eine Fehlermeldung erhält, sobald er auf den Sign Up-Button klickt, werden all seine Einträge gelöscht. Auch wenn er zum Beispiel ein bereits vergebenes Passwort eingegeben hat und dies zu einer Fehlermeldung bzw. Warnung an den User kommt, werden auch Name und E-Mail-Adresse gelöscht. Er muss alles noch einmal eingeben.


### Implikationen

Wir möchten einen Weg finden, dass nur der betroffene „falsche“ Eintrag gelöscht wird und nicht alle Einträge.

## 02: Anmelden und Aufgabenliste

### Meta

Status
: In Bearbeitung - **Abgeschlossen** - Überholt

Aktualisiert am
: 31-07-2023

### Ziel

Szenario: Ein Benutzer loggt sich ein möchte seine Aufgabenliste einsehen und bearbeiten.
- Wie verläuft der Anmeldeprozess mit Benutzernamen und Passwort? 
- Verläuft der Vorgang „Prüfen der Aufgabenliste“ und „Markieren einer Aufgabe als erledigt“ ohne Probleme? Kann man eine erledigte Aufgabe als "not completed" zurücksetzen?
- Kann der User eine neu hinzugefügte Aufgabe noch sehen, nachdem er sich ausgeloggt und erneut eingeloggt hat?

### Methode

Die Methode besteht darin, so vorzugehen, als wäre ich (Isabel, eigentlich die Rolle der Entwicklerin) in der Rolle des Users mit Erfahrungswissen einer Person, die an einer Universität studiert und oft mit Webanwendungen in Kontakt kommt.

### Ergebnisse

- Der Anmeldeprozess verläuft schnell und es sind E-Mail-Adresse und Passwort gefordert. Der User gelangt über die Navigationsleiste zum Login.
- Der Vorgang „Prüfen der Aufgabenliste“ und „Markieren einer Aufgabe als erledigt“ funktioniert fehlerfrei. Eine erledigte Aufgabe kann wieder zurückgesetzt werden. Dieser Vorgang kann auch n Male wiederholt werden.
- Der User kann eine neu hinzugefügte Aufgabe noch sehen, nachdem er sich ausgeloggt und erneut eingeloggt hat.

### Implikationen

Wir sind zufrieden, wie der Login-Prozess sowie die Einsicht und Bearbeitung der Aufgabenliste durch den User erfolgt. An dieser Stelle sehen wir vorerst keine Änderungen vor.

## 03: Notizenfunktion 

### Meta

Status
: In Bearbeitung - **Abgeschlossen** - Überholt

Aktualisiert am
: 31-07-2023

### Ziel

Szenario: Ein Benutzer ist bereits eingeloggt und befindet sich auf der Application Part One oder Two Seite und möchte dort die Notizfunktion nutzen: 
- Der Benutzer erstellt eine Notiz mit einem beliebigen Text als Inhalt
- Der Benutzer löscht die erstellte Notiz wieder
- Der Benutzer erstellt mehrere Notizen und achtet darauf, ob es ein Limit für die Anzahl der erstellten Notizen gibt
- Der Benutzer loggt sich aus und möchte, nachdem er sich wieder eingeloggt hat, seine erstellten Notizen angucken. 


### Methode

Die Methode besteht darin, so vorzugehen, als wäre ich (Lasse, eigentlich die Rolle des Entwicklers) in der Rolle des Users mit Erfahrungswissen einer Person, die an einer Universität studiert und oft mit Webanwendungen in Kontakt kommt.

### Ergebnisse
- Das Hinzufügen von Notizen ist simpel, denn der User benutzt das Textfeld, um seine Notiz zu schreiben. Danach drückt er auf den Knopf „Add a Note“ und schon ist die Notiz der Seite hinzugefügt. Diesen Vorgang kann der User auch n-Mal wiederholen. 
- Das Löschen der hinzugefügten Notiz funktioniert so, dass der User das Kreuz bei der erstellten Notiz drückt. Sobald er dies macht, wird die erstellte Notiz gelöscht. 
- Der User kann eine neu hinzugefügte Notiz noch sehen, nachdem er sich ausgeloggt und erneut eingeloggt hat.

### Implikationen

Wir sind zufrieden, wie die Notizenfunktion aufgebaut ist und der User schnell seine eigenen Notizen hinzufügen und löschen kann. Diese Funktion ist simpel gehalten, wie wir es uns vorgestellt haben. Daher sehen wir an dieser Stelle vorerst keine Änderungen vor.

## 04: Datumsfehlermeldung

### Meta

Status
: In Bearbeitung - **Abgeschlossen** - Überholt

Aktualisiert am
: 31-07-2023

### Ziel

Szenario: Ein Benutzer versucht mehrere Daten für eine Application Part Seite hinzuzufügen. 
- Was passiert, wenn der User versucht mehrere Daten für eine Seite hinzuzufügen?

### Methode

Die Methode besteht darin, so vorzugehen, als wäre ich (Lasse, eigentlich die Rolle des Entwicklers) in der Rolle des Users mit Erfahrungswissen einer Person, die an einer Universität studiert und oft mit Webanwendungen in Kontakt kommt.

### Ergebnisse

Sobald der User ein Datum hinzugefügt hat, steht dies oben auf der Seite (entweder Application Part One or Two). Versucht er jedoch ein weiteres Datum der Seite hinzuzufügen, so wird eine Fehlermeldung angezeigt, dass bereits ein Datum hinzugefügt wurde und dieses erst gelöscht werden muss bevor ein neues Datum hinzugefügt werden kann. 

### Implikationen

Wir sind zufrieden, wie die Datumsfunktion auch diese Option handhabt und der Benutzer nicht mehr als ein Datum hinzufügen kann. Dies entspricht unserem Design, dass pro Seite nur ein Datum, als Deadline, erstellt werden kann. Da diese Funktion unseren Ansprüchen entspricht, sehen wir an dieser Stelle vorerst keine Änderungen vor.
