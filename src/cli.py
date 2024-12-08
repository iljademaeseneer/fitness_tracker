import argparse
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.db_handler import add_exercise, list_exercises

def main():
    # Maak een parser voor de command-line argumenten
    parser = argparse.ArgumentParser(description="Fitness Tracker")
    subparsers = parser.add_subparsers(dest="command")  # subparsers voor verschillende commando's

    # Voeg een oefening toe
    add_parser = subparsers.add_parser('add', help="Voeg een oefening toe")
    add_parser.add_argument('--name', required=True, help="Naam van de oefening")
    add_parser.add_argument('--sets', type=int, required=True, help="Aantal sets")
    add_parser.add_argument('--reps', type=int, required=True, help="Aantal reps per set")

    # Bekijk alle oefeningen
    list_parser = subparsers.add_parser('list', help="Bekijk alle oefeningen")

    # Verwijder een oefening
    delete_parser = subparsers.add_parser('delete', help="Verwijder een oefening")
    delete_parser.add_argument('--id', type=int, required=True, help="ID van de oefening om te verwijderen")

    # Bewerk een oefening
    update_parser = subparsers.add_parser('update', help="Bewerk een oefening")
    update_parser.add_argument('--id', type=int, required=True, help="ID van de oefening om te bewerken")
    update_parser.add_argument('--name', help="Nieuwe naam van de oefening")
    update_parser.add_argument('--sets', type=int, help="Nieuw aantal sets")
    update_parser.add_argument('--reps', type=int, help="Nieuw aantal reps")

    # Filter oefeningen op datum
    filter_parser = subparsers.add_parser('filter', help="Filter oefeningen op datum")
    filter_parser.add_argument('--date', required=True, help="Datum (YYYY-MM-DD) om oefeningen te filteren")

    # Verwerk de argumenten
    args = parser.parse_args()

    if args.command == 'add':
        # Voeg een oefening toe
        add_exercise(args.name, args.sets, args.reps)
        print(f"Oefening '{args.name}' toegevoegd: {args.sets} sets van {args.reps} reps.")

    elif args.command == 'list':
        # Bekijk alle oefeningen
        exercises = list_exercises()
        if exercises:
            for exercise in exercises:
                print(f"{exercise[0]}: {exercise[1]} - {exercise[2]} sets van {exercise[3]} reps op {exercise[4]}")
        else:
            print("Er zijn nog geen oefeningen opgeslagen.")

    elif args.command == 'delete':
        # Verwijder een oefening
        delete_parser(args.id)
        print(f"Oefening met ID {args.id} is verwijderd.")

    elif args.command == 'update':
        # Bewerk een oefening
        update_parser(args.id, name=args.name, sets=args.sets, reps=args.reps)
        print(f"Oefening met ID {args.id} is bijgewerkt.")

    elif args.command == 'filter':
        # Filter oefeningen op datum
        exercises = filter_parser(args.date)
        if exercises:
            print(f"Oefeningen op {args.date}:")
            for exercise in exercises:
                print(f"{exercise[0]}: {exercise[1]} - {exercise[2]} sets van {exercise[3]} reps")
        else:
            print(f"Geen oefeningen gevonden voor de datum {args.date}.")

    else:
        # Als er geen geldig commando is, print dan de help
        parser.print_help()

if __name__ == '__main__':
    main()
