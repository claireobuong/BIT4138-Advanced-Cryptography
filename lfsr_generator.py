def lfsr(seed, taps, length):
    state = seed[:]
    seen_states = {}
    sequence = []

    for i in range(length):
        state_str = ''.join(str(bit) for bit in state)

        # Detect repeated states
        if state_str in seen_states:
            period = i - seen_states[state_str]
            print("\nRepeated State Detected!")
            print("State:", state_str)
            print("Estimated Sequence Period:", period)
            break

        seen_states[state_str] = i

        # Output bit
        sequence.append(state[-1])

        # XOR feedback
        feedback = 0
        for tap in taps:
            feedback ^= state[tap]

        # Shift register
        state = [feedback] + state[:-1]

    print("\nGenerated Sequence:")
    print(sequence)

    print("\nWeakness Analysis:")
    if len(seen_states) < length:
        print("- Sequence repetition detected.")
        print("- Short periods reduce cryptographic security.")
        print("- Predictable states make attacks easier.")
    else:
        print("- No repetition detected within the test length.")
        print("- Higher unpredictability observed.")


# Initial 4-bit seed
seed = [1, 0, 1, 1]

# Tap positions (0-based indexing)
taps = [0, 2]

# Number of bits to generate
length = 20

lfsr(seed, taps, length)