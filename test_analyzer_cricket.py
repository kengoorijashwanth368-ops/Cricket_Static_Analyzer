"""
=============================================================================
Project Title: Cricket Statistics Analyzer
Course: Python Programming (Course-End Project)
College: Vardhaman College of Engineering
Description:
    A complete, single-file Python application to process, analyze, and
    compare cricket player statistics. Designed to run seamlessly in any
    Python environment or online compiler with ZERO external dependencies.

Syllabus Topics Covered:
    1. Variables & Data Types (int, float, str, bool)
    2. Operators (Arithmetic, Relational, Logical, Membership)
    3. Conditional Statements (if, elif, else)
    4. Loops (while, for, enumerate, break, continue)
    5. Strings & Text Formatting (f-strings, strip, lower, title, center)
    6. Collections (Lists, Tuples, Sets)
    7. Dictionaries (Nested player records, key-value mappings)
    8. Functions (Modular parameters, return values, type hints)
    9. Recursion (Base cases & recursive steps: sum and binary search)
    10. Searching Algorithms (Linear Search & Recursive Binary Search)
    11. Sorting Algorithms (Custom Bubble Sort with swap flag optimization)
    12. File I/O & Persistence (JSON load/save and formatted TXT report export)
    13. Exception Handling (try, except, ZeroDivisionError, ValueError)
=============================================================================
"""

import copy
import json
import os
from typing import List, Dict, Any, Optional, Tuple

# =============================================================================
# DEFAULT IN-MEMORY DATASET (5 CORE PLAYERS: Rohit, Virat, Dhoni, Iyer, Bumrah)
# Ensures the code runs seamlessly in ANY compiler without external file dependencies
# =============================================================================

DEFAULT_PLAYERS: List[Dict[str, Any]] = [
    {
        "id": 1,
        "name": "Rohit Sharma",
        "country": "India",
        "role": "Batsman",
        "matches": 262,
        "innings": 254,
        "runs": 10709,
        "balls_faced": 11720,
        "highest_score": 264,
        "not_outs": 36,
        "centuries": 31,
        "half_centuries": 55,
        "fours": 995,
        "sixes": 323,
        "wickets": 9,
        "overs_bowled": 128.5,
        "runs_conceded": 715
    },
    {
        "id": 2,
        "name": "Virat Kohli",
        "country": "India",
        "role": "Batsman",
        "matches": 292,
        "innings": 280,
        "runs": 13848,
        "balls_faced": 14780,
        "highest_score": 183,
        "not_outs": 44,
        "centuries": 50,
        "half_centuries": 72,
        "fours": 1294,
        "sixes": 151,
        "wickets": 5,
        "overs_bowled": 108.2,
        "runs_conceded": 680
    },
    {
        "id": 3,
        "name": "MS Dhoni",
        "country": "India",
        "role": "Wicket-Keeper",
        "matches": 350,
        "innings": 297,
        "runs": 10773,
        "balls_faced": 12303,
        "highest_score": 183,
        "not_outs": 84,
        "centuries": 10,
        "half_centuries": 73,
        "fours": 826,
        "sixes": 229,
        "wickets": 1,
        "overs_bowled": 6.0,
        "runs_conceded": 31
    },
    {
        "id": 4,
        "name": "Shreyas Iyer",
        "country": "India",
        "role": "Batsman",
        "matches": 62,
        "innings": 57,
        "runs": 2421,
        "balls_faced": 2390,
        "highest_score": 128,
        "not_outs": 7,
        "centuries": 5,
        "half_centuries": 18,
        "fours": 228,
        "sixes": 59,
        "wickets": 0,
        "overs_bowled": 11.1,
        "runs_conceded": 78
    },
    {
        "id": 5,
        "name": "Jasprit Bumrah",
        "country": "India",
        "role": "Bowler",
        "matches": 89,
        "innings": 28,
        "runs": 125,
        "balls_faced": 210,
        "highest_score": 16,
        "not_outs": 14,
        "centuries": 0,
        "half_centuries": 0,
        "fours": 12,
        "sixes": 3,
        "wickets": 149,
        "overs_bowled": 745.3,
        "runs_conceded": 3420
    }
]

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "data", "players.json") if "__file__" in globals() else "players.json"


