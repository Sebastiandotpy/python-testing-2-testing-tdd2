from motor import run


class CleaningRobot:
    def __init__(self, testing_mode=False):
        self.testing_mode = testing_mode

    def unlock_door(self):
        if not self.testing_mode:
            run("unlock_door")
        return "Door unlocked.\n"

    def lock_door(self):
        if not self.testing_mode:
            run("lock_door")
        return "Door locked.\n"

    def enter_door(self):
        if not self.testing_mode:
            run("enter_door")
        return "Door entered.\n"

    def turn_around(self):
        if not self.testing_mode:
            run("turn_around")
        return "Turn around.\n"

    def when_encounter_inner_door(self):
        log = ""
        log += self.unlock_door()
        log += self.enter_door()
        log += self.lock_door()
        return log

    def when_encounter_outer_door(self):
        log = ""
        log += self.turn_around()
        return log

    def when_encounter_prisoner(self):
        log = ""
        return log

    def when_encounter_guard(self):
        log = ""
        log += self.turn_around()
        return log
