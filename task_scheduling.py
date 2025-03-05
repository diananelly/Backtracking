import heapq


def schedule_tasks(tasks, K):
    # step 1: sort tasks by start time
    tasks.sort(key=lambda x: x["start"])

    # step 2: initialize the priority queue and the resource assignment map
    resources = []  # priority queue to manage resource availability
    resource_assignment = {}

    # step 3: iterate through the tasks
    for task in tasks:
        # check if we have a resource that becomes available before the task starts
        while resources and resources[0][0] <= task["start"]:
            heapq.heappop(resources)  # resource becomes free

        # step 4: if no resources are available, and we already used K resources, fail
        if len(resources) >= K:
            return "Failure"

        # assign the task a resource (i.e., a test machine)
        resource_id = len(resources) + 1  # new resource ID
        resource_assignment[task["task_id"]] = resource_id

        # step 5: push the resource with its updated availability time into the queue
        heapq.heappush(resources, (task["end"], resource_id))

    return resource_assignment


# example tasks
tasks = [
    {"task_id": 1, "start": 9, "end": 11, "resource_needed": 1},
    {"task_id": 2, "start": 10, "end": 12, "resource_needed": 1},
    {"task_id": 3, "start": 12, "end": 14, "resource_needed": 1},
    {"task_id": 4, "start": 11, "end": 13, "resource_needed": 1},
]
K = 2
tasks1 = [
    {"task_id": 1, "start": 4, "end": 11, "resource_needed": 1},
    {"task_id": 2, "start": 5, "end": 12, "resource_needed": 1},
    {"task_id": 3, "start": 11, "end": 13, "resource_needed": 1},
    {"task_id": 4, "start": 12, "end": 14, "resource_needed": 1},
    {"task_id": 5, "start": 13, "end": 15, "resource_needed": 1},
    {"task_id": 6, "start": 10, "end": 16, "resource_needed": 1},
    {"task_id": 7, "start": 1, "end": 6, "resource_needed": 1},
    {"task_id": 8, "start": 15, "end": 17, "resource_needed": 1},
    {"task_id": 9, "start": 16, "end": 18, "resource_needed": 1},
    {"task_id": 10, "start": 14, "end": 16, "resource_needed": 1},
]

K1 = 3  # number of available test machines (resources)


# call the scheduler function
result = schedule_tasks(tasks, K)
result1 = schedule_tasks(tasks1, K1)

if result == "Failure":
    print("Failure: Not enough resources to schedule all tasks.")
else:
    print("Task Assignments:")
    for task_id, resource_id in result.items():
        print(f"Task {task_id}: Resource {resource_id}")

if result1 == "Failure":
    print("Failure: Not enough resources to schedule all tasks.")
else:
    print("Task Assignments:")
    for task_id, resource_id in result1.items():
        print(f"Task {task_id}: Resource {resource_id}")