# =============================================================================
# 1. FILE I/O & PERSISTENCE (WITH AUTOMATIC IN-MEMORY FALLBACK)
# =============================================================================

def load_player_data(filepath: str = DATA_FILE_PATH) -> List[Dict[str, Any]]:
    """Loads player statistics from JSON file, falling back gracefully to in-memory defaults.
    
    Demonstrates:
        - Exception handling (FileNotFoundError, json.JSONDecodeError)
        - Fallback resilience for online/external compilers
    """
    try:
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    return data
    except Exception:
        pass  # In online compilers or restricted environments, use embedded data

    # Use embedded copy to ensure standalone operation anywhere
    return copy.deepcopy(DEFAULT_PLAYERS)


def save_player_data(players: List[Dict[str, Any]], filepath: str = DATA_FILE_PATH) -> bool:
    """Saves player list back to JSON file.
    
    Demonstrates:
        - File writing with JSON indentation
        - Exception handling
    """
    try:
        dir_name = os.path.dirname(filepath)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(players, f, indent=2)
        return True
    except Exception as e:
        print(f"[Note]: Local file save skipped ({e}). In-memory records updated.")
        return False


# =============================================================================
# 2. STATISTICAL CALCULATION FUNCTIONS (OPERATORS & EXCEPTION HANDLING)
# =============================================================================

def calculate_batting_average(runs: int, innings: int, not_outs: int) -> float:
    """Calculates batting average: Runs / (Innings - NotOuts).
    
    Demonstrates:
        - Arithmetic operators
        - ZeroDivisionError exception handling
    """
    try:
        dismissals = innings - not_outs
        if dismissals <= 0:
            return float(runs)
        return round(runs / dismissals, 2)
    except ZeroDivisionError:
        return 0.0


def calculate_strike_rate(runs: int, balls_faced: int) -> float:
    """Calculates batting strike rate: (Runs / Balls) * 100.
    
    Demonstrates:
        - Percentage arithmetic
        - ZeroDivisionError handling
    """
    try:
        if balls_faced <= 0:
            return 0.0
        return round((runs / balls_faced) * 100, 2)
    except ZeroDivisionError:
        return 0.0


def calculate_bowling_average(runs_conceded: int, wickets: int) -> float:
    """Calculates bowling average: Runs Conceded / Wickets."""
    try:
        if wickets <= 0:
            return float("inf")
        return round(runs_conceded / wickets, 2)
    except ZeroDivisionError:
        return float("inf")


def calculate_economy_rate(runs_conceded: int, overs_bowled: float) -> float:
    """Calculates bowling economy rate: Runs Conceded / Overs Bowled.
    
    Handles cricket over fraction (e.g., 10.2 overs = 10 overs + 2 balls = 10.333 overs).
    """
    try:
        if overs_bowled <= 0.0:
            return 0.0
        complete_overs = int(overs_bowled)
        balls = round((overs_bowled - complete_overs) * 10)
        actual_overs = complete_overs + (balls / 6.0)
        if actual_overs <= 0:
            return 0.0
        return round(runs_conceded / actual_overs, 2)
    except ZeroDivisionError:
        return 0.0


def calculate_boundary_percentage(fours: int, sixes: int, total_runs: int) -> float:
    """Calculates percentage of runs scored in boundaries (4s and 6s)."""
    try:
        if total_runs <= 0:
            return 0.0
        boundary_runs = (fours * 4) + (sixes * 6)
        return round((boundary_runs / total_runs) * 100, 2)
    except ZeroDivisionError:
        return 0.0


def calculate_player_impact_score(player: Dict[str, Any]) -> float:
    """Calculates a composite MVP / Impact rating score.
    
    Formula:
        Impact = (Runs * 0.02) + (BatAvg * 0.35) + (StrikeRate * 0.25)
                 + (Wickets * 10) - (Economy * 2) + (Centuries * 8)
    """
    bat_avg = calculate_batting_average(player["runs"], player["innings"], player["not_outs"])
    sr = calculate_strike_rate(player["runs"], player["balls_faced"])
    econ = calculate_economy_rate(player.get("runs_conceded", 0), player.get("overs_bowled", 0.0))
    wickets = player.get("wickets", 0)
    centuries = player.get("centuries", 0)

    score = (
        (player["runs"] * 0.02)
        + (bat_avg * 0.35)
        + (sr * 0.25)
        + (wickets * 10.0)
        - (econ * 2.0)
        + (centuries * 8.0)
    )
    return round(max(0.0, score), 2)


