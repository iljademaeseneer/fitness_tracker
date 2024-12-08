# fitness_tracker
fitness tracking application

Een eenvoudige CLI app om oefeningen van een workout overzichtelijk bij te houden

## Functionaliteiten
- Voeg een oefening toe
- Bekijk opgeslagen oefeningen

## Installatie
1. Clone de repository.
2. Maak een virtuele omgeving en installeer de vereisten: zie requirements.txt
python -m venv venv source venv/bin/activate pip install -r requirements.txt
3. Initialiseer de database:
python -c "from src.db_handler import init_db; init_db()"


## Gebruik
- Voeg een oefening toe:
python src/cli.py add --name "Push Ups" --sets 3 --reps 10




