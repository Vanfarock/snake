class Event:
    MOVE_UP = "move_up"
    MOVE_DOWN = "move_down"
    MOVE_RIGHT = "move_right"
    MOVE_LEFT = "move_left"
    RESET = "reset"

    def is_move(event: str) -> bool:
        return\
            event == Event.MOVE_UP or\
            event == Event.MOVE_DOWN or\
            event == Event.MOVE_LEFT or\
            event == Event.MOVE_RIGHT

    def are_opposites(current_event: str, last_event) -> bool:
        return\
            current_event == Event.MOVE_UP and last_event == Event.MOVE_DOWN or\
            current_event == Event.MOVE_DOWN and last_event == Event.MOVE_UP or\
            current_event == Event.MOVE_LEFT and last_event == Event.MOVE_RIGHT or\
            current_event == Event.MOVE_RIGHT and last_event == Event.MOVE_LEFT

    def is_reset(event: str) -> bool:
        return event == Event.RESET