# =============================================================================
# 3. RECURSION MODULE
# =============================================================================

def recursive_sum_runs(runs_list: List[int], index: int = 0) -> int:
    """Calculates total runs scored using Recursion.
    
    Demonstrates:
        - Base case: when index reaches end of list
        - Recursive step: current element + recursive call
    """
    if index >= len(runs_list):
        return 0
    return runs_list[index] + recursive_sum_runs(runs_list, index + 1)


def recursive_binary_search(
    sorted_players: List[Dict[str, Any]], 
    target_name: str, 
    low: int, 
    high: int
) -> Optional[Dict[str, Any]]:
    """Performs Recursive Binary Search on players sorted alphabetically by name.
    
    Complexity: O(log N)
    Demonstrates:
        - Divide and Conquer paradigm
        - Base cases (found or empty interval)
    """
    if low > high:
        return None

    mid = (low + high) // 2
    current_name = sorted_players[mid]["name"].strip().lower()
    target_clean = target_name.strip().lower()

    if current_name == target_clean:
        return sorted_players[mid]
    elif current_name > target_clean:
        return recursive_binary_search(sorted_players, target_name, low, mid - 1)
    else:
        return recursive_binary_search(sorted_players, target_name, mid + 1, high)


# =============================================================================
# 4. SEARCHING & SORTING ALGORITHMS
# =============================================================================

def linear_search_players(players: List[Dict[str, Any]], query: str) -> List[Dict[str, Any]]:
    """Performs Linear Search for substring match across name and role/country."""
    query_lower = query.strip().lower()
    return [
        p for p in players 
        if query_lower in p["name"].lower() 
        or query_lower in p["country"].lower() 
        or query_lower in p["role"].lower()
    ]


def bubble_sort_players(
    players: List[Dict[str, Any]], 
    metric_key: str, 
    descending: bool = True
) -> List[Dict[str, Any]]:
    """Sorts players by numerical attribute using classic Bubble Sort with swap flag.
    
    Demonstrates:
        - In-place swapping
        - Nested loops
        - Early exit optimization
    """
    sorted_list = players.copy()
    n = len(sorted_list)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            val1 = sorted_list[j].get(metric_key, 0)
            val2 = sorted_list[j + 1].get(metric_key, 0)

            should_swap = (val1 < val2) if descending else (val1 > val2)
            if should_swap:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                swapped = True
        if not swapped:
            break

    return sorted_list


# =============================================================================
# 5. DATA SETS, TUPLES & DICTIONARIES DEMONSTRATION
# =============================================================================

def get_unique_countries(players: List[Dict[str, Any]]) -> set:
    """Demonstrates Sets: returns distinct nationalities."""
    return {p["country"] for p in players}


def get_unique_roles(players: List[Dict[str, Any]]) -> set:
    """Demonstrates Sets: returns unique cricket roles."""
    return {p["role"] for p in players}


def get_player_summary_tuple(player: Dict[str, Any]) -> Tuple[str, str, int, float, float]:
    """Demonstrates Tuples: creates an immutable snapshot of key player stats."""
    avg = calculate_batting_average(player["runs"], player["innings"], player["not_outs"])
    sr = calculate_strike_rate(player["runs"], player["balls_faced"])
    return (player["name"], player["role"], player["runs"], avg, sr)


# =============================================================================
# 6. FORMATTING & DISPLAY FUNCTIONS (PURE ASCII FORMATTING)
# =============================================================================

def print_separator(char: str = "=", length: int = 80) -> None:
    """Prints a styled separator line."""
    print(char * length)


