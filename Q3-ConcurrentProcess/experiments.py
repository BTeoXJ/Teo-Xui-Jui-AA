import time
from threading import Thread, Lock
from factorial import calculate_factorial

FACTORIAL_NUMBERS = [50, 100, 200]

def factorial_worker(number, results, timings, lock):
    """Calculates one factorial in a separate thread."""

    start_time = time.perf_counter_ns()
    factorial_result = calculate_factorial(number)
    end_time = time.perf_counter_ns()

    with lock:
        results[number] = factorial_result
        timings[number] = {
            "start": start_time,
            "end": end_time
        }

def run_multithreading_round():
    """Runs 50!, 100!, and 200! using three separate threads."""

    results = {}
    timings = {}
    lock = Lock()

    threads = []

    for number in FACTORIAL_NUMBERS:
        thread = Thread(
            target=factorial_worker,
            args=(number, results, timings, lock),
            name=f"Factorial-{number}"
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    first_start_time = min(timing["start"] for timing in timings.values())
    last_end_time = max(timing["end"] for timing in timings.values())

    total_time = last_end_time - first_start_time

    return results, total_time

def run_sequential_round():
    """Runs 50!, 100!, and 200! one after another without threads."""

    results = {}

    start_time = time.perf_counter_ns()

    for number in FACTORIAL_NUMBERS:
        results[number] = calculate_factorial(number)

    end_time = time.perf_counter_ns()

    total_time = end_time - start_time

    return results, total_time

def run_multithreading_experiment(rounds=10):
    """Runs the multithreading experiment for the required number of rounds."""

    times = []
    final_results = None

    print("\n========== MULTITHREADING EXPERIMENT ==========")
    print("Three threads are created for 50!, 100!, and 200!.\n")

    for round_number in range(1, rounds + 1):
        results, elapsed_time = run_multithreading_round()

        times.append(elapsed_time)
        final_results = results

        print(f"Round {round_number}: {elapsed_time:,} ns")

    average_time = sum(times) / len(times)

    print(f"\nAverage Multithreading Time: {average_time:,.2f} ns")

    return final_results, times, average_time

def run_sequential_experiment(rounds=10):
    """Runs the non-multithreading experiment for the required number of rounds."""

    times = []
    final_results = None

    print("\n========== SEQUENTIAL EXPERIMENT ==========")
    print("50!, 100!, and 200! are calculated one after another.\n")

    for round_number in range(1, rounds + 1):
        results, elapsed_time = run_sequential_round()

        times.append(elapsed_time)
        final_results = results

        print(f"Round {round_number}: {elapsed_time:,} ns")

    average_time = sum(times) / len(times)

    print(f"\nAverage Sequential Time: {average_time:,.2f} ns")

    return final_results, times, average_time

def display_factorial_summary(results):
    """Displays confirmation that all factorial values were calculated."""

    print("\n========== FACTORIAL RESULT SUMMARY ==========")

    for number in FACTORIAL_NUMBERS:
        digit_count = len(str(results[number]))
        print(f"{number}! was calculated successfully. Digits: {digit_count}")




