from classes.actor import Actor

if __name__ == "__main__":
    # Define two actors
    alice = Actor("Alice", "friendly", "likes to count", "wants to count")
    bob = Actor("Bob", "curious", "likes to count", "wants to count")

    # Initial conversation
    conversation = []

    # Main loop
    for i in range(12):  # Let's make them talk back and forth for 5 turns
        print(f"Turn {i}")
        if i % 2 == 0:  # Alice's turn to talk
            response = alice.prompt(bob, conversation)
            conversation.append(f"""Alice: {response}""")
            print("Alice: ", response)
        else:  # Bob's turn to talk
            response = bob.prompt(alice, conversation)
            conversation.append("Bob: " + response)
            print("Bob: ", response)

    # Print the final conversation
    print("Final conversation:")
    print(conversation)