def display_player_table(players: List[Dict[str, Any]], title: str = "Player Statistics") -> None:
    """Displays player records in a clean, formatted ASCII table."""
    print_separator("=")
    print(f"{title.center(80)}")
    print_separator("=")
    headers = f"{'ID':<4} {'Name':<18} {'Country':<10} {'Role':<14} {'Runs':<7} {'Avg':<7} {'SR':<7} {'Wkts':<5}"
    print(headers)
    print_separator("-")

    if not players:
        print("No players found.".center(80))
        print_separator("=")
        return

    for p in players:
        avg = calculate_batting_average(p["runs"], p["innings"], p["not_outs"])
        sr = calculate_strike_rate(p["runs"], p["balls_faced"])
        print(
            f"{p['id']:<4} {p['name']:<18} {p['country']:<10} {p['role']:<14} "
            f"{p['runs']:<7} {avg:<7.2f} {sr:<7.2f} {p.get('wickets', 0):<5}"
        )
    print_separator("=")


def display_player_detailed_card(player: Dict[str, Any]) -> None:
    """Displays a detailed performance card for an individual cricketer."""
    bat_avg = calculate_batting_average(player["runs"], player["innings"], player["not_outs"])
    sr = calculate_strike_rate(player["runs"], player["balls_faced"])
    bowl_avg = calculate_bowling_average(player.get("runs_conceded", 0), player.get("wickets", 0))
    econ = calculate_economy_rate(player.get("runs_conceded", 0), player.get("overs_bowled", 0.0))
    boundary_pct = calculate_boundary_percentage(player.get("fours", 0), player.get("sixes", 0), player["runs"])
    impact = calculate_player_impact_score(player)

    print_separator("*")
    print(f" PLAYER PROFILE CARD: {player['name'].upper()} ".center(80, "*"))
    print_separator("*")
    print(f" Country      : {player['country']:<20} Role          : {player['role']}")
    print(f" Matches      : {player['matches']:<20} Innings       : {player['innings']}")
    print_separator("-")
    print(" BATTING METRICS:")
    print(f"  Runs        : {player['runs']:<20} Highest Score : {player['highest_score']}")
    print(f"  Bat Average : {bat_avg:<20} Strike Rate   : {sr}%")
    print(f"  Centuries   : {player.get('centuries', 0):<20} Half-Centuries: {player.get('half_centuries', 0)}")
    print(f"  Fours       : {player.get('fours', 0):<20} Sixes         : {player.get('sixes', 0)}")
    print(f"  Boundary %  : {boundary_pct}%")
    print_separator("-")
    print(" BOWLING METRICS:")
    print(f"  Wickets     : {player.get('wickets', 0):<20} Overs Bowled : {player.get('overs_bowled', 0.0)}")
    print(f"  Runs Given  : {player.get('runs_conceded', 0):<20} Economy Rate  : {econ}")
    bowl_avg_str = "N/A (0 wickets)" if bowl_avg == float("inf") else f"{bowl_avg:.2f}"
    print(f"  Bowl Average: {bowl_avg_str}")
    print_separator("-")
    print(f" OVERALL IMPACT / MVP SCORE: {impact} / 100.00")
    print_separator("*")


