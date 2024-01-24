from random import randint
from tank_game_highscores import hs_archive

class TankGame:
    def __init__(self, N: int = 7):
        """Create a tank game object.

        :param N: the size of the map (grid) NxN to generate for the game.
        """
        self.N = N
        # Hard-coded starting tank location is 2, 1
        self.tank_loc_x = 2
        self.tank_loc_y = 1
        self.face = "north"
        self.shots_north = 0
        self.shots_west = 0
        self.shots_east = 0
        self.shots_south = 0
        self.enemy_x = randint(0,6)
        self.enemy_y = randint(0,6)
        self.points = 100
        self.hits = 0
        self.your_name = ""
        self.high_scores = {}

    def print_map(self):
        """Print the current map of the game.

        Example output for a 7x7 map:
           0  1  2  3  4  5  6
        0  .  .  .  .  .  .  .
        1  .  .  T  .  .  .  .
        2  .  .  .  .  .  .  .
        3  .  .  .  .  .  .  .
        4  .  .  .  .  .  .  .
        5  .  .  .  .  .  .  .
        6  .  .  .  .  .  .  .

        where T is the location of the tank,
        where . (the dot) is an empty space on the map,
        where the horizontal axis is the x location of the tank and,
        where the vertical axis is the y location of the tank.
        """
        # Print the numbers for the x axis
        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for index, i in enumerate(range(self.N)):
            if index == 6:
                print(f"{i} ", end="")
                # using enumerate, to add ending to the last position of loop.
                # so i can have points printed next to the game grid (as exercise requires).
                # Edit. not the best way to print it like that
                # And i have changed T symbol to ↑, and made it turn according to tank's facing

                for ind, j in enumerate(range(self.N)):
                    if self.tank_loc_x == j and self.tank_loc_y == i and self.face == "east":
                        if j == 6 and i == 6:
                            print(" → ", end="Points: ")
                            print(self.points)
                        else:
                            print(" → ", end="")
                    elif self.tank_loc_x == j and self.tank_loc_y == i and self.face == "west":
                        if j == 6 and i == 6:
                            print(" ← ", end="Points: ")
                            print(self.points)
                        else:
                            print(" ← ", end="")
                    elif self.tank_loc_x == j and self.tank_loc_y == i and self.face == "north":
                        if j == 6 and i == 6:
                            print(" ↑ ", end="Points: ")
                            print(self.points)
                        else:
                            print(" ↑ ", end="")
                    elif self.tank_loc_x == j and self.tank_loc_y == i and self.face == "south":
                        if j == 6 and i == 6:
                            print(" ↓ ", end="Points: ")
                            print(self.points)
                        else:
                            print(" ↓ ", end="")
                    elif self.enemy_x == j and self.enemy_y == i:
                        if j == 6 and i == 6:
                            print(" X ", end="Points: ")
                            print(self.points)
                        else:
                            print(" X ", end="")
                    elif ind == 6:
                        print(" . ", end="Points: ")
                        print(self.points)
                    else:
                        print(" . ", end="")
                        # I should not have print points here that way (line 66).
                        # Because it makes my future updates more difficult.
                        # I didn't think of it at start, so i'll leave it like it is.
                        # Print line bellow is more for testing things out as well.
                print("|---------------------|-----------|")
            else:
                print(f"{i} ", end="")
                for j in range(self.N):
                    if self.tank_loc_x == j and self.tank_loc_y == i and self.face == "east":
                        print(" → ", end="")
                    elif self.tank_loc_x == j and self.tank_loc_y == i and self.face == "west":
                        print(" ← ", end="")
                    elif self.tank_loc_x == j and self.tank_loc_y == i and self.face == "north":
                        print(" ↑ ", end="")
                    elif self.tank_loc_x == j and self.tank_loc_y == i and self.face == "south":
                        print(" ↓ ", end="")
                    elif self.enemy_x == j and self.enemy_y == i:
                        print(" X ", end="")
                    else:
                        print(" . ", end="")
                print()
    def left(self):
        if self.face == "north":
            self.face = "west"
        elif self.face == "west":
            self.face = "south"
        elif self.face == "south":
            self.face = "east"
        elif self.face == "east":
            self.face = "north"

    def right(self):
        if self.face == "north":
            self.face = "east"
        elif self.face == "east":
            self.face = "south"
        elif self.face == "south":
            self.face = "west"
        elif self.face == "west":
            self.face = "north"

    # while moving, forward, if my tank tries to go through the edge, it will spawn on another side.
    def forward(self):
        self.points -= 10
        if self.face == "north":
            self.tank_loc_y -= 1
            if self.tank_loc_y == -1:
                self.tank_loc_y = 6
        elif self.face == "south":
            self.tank_loc_y += 1
            if self.tank_loc_y == 7:
                self.tank_loc_y = 0
        elif self.face == "west":
            self.tank_loc_x -= 1
            if self.tank_loc_x == -1:
                self.tank_loc_x = 6
        elif self.face == "east":
            self.tank_loc_x += 1
            if self.tank_loc_x == 7:
                self.tank_loc_x = 0

    # the same as moving forward, it takes -10 points as well.
    def backward(self):
        self.points -= 10
        if self.face == "north":
            self.tank_loc_y += 1
            if self.tank_loc_y == 7:
                self.tank_loc_y = 0
        elif self.face == "south":
            self.tank_loc_y -= 1
            if self.tank_loc_y == -1:
                self.tank_loc_y = 6
        elif self.face == "west":
            self.tank_loc_x += 1
            if self.tank_loc_x == 7:
                self.tank_loc_x = 0
        elif self.face == "east":
            self.tank_loc_x -= 1
            if self.tank_loc_x == -1:
                self.tank_loc_x = 6

    # if my tank goes on the top of the target, it gets a hint to move away (optional feature).
    def exact_loc(self):
        if self.enemy_x == self.tank_loc_x and self.enemy_y == self.tank_loc_y:
            print("You are over the target, it is too close to shoot, move next to it")


    def info(self):
        shots_total = (sum([self.shots_north + self.shots_west + self.shots_east + self.shots_south]))
        print(f"Info: your tank is facing -{self.face}-, x = {self.tank_loc_x}, y = {self.tank_loc_y}")
        print (f"Total shots fired: {shots_total} (north: {self.shots_north}, "
               f"west: {self.shots_west}, east: {self.shots_east}, south: {self.shots_south})")
        print(f"↑ - your tank, X - enemy. Total successful Hits: {self.hits}")
        print()

    def shoot(self):
        if self.face == "north":
            self.shots_north += 1
        elif self.face == "west":
            self.shots_west += 1
        elif self.face == "east":
            self.shots_east += 1
        elif self.face == "south":
            self.shots_south += 1

    # my tank must be next to the enemy, and face it to "hit". (calls another function).
    def target_hit(self):
        if (self.enemy_x == self.tank_loc_x
                and (self.enemy_y == self.tank_loc_y + 1 or (self.enemy_y == 0 and self.tank_loc_y == 6))
                and self.face == "south"):
            tg.shot_hit()
        elif (self.enemy_x == self.tank_loc_x
              and (self.enemy_y == self.tank_loc_y - 1 or (self.enemy_y == 6 and self.tank_loc_y == 0))
              and self.face == "north"):
            tg.shot_hit()
        elif (self.enemy_y == self.tank_loc_y
              and (self.enemy_x == self.tank_loc_x + 1 or (self.enemy_x == 0 and self.tank_loc_x == 6))
              and self.face == "east"):
            tg.shot_hit()
        elif (self.enemy_y == self.tank_loc_y
              and (self.enemy_x == self.tank_loc_x - 1 or (self.enemy_x == 6 and self.tank_loc_x == 0))
              and self.face == "west"):
            tg.shot_hit()
        else:
            tg.shot_missed()

    def shot_hit(self):
        print() # these are intentional, i like some spaces, when it prints. More readable.
        print("Hit! You have successfully eliminated the target.")
        self.generate_target()
        self.points += 50
        self.hits += 1

    # missed shots takes 10 points as well in this world.
    def shot_missed(self):
        self.points -= 10
        print("You missed the shot :( You must be next to the target and face it to succeed.")

    def out_of_points(self):
        if self.points < 0:
            print(f"Total successful Hits: {self.hits}.")
            print("You are out of points. Game over!")
            print("Thank you for playing! See you next time!")
            self.end_hs()
            return True


    def generate_target(self):
        self.enemy_x = randint(0,6)
        self.enemy_y = randint(0,6)

    # highscore list is saved in dictionary on another file, so data don't disappear if program is restarted.
    def end_hs(self):
        self.your_name = input("Enter your name to save your score to highscore list: ").upper()
        if self.your_name not in hs_archive:
            hs_archive[self.your_name] = self.hits
            with open('tank_game_highscores.py', 'w') as file:
                file.write(f"hs_archive = {hs_archive}")
        else:
            if hs_archive[self.your_name] <= self.hits:
                hs_archive[self.your_name] = self.hits
                with open('tank_game_highscores.py', 'w') as file:
                    file.write(f"hs_archive = {hs_archive}")
        self.highscore()

    # prints sorted highscore
    def highscore(self):
        sorted_top = sorted(hs_archive.items(), key=lambda item: item[1], reverse=True)
        print("Highscore list:")
        for player, score in sorted_top:
            print(player, "\t", score)

    # Turbo mode. Optional feature. Tank jumps 3 "moves". Costs 40 points.
    # Our playground is "round", so by crossing border, you just arrive to another side.
    def turbomode(self):
        self.points -= 40
        if self.face == "south":
            if self.tank_loc_y + 3 == 7:
                self.tank_loc_y = 0
            elif self.tank_loc_y + 3 == 8:
                self.tank_loc_y = 1
            elif self.tank_loc_y + 3 == 9:
                self.tank_loc_y = 2
            else:
                self.tank_loc_y += 3
        if self.face == "north":
            if self.tank_loc_y - 3 == -1:
                self.tank_loc_y = 6
            elif self.tank_loc_y - 3 == -2:
                self.tank_loc_y = 5
            elif self.tank_loc_y - 3 == -3:
                self.tank_loc_y = 4
            else:
                self.tank_loc_y -= 3
        if self.face == "west":
            if self.tank_loc_x - 3 == -1:
                self.tank_loc_x = 6
            elif self.tank_loc_x - 3 == -2:
                self.tank_loc_x = 5
            elif self.tank_loc_x - 3 == -3:
                self.tank_loc_x = 4
            else:
                self.tank_loc_x -= 3
        if self.face == "east":
            if self.tank_loc_x + 3 == 7:
                self.tank_loc_x = 0
            elif self.tank_loc_x + 3 == 8:
                self.tank_loc_x = 1
            elif self.tank_loc_x + 3 == 9:
                self.tank_loc_x = 2
            else:
                self.tank_loc_x += 3


