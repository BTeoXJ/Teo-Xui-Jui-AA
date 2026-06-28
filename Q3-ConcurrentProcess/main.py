from experiments import (
    run_multithreading_experiment,
    run_sequential_experiment,
    display_factorial_summary
)

def main():
    print("==============================================")
    print(" FACTORIAL MULTITHREADING PERFORMANCE TEST")
    print("==============================================")

    threaded_results, threaded_times, threaded_average = \
        run_multithreading_experiment()

    display_factorial_summary(threaded_results)

    sequential_results, sequential_times, sequential_average = \
        run_sequential_experiment()

    display_factorial_summary(sequential_results)

    print("\n========== FINAL COMPARISON ==========")
    print(f"Average Multithreading Time: {threaded_average:,.2f} ns")
    print(f"Average Sequential Time    : {sequential_average:,.2f} ns")

    if threaded_average < sequential_average:
        print("Result: Multithreading was faster in this experiment.")
    else:
        print("Result: Sequential processing was faster in this experiment.")

if __name__ == "__main__":
    main()

