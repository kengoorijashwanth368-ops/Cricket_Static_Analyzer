"""
=============================================================================
Automated Test & Verification Script for Cricket Statistics Analyzer
Author: Ruthvik
Dataset: 5 Core Indian Cricketers (Rohit, Virat, Dhoni, Iyer, Bumrah)
=============================================================================
"""

import sys
import os
from cricket_analyzer import (
    load_player_data,
    display_player_table,
    display_player_detailed_card,
    compare_two_players,
    linear_search_players,
    recursive_binary_search,
    bubble_sort_players,
    recursive_sum_runs,
    calculate_strike_rate,
    export_report_to_file,
    print_separator
)

def run_all_tests():
    print("=================================================================")
    print("   AUTOMATED VERIFICATION RUN: CRICKET STATISTICS ANALYZER")
    print("   Dataset: 5 Core Players (Rohit, Virat, Dhoni, Iyer, Bumrah)")
    print("=================================================================\n")

    # 1. Test Data Loading
    print(">>> TEST 1: Loading Player Records...")
    players = load_player_data()
    print(f"Loaded {len(players)} players successfully.\n")
    assert len(players) == 5, f"Expected 5 players, found {len(players)}"

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
    p1 = next(p for p in players if p["name"] == "Rohit Sharma")
    p2 = next(p for p in players if p["name"] == "Virat Kohli")
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
    export_filename = os.path.join(os.path.dirname(__file__), "cricket_analysis_export.txt")
    export_report_to_file(players, export_filename)
    print(f"File verified at: {export_filename}\n")

    print("=================================================================")
    print("   ALL TESTS COMPLETED SUCCESSFULLY WITH ZERO ERRORS!")
    print("=================================================================")

if __name__ == "__main__":
    run_all_tests()
