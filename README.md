	Initial, se instaleaza RASA NLU: 

- se instaleaza python3 si pip3:

	$ sudo apt update
	$ sudo apt install python3-dev python3-pip

- se creeaza un mediu virtual si se activeaza:

	$ python3 -m venv ./venv
	$ source ./venv/bin/activate
	
- se instaleaza RASA cu ajutorul pip:
	
	$ pip install rasa

- se initializeaza un proiect nou:

	$ rasa init --no-prompt

	A fost creat fisierul actions.py, unde au fost implementate actiunile necesare pentru a face procesarea de limbaj natural a comenzilor date de catre utilizator. A mai fost creat un director “data”, unde sunt datele propriu-zise si anume variatii ale comenzilor pe care utilizatorul le poate da. In acest director mai exista un alt director “lookup_tables”, unde sunt fisiere pentru fiecare parametru de sanatate (si nu doar) existent in proiect ce contin sinonime pentru fiecare parametru in parte. Atunci cand fisierele respective sunt modificate, este necesara antrenarea modelului pentru a putea vedea schimbarile. Acest lucru se face cu comanda: 

	$ rasa train


	Sunt necesare instalarea bibliotecilor din Python: pandas, SpeechRecognition, pyAudio, tkinter, subprocess si gtts. Se instaleaza cu comanda: pip install <nume_biblioteca>.

	Seturile de date pentru a da raspunsuri sunt in fisierul date.csv. Este utilizat in actions.py si chatbot.py. 


	Initial, se da comanda de mai jos pentru a deschide un server RASA pe portul 5002, cu endpoints si credentialele specificate in fisierele .yml si modelul antrenat: 

	$ rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml

	In alt terminal,  se ruleaza fisierul de actiuni actions.py cu comanda:
	
	$ rasa run actions

	Intr-un final, in alt terminal se ruleaza aplicatia propriu-zisa, interfata multimodala implementata in fisierul chatbot.py:

	$ python chatbot.py
