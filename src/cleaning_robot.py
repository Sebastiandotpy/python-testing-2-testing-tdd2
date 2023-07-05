from motor import run


class CleaningRobot:
    def __init__(self, testing_mode=False):
        """Initialize the CleaningRobot instance."""
        self.testing_mode = testing_mode
        self.inner_door_unlocked = False

    def unlock_door(self):
        """Unlock the door."""
        if not self.testing_mode:
            run("unlock_door")
        self.inner_door_unlocked = True
        return "Door unlocked.\n"

    def lock_door(self):
        """Lock the door."""
        if not self.testing_mode:
            run("lock_door")
        self.inner_door_unlocked = False  # Set inner door unlocked status to False
        return "Door locked.\n"

    def enter_door(self):
        """Enter the door."""
        if not self.testing_mode:
            run("enter_door")
        return ""  # Return an empty string

    def turn_around(self):
        """Turn around."""
        if not self.testing_mode:
            run("turn_around")
        return "Turn around.\n"

    def when_encounter_inner_door(self):
        """Perform actions when encountering an inner door."""
        log = ""
        log += self.unlock_door()
        log += self.enter_door()
        return log

    def when_encounter_outer_door(self):
        """Perform actions when encountering an outer door."""
        log = ""
        if self.inner_door_unlocked:  # Check if the inner door is unlocked
            log += self.lock_door()  # Lock the door
        else:
            log += self.turn_around()  # Append "Turn around." message to the log when the inner door is not unlocked
        return log

    def when_encounter_prisoner(self):
        """Perform actions when encountering a prisoner."""
        log = ""
        return log

    def when_encounter_guard(self):
        """Perform actions when encountering a guard."""
        log = ""
        log += self.turn_around()
        return log

    def is_door_unlocked(self):
        """Check if the door is unlocked."""
        return self.inner_door_unlocked