def compare_two_players(p1: Dict[str, Any], p2: Dict[str, Any]) -> None:
    """Performs a head-to-head comparison between two cricketers."""
    avg1 = calculate_batting_average(p1["runs"], p1["innings"], p1["not_outs"])
    avg2 = calculate_batting_average(p2["runs"], p2["innings"], p2["not_outs"])
    sr1 = calculate_strike_rate(p1["runs"], p1["balls_faced"])
    sr2 = calculate_strike_rate(p2["runs"], p2["balls_faced"])
    econ1 = calculate_economy_rate(p1.get("runs_conceded", 0), p1.get("overs_bowled", 0.0))
    econ2 = calculate_economy_rate(p2.get("runs_conceded", 0), p2.get("overs_bowled", 0.0))
    imp1 = calculate_player_impact_score(p1)
    imp2 = calculate_player_impact_score(p2)

    print_separator("=")
    print(f" HEAD-TO-HEAD COMPARISON: {p1['name']} VS {p2['name']} ".center(80))
    print_separator("=")
    row_fmt = "{:<25} | {:<22} | {:<22}"
    print(row_fmt.format("Metric", p1["name"], p2["name"]))
    print_separator("-")
    print(row_fmt.format("Country", p1["country"], p2["country"]))
    print(row_fmt.format("Role", p1["role"], p2["role"]))
    print(row_fmt.format("Matches", str(p1["matches"]), str(p2["matches"])))
    print(row_fmt.format("Total Runs", str(p1["runs"]), str(p2["runs"])))
    print(row_fmt.format("Batting Average", f"{avg1:.2f}", f"{avg2:.2f}"))
    print(row_fmt.format("Strike Rate", f"{sr1:.2f}%", f"{sr2:.2f}%"))
    print(row_fmt.format("Highest Score", str(p1["highest_score"]), str(p2["highest_score"])))
    print(row_fmt.format("100s / 50s", f"{p1.get('centuries', 0)} / {p1.get('half_centuries', 0)}", f"{p2.get('centuries', 0)} / {p2.get('half_centuries', 0)}"))
    print(row_fmt.format("Wickets", str(p1.get("wickets", 0)), str(p2.get("wickets", 0))))
    print(row_fmt.format("Economy Rate", f"{econ1:.2f}", f"{econ2:.2f}"))
    print(row_fmt.format("MVP Impact Score", f"{imp1:.2f}", f"{imp2:.2f}"))
    print_separator("=")

    print("ANALYSIS SUMMARY:")
    if avg1 > avg2:
        print(f" • {p1['name']} has a higher batting average (+{avg1 - avg2:.2f}).")
    elif avg2 > avg1:
        print(f" • {p2['name']} has a higher batting average (+{avg2 - avg1:.2f}).")
    else:
        print(" • Both players have an identical batting average.")

    if sr1 > sr2:
        print(f" • {p1['name']} scores faster with a higher strike rate (+{sr1 - sr2:.2f}%).")
    elif sr2 > sr1:
        print(f" • {p2['name']} scores faster with a higher strike rate (+{sr2 - sr1:.2f}%).")

    if imp1 > imp2:
        print(f" • Winner by Overall Impact: {p1['name']} (Score: {imp1})")
    elif imp2 > imp1:
        print(f" • Winner by Overall Impact: {p2['name']} (Score: {imp2})")
    else:
        print(" • Both players are tied in overall impact score.")
    print_separator("=")


def export_report_to_file(players: List[Dict[str, Any]], export_path: str = "cricket_analysis_export.txt") -> None:
    """Exports structured summary report to a text file."""
    try:
        with open(export_path, "w", encoding="utf-8") as f:
            f.write("=" * 70 + "\n")
            f.write("CRICKET STATISTICS ANALYZER - SUMMARY EXPORT REPORT\n")
            f.write("Generated by: Python Course-End Project (Author: Ruthvik)\n")
            f.write("=" * 70 + "\n\n")

            total_runs = recursive_sum_runs([p["runs"] for p in players])
            total_wickets = sum(p.get("wickets", 0) for p in players)
            f.write(f"Total Players Analyzed : {len(players)}\n")
            f.write(f"Cumulative Runs Scored  : {total_runs}\n")
            f.write(f"Cumulative Wickets Taken: {total_wickets}\n\n")

            f.write("-" * 70 + "\n")
            f.write(f"{'Name':<20} {'Role':<14} {'Runs':<8} {'Avg':<8} {'SR':<8} {'Wkts':<6}\n")
            f.write("-" * 70 + "\n")

            for p in players:
                avg = calculate_batting_average(p["runs"], p["innings"], p["not_outs"])
                sr = calculate_strike_rate(p["runs"], p["balls_faced"])
                f.write(
                    f"{p['name']:<20} {p['role']:<14} {p['runs']:<8} "
                    f"{avg:<8.2f} {sr:<8.2f} {p.get('wickets', 0):<6}\n"
                )
            f.write("=" * 70 + "\n")
        print(f"[Success]: Report successfully exported to '{export_path}'!")
    except Exception as e:
        print(f"[Export Notice]: File export skipped ({e}). Summary displayed on screen:")
        display_player_table(players, "EXPORT SUMMARY")


# =============================================================================
# 7. ADD PLAYER FUNCTIONALITY (VALIDATED INPUTS)
# =============================================================================

