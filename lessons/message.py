"""Class to store a message (operator overload, union types, default parameters)"""

class Message:
    
    to: str
    content: str 
    important: bool

    def __init__(self, recipient: str, message_content: str = "", importance_flag: bool = False):
        """Constructs a message."""
        self.to = recipient
        self.content = message_content
        self.important = importance_flag

    def __str__(self) -> str:
        output: str = f"Message to {self.to}:\n"
        output += f"Important? {self.important}\n"
        output += f'"{self.content}"'
        return output
    
    def __mul__(self, factor: int):
        """Multiplication operator overload."""
        copy_val: str = self.content
        for loop_number in range(1, factor):
            self.content += " " + copy_val


msg: Message = Message("erin", "Great job!", False)
msg * 5
print(msg)
msg_to_camila: Message = Message("camila", "You inspire the students")
print(msg_to_camila)

msg: Message = Message("erin", "great job", False)
print(msg)

msg_to_bear: Message = Message("Bear")
print(msg_to_bear)
msg_to_bear.content = "Good boy!" 
msg_to_bear.important = True