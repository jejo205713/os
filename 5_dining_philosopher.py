import threading
import time

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            self.think()
            self.eat()

    def think(self):
        print(f"{self.name} is thinking.")
        time.sleep(1)  # Philosopher is thinking

    def eat(self):
        print(f"{self.name} is hungry.")
        with self.left_fork:
            print(f"{self.name} picked up left fork.")
            with self.right_fork:
                print(f"{self.name} picked up right fork and starts eating.")
                time.sleep(1)  # Philosopher is eating
                print(f"{self.name} has finished eating and put down both forks.")

if __name__ == "__main__":
    # Create 5 forks (locks)
    forks = [threading.Lock() for _ in range(5)]

    # Create 5 philosophers and assign them forks
    philosophers = [Philosopher(f"Philosopher {i+1}", forks[i], forks[(i+1) % 5]) for i in range(5)]

    # Start each philosopher thread
    for philosopher in philosophers:
        philosopher.start()
