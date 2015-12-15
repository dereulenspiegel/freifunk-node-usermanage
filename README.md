# PoC zum Usermanagement auf FFRL Servern

Dieses Repo soll zeigen wie in Zukunft mal User im FFRL gemanaged werden können. Andere Communities können diesen
Ansatz aber leicht übernehmen.

## Setup

Es ist so viel wie möglich automatisiert worden. Daher reicht unter Linux oder MacOS X ein `make setup` um alle
nötigen Voraussetzungen zu installieren.

## Benutzung

Um die User auf allen im Inventory definierten Systemen zu managen reicht `make manage-users`.

### User hinzufügen

User sind als JSON-Dateien definiert. Konvention ist es die JSON-Datei [benutzername].json zu nennen.
Die Datei für einen User sieht typischerweise so aus:
```json
{
  "id": "till",
  "action": "create",
  "shell": "/bin/bash",
  "comment": "Till Klocke (till.klocke@gmail.com)",
  "system": false,
  "groups": [
    "sudo"
  ],
  "ssh_keys": [
    "öffentlicher SSH-Key"
  ]
}
```

Diese Dateien werden dann unter databags/[Communitykürzel]/users abgelegt. Soll ein user entfernt werden, wird
das Feld 'action' einfach von 'create' auf 'delete' geändert.

### Communities verwalten

Um eine Community hinzuzufügen muss zuerst ein passender Ordner für deren User hinzugefügt werden. Dies ist 
databags/[Communitykürzel]/users und natürlich sollten einige User in diesem Ordner angelegt werden.

Zusätzlich muss ein neuer Ordner unter playbooks/group_vars angelegt werden. Dieser trägt wieder das Communitykürzel
als Namen. In diesem Ordner muss eine Datei beliebeigen Namens ( aber am besten mit der Endung yml ) angelegt werden.
Hier muss nun die Variable `ffrl_community: [Communitykürzel]` definiert werden.

Zusätzlich muss unter inventory noch eine statische Inventory-Datei mit dem Communitykürzel angelegt werden, in der alle
Hosts dieser Community in einer Gruppe names [Communitykürzel] erfasst sind.

Beispielhaft ist das für die Community Dortmund schon geschehen.