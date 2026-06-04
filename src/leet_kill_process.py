def killProcess(pid, ppid, kill):
    children = {} # dictionary for children list, key value
    for child, parent in zip(pid, ppid):
        # TODO build children mapping
        pass

    res = []
    queue = [kill]

    while queue:
        cur = queue.pop(0)
        res.append(cur)

        # TODO add children of cur
        queue.append(nxt)
        pass

    return res