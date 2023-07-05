# Test Driven Development in a prison

In this exercise, we'll be looking at the basic test driven development in a prison setting.

You are an inmate in Germany's largest prison Bielefeld-Senne. You cannot wait to leave and you have
tried to do everything possible to break out. Nothing worked so far, but today you have finally
been able to break into the prison's cleaning robot main harddrive and you are now able to reprogram it.

The robot only visits your room once a day and you then need to change its programming. You really want
to make sure that your program will work well, so you want to make sure to use test-driven development
for writing the program.

**What you need to do:**
1. Write your tests. In the file `src/test.py`, initiate the `CleaningRobot` class in testing mode. Add
tests to make sure that:
- When it encounters an inner or outer door, it unlocks it.
- It does not lock doors after unlocking them.
- It enters inner doors but it does not enter the outer door.
- It ignores prison guards.

2. Then modify `src/cleaning_robot.py` so that all the tests pass and running `src/test.py` outputs the
line "All tests ran successfully.".

**Note:** There is an internal `src/motor.py` file in the cleaning robots system that you do not have
access to. The file you can see here is a file you have created for testing purposes on your laptop.
You do not need to modify it.
