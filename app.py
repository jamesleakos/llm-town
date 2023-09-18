import sys
from prompts import chaining_prompts

if __name__ == "__main__":
    user_message_1 = f"""
      tell me about the smartx pro phone and \
      the fotosnap camera, the dslr one. \
      Also tell me about your tvs """

    if len(sys.argv) >= 2:
        user_message_1 = sys.argv[1]
    else:
        print("Using default prompt: ", user_message_1, "\n")

    print(chaining_prompts.customer_service_bot(user_message_1))