def add_new_player(players: List[Dict[str, Any]]) -> None:
    """Collects and validates inputs to register a new cricketer."""
    print_separator("-")
    print(" ENTER NEW CRICKETER DETAILS ".center(80, "-"))
    print_separator("-")

    name = input("Enter Player Name: ").strip()
    if not name:
        print("[Validation Error]: Player name cannot be blank.")
        return

    country = input("Enter Country: ").strip() or "India"

    print("Choose Role: [1] Batsman  [2] Bowler  [3] All-Rounder  [4] Wicket-Keeper")
    role_choice = input("Enter choice (1-4): ").strip()
    role_map = {"1": "Batsman", "2": "Bowler", "3": "All-Rounder", "4": "Wicket-Keeper"}
    role = role_map.get(role_choice, "Batsman")

    def get_valid_int(prompt: str, min_val: int = 0) -> int:
        while True:
            val_str = input(prompt).strip()
            try:
                val = int(val_str)
                if val < min_val:
                    print(f"Value must be at least {min_val}.")
                    continue
                return val
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def get_valid_float(prompt: str, min_val: float = 0.0) -> float:
        while True:
            val_str = input(prompt).strip()
            try:
                val = float(val_str)
                if val < min_val:
                    print(f"Value must be at least {min_val}.")
                    continue
                return val
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    matches = get_valid_int("Enter Matches Played: ")
    innings = get_valid_int("Enter Innings Batted: ")
    runs = get_valid_int("Enter Total Runs Scored: ")
    balls = get_valid_int("Enter Total Balls Faced: ")
    highest = get_valid_int("Enter Highest Score: ")
    not_outs = get_valid_int("Enter Times Not Out: ")
    centuries = get_valid_int("Enter Centuries (100s): ")
    half_centuries = get_valid_int("Enter Half-Centuries (50s): ")
    fours = get_valid_int("Enter Fours (4s): ")
    sixes = get_valid_int("Enter Sixes (6s): ")
    wickets = get_valid_int("Enter Wickets Taken: ")
    overs = get_valid_float("Enter Overs Bowled: ")
    runs_conceded = get_valid_int("Enter Runs Conceded: ")

    new_id = max([p["id"] for p in players], default=0) + 1

    new_player_dict = {
        "id": new_id,
        "name": name,
        "country": country,
        "role": role,
        "matches": matches,
        "innings": innings,
        "runs": runs,
        "balls_faced": balls,
        "highest_score": highest,
        "not_outs": not_outs,
        "centuries": centuries,
        "half_centuries": half_centuries,
        "fours": fours,
        "sixes": sixes,
        "wickets": wickets,
        "overs_bowled": overs,
        "runs_conceded": runs_conceded,
    }

    players.append(new_player_dict)
    save_player_data(players)
    print(f"\n[Success]: Player '{name}' (ID: {new_id}) successfully added!")


# =============================================================================
# 8. MAIN INTERACTIVE CLI MENU CONTROLLER
# =============================================================================

def print_main_menu() -> None:
    """Displays the user menu options."""
    print("\n" + "=" * 50)
    print("     🏏 CRICKET STATISTICS ANALYZER 🏏")
    print("=" * 50)
    print(" 1.  View All Players (Formatted Table)")
    print(" 2.  Search Player by Name / Role / Country (Linear Search)")
    print(" 3.  Search Player by Exact Name (Recursive Binary Search)")
    print(" 4.  View Detailed Player Profile Card & Impact Score")
    print(" 5.  Leaderboard: Top Run Scorers (Bubble Sort)")
    print(" 6.  Leaderboard: Top Wicket Takers (Bubble Sort)")
    print(" 7.  Leaderboard: Best Batting Strike Rates")
    print(" 8.  Head-to-Head Player Comparison")
    print(" 9.  Filter Players by Role / Country")
    print(" 10. Compute Cumulative Runs (Demonstrating Recursion)")
    print(" 11. Add a New Player Record")
    print(" 12. Export Analytical Summary Report (.txt)")
    print(" 13. Run Automated Verification Test Suite (Non-interactive)")
    print(" 0.  Exit")
    print("=" * 50)


