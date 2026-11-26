class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        courseMap = defaultdict(list)
        for prereq, course in prerequisites:
            courseMap[course].append(prereq)

        def dfs(course):
            if course not in prereqMap:
                prereqMap[course] = set()
                for prereq in courseMap[course]:
                    prereqMap[course] |= dfs(prereq) #union
                prereqMap[course].add(course)
            return prereqMap[course]
            
        prereqMap = {} #map course -> hashset of indirect prereqs
        for course in range(numCourses):
            dfs(course)
        
        answer = []
        for prereq, course in queries:
            answer.append(prereq in prereqMap[course])
        return answer