# RasaGdKi

Zuerst env erstellen mit python 3.7.2
Wir hatten auch das neuste und 3.8 verwendet. Allerdings gab es hier immer irgendwelche pakackes, welche sich nicht mit den neueren Versionen verstanden haben.
1. conda create -n rasagdki python==3.7.2

env starten. Dies hat auch nicht in der Powershell funktiniert. Nach langen ausprobieren haben wir dann festgestellt, dases wirklich an der powershell liegt und wir sind auf den cmd terminal umgestiegen
2. conda activate rasagdki

Auch hatten wir mit pip3 sowie mit pip unsere Porbleme. Am Ende hat es am ebsten mit pip 20.2 funktiniert.

3. pip install --upgrade pip==20.2

Installation von rasa
4. pip install rasa

Jetzt werden ersteinmal die ganzen fehler ausgemerzt, da sanic und tensorflow auf einem zu neuen stand sind.
Das hat dann jedoch nicht funktiniert. deshalb habe ich noch einmal rasa gelöscht und es doch mit pip3 versucht was dann auch nicht funktioniert hat. wir haben es dann mit dem befehl 

5. pip uninstall rasa

Auf stackoverflow haben wir folgende lösung gefunden

6. pip install <PACKAGE> --use-feature=2020-resolver

Rasa wurde jetzt erfolgreich isntalliert!

Wir richten das directory ein mit dem Befehl und trainieren das Model

7. rasa init

Das Framework ist jetzt betriebsbereit und es können erste tests gemacht werden ob alles läuft.

Der Assistent kann mit
8. rasa shell direkt getestet werden













