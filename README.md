	Initial, se instaleaza RASA NLU: 

- se instaleaza python3 si pip3:

	$  s u d o  a p t  u p d a t e
	$  s u d o  a p t  i n s t a l l  p y t h o n 3−d e v  p y t h o n 3−p i p

- se creeaza un mediu virtual si se activeaza:

	$  p y t h o n 3  −m   v e n v   . / v e n v
	$  s o u r c e   . / v e n v / b i n / a c t i v a t e

- se instaleaza RASA cu ajutorul pip:
	
	$  p i p  i n s t a l l  r a s a

- se initializeaza un proiect nou:

	$  r a s a  i n i t  −−no−p r o m p t

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
