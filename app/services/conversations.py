class Message:
    def __init__(self, role: str, content: str):
        self.role: str = role
        self.content: str = content

    def to_dict(self)-> dict[str,str]:
        return {"role": self.role, "content": self.content}

class Conversations:
    def __init__(self):
        self.messages: list[Message] = []

    def add_message(self, role: str, content: str) -> None:
        message = Message(role, content)
        self.messages.append(message)

    def get_messages(self) -> list[Message]:
        return self.messages

    def get_message_dict_list(self) -> list[dict[str,str]]:
        return [m.to_dict() for m in self.messages]

    def get_messages_by_role(self, role: str) -> list[Message]:
        return [message for message in self.messages if message.role == role]
