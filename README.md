
Rasa installieren
$ pip install rasa

Discord packages installieren
$ pip3 install discord.py python_dotenv pytz requests

Um die Discord API auf einem eigenen Bot zu nutzen, muss der Discord Token in der StartDiscordConnection ausgetauscht werden.

Google API Installieren
$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

Um Die Google API selbst zu verwenden, muss unter Google Cloud Plattforms ein eigener OAuth 2.0 Client erstellt werden. Der Cleint-Secret muss client_secret.json genannt werden unter unter actions abgelegt werden. 
Um den ersten Token zu erstellen kann CreateFirstToken.py aufgeführt werden.

Spacy German NLU
$ pip3 install spacy==3.0.6
$ pip install packages/de_ner_demo_replace-0.0.0/

Um Pipelines für Spacy zu konfigurieren config.yml pipelines bearbeiten zu:
pipeline:
  - name: SpacyNLP
  - name: SpacyTokenizer
  - name: SpacyFeaturizer
  - name: RegexFeaturizer
  - name: LexicalSyntacticFeaturizer
  - name: CountVectorsFeaturizer
  - name: CountVectorsFeaturizer
    analyzer: "char_wb"
    min_ngram: 1
    max_ngram: 4
  - name: DIETClassifier
    epochs: 100
  - name: EntitySynonymMapper
  - name: ResponseSelector
    epochs: 100

Um alles zu starten:
$ rasa train nlu
$ rasa train
$ rasa run
$ rasa run actions
$ StartDiscordConnection.py