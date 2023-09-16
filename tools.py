def make_email_title(event_name: str, proximity: str) -> str:
    """
    Generates a title for a reminder email.
    """
    return f'Your event {event_name} is beginning {proximity}!'


def make_email_body(commentary: str) -> str:
    """
    Genearates a body text for a reminder email.
    """
    base = (f"\nYou are recieving this message because you have set a reminder in the Reminder app.")
    if commentary:
        return (base +
                f"\nEvent comment:\n{commentary}")
    return base