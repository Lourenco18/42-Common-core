#!/usr/bin/env python3
import time


def game_events(num_events):
    players = ['alice', 'bob', 'charlie']
    events = ['killed monster', 'found treasure', 'leveled up']
    for i in range(1, num_events+1):
        player = players[i % len(players)]
        action = events[i % len(events)]
        yield f"Event {i}: Player {player} ({i % 20 + 1}) {action}"


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


def primes(n):
    found = 0
    num = 2
    while found < n:
        is_prime = all(num % i != 0 for i in range(2, num))
        if is_prime:
            yield num
            found += 1
        num += 1


def main():
    print("=== Game Data Stream Processor ===")
    total_events = 1000
    event_gen = game_events(total_events)

    start_time = time.time()
    high_level = 0
    treasure_events = 0
    levelup_events = 0

    for event in event_gen:
        if "level 10" in event or "level 12" in event:
            high_level += 1
        if "treasure" in event:
            treasure_events += 1
        if "leveled up" in event:
            levelup_events += 1

    end_time = time.time()
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelup_events}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time-start_time:.3f} seconds")

    print("=== Generator Demonstration ===")
    print(
            "Fibonacci sequence (first 10):", ', '.join(str(x) for x in fibonacci(10)))
    print("Prime numbers (first 5):", ', '.join(str(x) for x in primes(5)))


if __name__ == "__main__":
    main()
