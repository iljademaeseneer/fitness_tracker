import argparse
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.db_handler import add_exercise, list_exercises

def main():
    parser = argparse.ArgumentParser(description="Fitness Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # Voeg oefening toe
    add_parser = subparsers.add_parser('add', help="Voeg een oefening toe")
    add_parser.add_argument('--name', required=True, help="Naam van de oefening")
    add_parser.add_argument('--sets', type=int, required=True, help="Aantal sets")
    add_parser.add_argument('--reps', type=int, required=True, help="Aantal reps per set")

    # Bekijk oefeningen
    list_parser = subparsers.add_parser('list', help="Bekijk alle oefeningen")

    args = parser.parse_args()

    if args.command == 'add':
        add_exercise(args.name, args.sets, args.reps)
        print("Oefening toegevoegd!")
    elif args.command == 'list':
        exercises = list_exercises()
        for exercise in exercises:
            print(f"{exercise[0]}: {exercise[1]} - {exercise[2]} sets van {exercise[3]} reps op {exercise[4]}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
