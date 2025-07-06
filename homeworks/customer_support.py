from datetime import datetime

class SupportTicket:
    ticket_counter = 1
    tickets = []

    def __init__(self, title, description):
        self.id = SupportTicket.ticket_counter
        SupportTicket.ticket_counter += 1

        # 🧠 HINT: Store the following as instance attributes:
        # - title (string)
        # - description (string)
        # - status should start as "open"
        # - created_at should use current date/time (formatted as "YYYY-MM-DD HH:MM")
        # - then add this ticket object to SupportTicket.tickets list
        pass # <--- remove me after u finish

    def close_ticket(self):
        # TODO: Raise an Exception if the ticket is already closed
        pass

    def show_info(self):
        print(f"Ticket #{self.id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")
        print(f"Created At: {self.created_at}")
        print("-" * 40)

    @classmethod
    def get_ticket_by_id(cls, ticket_id):
        # TODO: Return the ticket by ID or raise an error if not found
        pass

    def __str__(self):
        # TODO: Return a user-friendly string representation
        pass

    def __repr__(self):
        # TODO: Return a developer-style representation
        pass
