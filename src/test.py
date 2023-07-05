import unittest
from cleaning_robot import CleaningRobot


class CleaningRobotTest(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test case."""
        self.robot = CleaningRobot(testing_mode=True)

    def test_encounter_inner_and_outer_doors_unlocks_them(self):
        """Test that encountering inner and outer doors unlocks them."""
        self.robot.when_encounter_inner_door()
        self.assertTrue(self.robot.is_door_unlocked())

        self.robot.when_encounter_outer_door()
        self.assertFalse(self.robot.is_door_unlocked())

    def test_does_not_lock_doors_after_unlocking(self):
        """Test that doors are not locked after unlocking them."""
        self.robot.when_encounter_inner_door()
        self.robot.lock_door()
        self.assertFalse(self.robot.is_door_unlocked())

    def test_enters_inner_doors_but_not_outer_door(self):
        """Test that the robot enters inner doors but not the outer door."""
        self.robot.when_encounter_inner_door()
        log = self.robot.enter_door()
        self.assertNotIn("Door entered.", log)

        log = self.robot.when_encounter_outer_door()
        self.assertIn("Door locked.\n", log)

    def test_ignores_prison_guards(self):
        """Test that the robot ignores prison guards."""
        log = self.robot.when_encounter_prisoner()
        self.assertEqual("", log)

        log = self.robot.when_encounter_guard()
        self.assertIn("Turn around.", log)

    def test_encounter_invalid_door_types(self):
        """Test that encountering invalid door types behaves correctly."""
        log = self.robot.when_encounter_inner_door()
        self.assertIn("Door unlocked.\n", log)

        log = self.robot.when_encounter_outer_door()
        self.assertNotIn("Turn around.\n", log)

        log = self.robot.when_encounter_inner_door()
        self.assertIn("Door unlocked.\n", log)

        log = self.robot.when_encounter_inner_door()
        self.assertNotIn("Door entered.", log)

        log = self.robot.when_encounter_outer_door()
        self.assertNotIn("Turn around.\n", log)
        self.assertNotIn("Door entered.", log)

    def test_encounter_unexpected_persons(self):
        """Test that encountering unexpected persons behaves correctly."""
        log = self.robot.when_encounter_prisoner()
        self.assertEqual("", log)

        log = self.robot.when_encounter_guard()
        self.assertIn("Turn around.", log)

        log = self.robot.when_encounter_prisoner()
        self.assertEqual("", log)

    def test_negative_scenario(self):
        """Test a negative scenario."""
        self.assertFalse(self.robot.is_door_unlocked())

        log = self.robot.enter_door()
        self.assertNotIn("Door entered.", log)

        log = self.robot.turn_around()
        self.assertIn("Turn around.", log)

        log = self.robot.lock_door()
        self.assertIn("Door locked.\n", log)

    def test_is_door_unlocked(self):
        """Test the is_door_unlocked method."""
        self.assertFalse(self.robot.is_door_unlocked())

        self.robot.when_encounter_inner_door()
        self.assertTrue(self.robot.is_door_unlocked())

        self.robot.lock_door()
        self.assertFalse(self.robot.is_door_unlocked())

        self.robot.unlock_door()
        self.assertTrue(self.robot.is_door_unlocked())


if __name__ == "__main__":
    unittest.main()
