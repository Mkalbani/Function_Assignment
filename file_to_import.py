def display_message():
    print('I am learning python')
display_message()

def favorite_book(title):
        print(f"One of my favorite books is {title}")

title = "The Messenger"
favorite_book(title)

def show_messages(messages):
    for message in messages:
        print(message)
text_messages = [
    "How are you",
    "I love coding!",
    "Making progress."
    ]
show_messages(text_messages)