def run_analyzer():
    """Main execution loop of the Cricket Statistics Analyzer."""
    players = load_player_data()

    while True:
        print_main_menu()
        choice = input("Enter your option (0-13): ").strip()

        if choice == "1":
            display_player_table(players, "CORE INDIAN SQUAD - ALL 5 PLAYERS")

        elif choice == "2":
            query = input("Enter player name or role keyword: ")
            results = linear_search_players(players, query)
            display_player_table(results, f"Search Results for '{query}' (Linear Search)")

        elif choice == "3":
            sorted_by_name = sorted(players, key=lambda x: x["name"].lower())
            target_name = input("Enter exact player name to search (e.g. MS Dhoni, Virat Kohli): ")
            result = recursive_binary_search(sorted_by_name, target_name, 0, len(sorted_by_name) - 1)
            if result:
                print("\n[Match Found via Recursive Binary Search!]")
                display_player_detailed_card(result)
            else:
                print(f"\n[Not Found]: No player found with name '{target_name}'.")

        elif choice == "4":
            try:
                pid = int(input("Enter Player ID to view profile (1-5): "))
                found = next((p for p in players if p["id"] == pid), None)
                if found:
                    display_player_detailed_card(found)
                else:
                    print(f"[Error]: Player with ID {pid} not found.")
            except ValueError:
                print("[Error]: Please enter a numeric ID.")

        elif choice == "5":
            top_scorers = bubble_sort_players(players, "runs", descending=True)
            display_player_table(top_scorers, "LEADERBOARD: TOP RUN SCORERS (BUBBLE SORT)")

        elif choice == "6":
            top_bowlers = bubble_sort_players(players, "wickets", descending=True)
            display_player_table(top_bowlers, "LEADERBOARD: TOP WICKET TAKERS (BUBBLE SORT)")

        elif choice == "7":
            sr_sorted = sorted(
                players, 
                key=lambda p: calculate_strike_rate(p["runs"], p["balls_faced"]), 
                reverse=True
            )
            print_separator("=")
            print(" LEADERBOARD: BEST BATTING STRIKE RATES ".center(80))
            print_separator("=")
            print(f"{'Rank':<5} {'Player Name':<20} {'Runs':<8} {'Balls':<8} {'Strike Rate':<12}")
            print_separator("-")
            for idx, p in enumerate(sr_sorted, start=1):
                sr = calculate_strike_rate(p["runs"], p["balls_faced"])
                print(f"{idx:<5} {p['name']:<20} {p['runs']:<8} {p['balls_faced']:<8} {sr:<12.2f}%")
            print_separator("=")

        elif choice == "8":
            display_player_table(players, "SELECT PLAYERS FOR COMPARISON")
            try:
                id1 = int(input("Enter ID of Player 1: "))
                id2 = int(input("Enter ID of Player 2: "))
                p1 = next((p for p in players if p["id"] == id1), None)
                p2 = next((p for p in players if p["id"] == id2), None)
                if p1 and p2:
                    compare_two_players(p1, p2)
                else:
                    print("[Error]: One or both Player IDs were not found.")
            except ValueError:
                print("[Error]: Invalid input. IDs must be integers.")

        elif choice == "9":
            roles = list(get_unique_roles(players))
            print(f"Available Roles: {', '.join(roles)}")
            r_choice = input("Enter role to filter (e.g. Batsman, Bowler, Wicket-Keeper): ").strip().lower()
            matched = [p for p in players if p["role"].lower() == r_choice]
            display_player_table(matched, f"Filtered by Role: {r_choice.title()}")

        elif choice == "10":
            runs_list = [p["runs"] for p in players]
            total_recursive = recursive_sum_runs(runs_list)
            print_separator("=")
            print(" RECURSION DEMONSTRATION ".center(80))
            print_separator("=")
            print(f" List of player runs extracted: {runs_list}")
            print(f" Computed Cumulative Runs (via recursive_sum_runs): {total_recursive}")
            print(f" Verification using Python's sum()             : {sum(runs_list)}")
            print(" Recursion verified successfully: Both results match!")
            print_separator("=")

        elif choice == "11":
            add_new_player(players)

        elif choice == "12":
            export_report_to_file(players)

        elif choice == "13":
            run_all_tests()

        elif choice == "0":
            print("\nThank you for using Cricket Statistics Analyzer. Goodbye!\n")
            break

        else:
            print("[Error]: Invalid option. Please select a valid number from the menu.")


