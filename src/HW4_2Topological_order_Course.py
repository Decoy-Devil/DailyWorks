from collections import deque  # importing deque to use as a queue for BFS (fast pop from left)


def find_course_order(n, prerequisites):
    # n = number of courses labeled 0 to n-1
    # prerequisites = list of [course, pre] pairs meaning: pre must be taken before course
    # return: a valid ordering list of courses, or [] if impossible

    adj = [[] for _ in range(n)]  # adj[pre] will store courses unlocked after taking pre
    indegree = [0] * n  # indegree[c] = number of prerequisites course c still needs

    for course, pre in prerequisites:  # read each prerequisite relation
        adj[pre].append(course)  # add directed edge pre -> course
        indegree[course] += 1  # course now has one more prerequisite

    q = deque()  # queue for courses ready to take (indegree 0)
    for c in range(n):  # check every course
        if indegree[c] == 0:  # if it has no prerequisites
            q.append(c)  # it can be taken immediately

    order = []  # this will store the final course ordering

    while q:  # while there are still available courses
        cur = q.popleft()  # take one available course
        order.append(cur)  # add it to the ordering

        for nxt in adj[cur]:  # for each course that depends on cur
            indegree[nxt] -= 1  # remove cur as a prerequisite
            if indegree[nxt] == 0:  # if nxt now has no remaining prerequisites
                q.append(nxt)  # nxt becomes available to take

    # if we were able to schedule all courses, return the ordering
    if len(order) == n:  # all courses included => no cycle
        return order  # return any valid ordering
    else:
        return []  # cycle exists => impossible to finish all courses


from collections import deque  # importing deque to use as a queue for BFS (fast pop from left)

def topo_order_or_cycle(num_courses, prerequisites):
    # num_courses = total number of courses (0 to num_courses-1)
    # prerequisites = list of pairs [course, pre] meaning pre must be done before course

    # Create adjacency list: adj[pre] will store the courses unlocked after finishing 'pre'
    adj = [[] for _ in range(num_courses)]  # making empty neighbor lists for each course

    # Create indegree list: indegree[c] counts how many prerequisites course c has
    indegree = [0] * num_courses  # initially assume no prerequisites for any course

    # Build graph and indegree counts
    for course, pre in prerequisites:     # loop over each prerequisite pair
        adj[pre].append(course)           # add directed edge: pre -> course
        indegree[course] += 1             # course needs one more prerequisite

    # Queue for all courses that currently have indegree 0 (can be taken immediately)
    q = deque()                           # create empty queue
    for c in range(num_courses):          # check every course
        if indegree[c] == 0:              # if no prerequisites
            q.append(c)                   # push into queue

    order = []                            # this will store the topological ordering (valid course order)

    # Process courses in BFS manner
    while q:                               # while queue still has courses we can take
        cur = q.popleft()                  # take one available course
        order.append(cur)                  # add it to answer ordering

        # cur is now completed, so it helps unlock its dependent courses
        for nxt in adj[cur]:               # go through all courses that depend on cur
            indegree[nxt] -= 1             # remove one prerequisite requirement
            if indegree[nxt] == 0:         # if nxt has no more prerequisites left
                q.append(nxt)              # it becomes available

    # If we scheduled all courses, ordering is valid
    if len(order) == num_courses:          # all courses processed
        return True, order                 # possible + return one valid ordering
    else:
        return False, []                   # impossible because of a cycle


if __name__ == "__main__":
    # ----- Input section (you type values, not hardcoded) -----

    num_courses = int(input("Enter number of courses: "))  # read total courses

    m = int(input("Enter number of prerequisite pairs: "))  # read how many pairs follow

    prerequisites = []                                      # list to store pairs
    for _ in range(m):                                      # repeat m times
        course, pre = map(int, input("Enter course pre: ").split())  # read two ints
        prerequisites.append([course, pre])                 # store the pair

    possible, order = topo_order_or_cycle(num_courses, prerequisites)  # run topo algorithm

    print("Possible:", possible)                             # print whether scheduling is possible
    if possible:
        print("One valid order:", order)                     # print one valid order if exists