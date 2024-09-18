# Subsystem classes
class DVDPlayer:
    def on(self):
        print("DVD Player is ON")

    def play(self, movie):
        print(f"Playing movie: {movie}")

    def off(self):
        print("DVD Player is OFF")


class Amplifier:
    def on(self):
        print("Amplifier is ON")

    def set_volume(self, level):
        print(f"Amplifier volume set to {level}")

    def off(self):
        print("Amplifier is OFF")


class Projector:
    def on(self):
        print("Projector is ON")

    def wide_screen_mode(self):
        print("Projector set to Widescreen mode")

    def off(self):
        print("Projector is OFF")


# Facade class
class HomeTheaterFacade:
    def __init__(self, dvd_player, amplifier, projector):
        self.dvd_player = dvd_player
        self.amplifier = amplifier
        self.projector = projector

    def watch_movie(self, movie):
        print("Setting up home theater to watch a movie...")
        self.projector.on()
        self.projector.wide_screen_mode()

        self.amplifier.on()
        self.amplifier.set_volume(5)

        self.dvd_player.on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print("Shutting down the home theater...")
        self.dvd_player.off()
        self.amplifier.off()
        self.projector.off()


# Client code
if __name__ == "__main__":
    # Create subsystem objects
    dvd = DVDPlayer()
    amp = Amplifier()
    proj = Projector()

    # Create the facade
    home_theater = HomeTheaterFacade(dvd, amp, proj)

    # Use the facade to control the complex subsystem
    home_theater.watch_movie("Inception")
    print("\n")
    home_theater.end_movie()