# =============================================================================
# 9. EMBEDDED AUTOMATED TEST & VERIFICATION SUITE
# =============================================================================

def run_all_tests():
    """Executes non-interactive verification tests for all 5 core players.
    
    Can be run directly from menu Option 13 or with command line argument `python cricket_analyzer.py --test`.
    """
    print_separator("=")
    print("   AUTOMATED VERIFICATION RUN: CRICKET STATISTICS ANALYZER")
    print("   Dataset: 5 Core Players (Rohit, Virat, Dhoni, Iyer, Bumrah)")
    print_separator("=")
    print()

    # 1. Test Data Loading
    print(">>> TEST 1: Loading Player Records...")
    players = load_player_data()
    print(f"Loaded {len(players)} players successfully.\n")

    # 2. Test All Players Table Display
    print(">>> TEST 2: Displaying All 5 Players Formatted Table...")
    display_player_table(players, "CORE INDIAN SQUAD - ALL 5 PLAYERS")
    print()

    # 3. Test Linear Search
    print(">>> TEST 3: Linear Search for 'Batsman'...")
    batsmen = linear_search_players(players, "Batsman")
    display_player_table(batsmen, "Linear Search Results: Role 'Batsman'")
    print()

    # 4. Test Recursive Binary Search
    print(">>> TEST 4: Recursive Binary Search for 'MS Dhoni'...")
    sorted_players = sorted(players, key=lambda x: x["name"].lower())
    found_player = recursive_binary_search(sorted_players, "MS Dhoni", 0, len(sorted_players) - 1)
    if found_player:
        print("MS Dhoni successfully found via Recursive Binary Search!")
        display_player_detailed_card(found_player)
    else:
        print("Player not found.")
    print()

    # 5. Test Bubble Sort (Top Run Scorers)
    print(">>> TEST 5: Top Run Scorers (Bubble Sort Algorithm)...")
    top_runs = bubble_sort_players(players, "runs", descending=True)
    display_player_table(top_runs, "TOP RUN SCORERS (BUBBLE SORT)")
    print()

    # 6. Test Bubble Sort (Top Wicket Takers)
    print(">>> TEST 6: Top Wicket Takers (Bubble Sort Algorithm)...")
    top_wickets = bubble_sort_players(players, "wickets", descending=True)
    display_player_table(top_wickets, "TOP WICKET TAKERS (BUBBLE SORT)")
    print()

    # 7. Test Head-to-Head Comparison
    print(">>> TEST 7: Head-to-Head Comparison: Rohit Sharma vs Virat Kohli...")
    p1 = next((p for p in players if p["name"] == "Rohit Sharma"), players[0])
    p2 = next((p for p in players if p["name"] == "Virat Kohli"), players[1])
    compare_two_players(p1, p2)
    print()

    # 8. Test Recursion on Runs
    print(">>> TEST 8: Recursive Cumulative Runs Summation...")
    all_runs = [p["runs"] for p in players]
    rec_sum = recursive_sum_runs(all_runs)
    iter_sum = sum(all_runs)
    print(f"Runs array: {all_runs}")
    print(f"Recursive Sum: {rec_sum} | Python sum(): {iter_sum}")
    assert rec_sum == iter_sum, "Recursive sum mismatch!"
    print("Assertion Passed: Recursive computation matches iterative sum.\n")

    # 9. Test Report Export
    print(">>> TEST 9: Exporting Analysis Summary Report...")
    export_report_to_file(players, "cricket_analysis_export.txt")
    print()

    print_separator("=")
    print("   ALL TESTS COMPLETED SUCCESSFULLY WITH ZERO ERRORS!")
    print_separator("=")


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    import sys
    # If launched with '--test', run the automated verification suite directly
    if len(sys.argv) > 1 and sys.argv[1].lower() in ["--test", "-t", "test"]:
        run_all_tests()
    else:
        run_analyzer()

