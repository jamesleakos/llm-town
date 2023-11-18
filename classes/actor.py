import sys
from utilities.llm_interface import get_completion, get_completion_from_messages


class Actor:
    def __init__(self, name, personality, knowledge, goals):
        self.name = name
        self.personality = personality
        self.knowledge = knowledge
        self.goals = goals

    def prompt(self, other, current_conversation):
        system_message = f"""
          You and a friend are counting. \
          Your name is {self.name}. Your friend's name is {other.name}. \
          You will say one number and then they will say the next \
          number. You will start with the number 1. You will say the next number after your friend \
          says their number. You will keep counting until you reach the number 10.

          Here is the conversation so far: {current_conversation}
        """

        messages = [
            {"role": "system", "content": system_message},
        ]

        response = get_completion(system_message)
        return response
