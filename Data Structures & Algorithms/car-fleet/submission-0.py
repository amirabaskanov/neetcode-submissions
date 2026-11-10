class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        fleets = []

        for item in sorted(cars)[::-1]:
            fleets.append((target - item[0]) / item[1])
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()

        return len(fleets)
        


        

        