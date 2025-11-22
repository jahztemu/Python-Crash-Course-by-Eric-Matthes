def show_messages(out):
    """getting text messages"""
    print("Typed messages:")
    for xx in out:
        print(f"Message : {xx}")


messages = [
    "hey dad how was your day?",
    "James i got the new title for the project",
    "I can't go shopping this weekend",
]
show_messages(messages)

print("\n")  # 8.10


def send_messages(out, send):
    """Sending messages to user"""
    while out:
        sending = out.pop()
        send.append(sending)
    print("sending messages...")
    print("This following message was sent:")
    for xx in send:
        print(f" -{xx}")


sent = []
send_messages(messages, sent)


print("\n")  # 8.11
text = [
    "hey dad how was your day?",
    "James i got the new title for the project",
    "I can't go shopping this weekend",
]
texts = text[:]
new_send = []
send_messages(texts, new_send)

print("\n--- Final Lists ---")
print("Original messages")
for message in new_send:
    print(f"- {message}")

print("\nArchived messages:")
for message in text:
    print(f"- {message}")
