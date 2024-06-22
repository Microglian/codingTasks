class Problem():
    def setup(self):
        with open("aoc202301data1.txt", "r") as file:
            self.strings = file.readlines()


    def part1(self):
        total = 0
        for line in self.strings:
            # print(line)
            digits = []
            for char in line:
                if char.isdigit():
                    digits.append(char)
            # print(digits)
            if len(digits) > 0:
                total += int(f"{digits[0]}{digits[-1]}")
        print(f"AOC202301 part 1 answer: {total}")
    
    
    def part2(self):
        total = 0
        words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        
        
    
    def run(self):
        print("running")
        self.setup()
        self.part1()
        self.part2()
        

problem = Problem()

if __name__ == "__main__":
    problem.run()