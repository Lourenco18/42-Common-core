#!/usr/bin/env python3

def main():
    print("=== Game Analytics Dashboard ===")

    players = ['alice', 'bob', 'charlie', 'diana']
    scores = [2300, 1800, 2150, 2050]
    achievements = {
        'alice': 5,
        'bob': 3,
        'charlie': 7,
        'diana': 4
    }
    player_regions = ['north', 'east', 'central', 'north']

    high_scorers = [p for p, s in zip(players, scores) if s > 2000]
    scores_doubled = [s*2 for s in scores]
    active_players = [p for p in players if p in ['alice', 'bob', 'charlie']]

    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    player_scores = {p: s for p, s in zip(players, scores)}
    score_categories = {
        'high': len([s for s in scores if s > 2000]),
        'medium': len([s for s in scores if 1800 <= s <= 2000]),
        'low': len([s for s in scores if s < 1800])
    }
    achievement_counts = {p: a for p, a in achievements.items()}

    print("=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")

    unique_players = {p for p in players}
    unique_achievements = {a for a in achievements.values()}
    active_regions = {r for r in player_regions}

    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    total_players = len(players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(scores)/len(scores)
    top_index = scores.index(max(scores))
    top_performer = players[top_index]
    print("=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(f"Top performer: {top_performer} ({scores[top_index]} points, {achievements[top_performer]} achievements)")


if __name__ == "__main__":
    main()