if __name__ == "__main__":
    # Initialize your game object
    tg = TankGame()

    # Start game loop
    while True:
        tg.print_map()
        tg.info()
        try:
            command = input("Input a command: ")
            # I added error exception here, because i often stop the program and i don't like red errors.
            # And it is nice to practice a bit.
        except KeyboardInterrupt:
            print("Game terminated by user. Run game again.")
            break
        else:
            if command == "l":
                tg.left()
            elif command == "r":
                tg.right()
            elif command == "f":
                tg.forward()
                tg.exact_loc()
                if tg.out_of_points():
                    break
            elif command == "t":  ## new feature. Turbomode. Tank jumps 3 moves (costs 40 points) ##
                tg.turbomode()
                tg.exact_loc()
                if tg.out_of_points():
                    break
            elif command == "b":
                tg.backward()
                tg.exact_loc()
                if tg.out_of_points():
                    break
            elif command == "w":
                tg.shoot()
                tg.target_hit()
                if tg.out_of_points():
                    break
            elif command == "end":
                print("Thank you for playing! See you next time!")
                print()
                tg.end_hs()
                break
            elif command == "top":
                tg.highscore()
            else:
                print()
                print ("Enter right command: l - to steer left, r -  to steer right, f -  to move forward, "
                       "b -  to move backwards, w - to shoot, \nt -turbo mode (tank moves 3x further(costs 40 pts)),  "
                       "top - to see highscore, end - to finsh the game. ")
