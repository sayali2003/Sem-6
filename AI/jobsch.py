def sort_jobs_by_deadline(job):
    return job[1]

def jobScheduling():
    jobs = []
    n = int(input("Enter the number of jobs: "))

    for i in range(n):
        job_id = int(input("Enter job ID: ")
        deadline = int(input("Enter deadline for job: "))
        profit = int(input("Enter profit for job: "))
        jobs.append((job_id, deadline, profit))

    # Sort jobs based on their deadlines in descending order
    jobs.sort(key=sort_jobs_by_deadline, reverse=True)

    max_deadline = max(jobs, key=sort_jobs_by_deadline)[1]
    schedule = [-1] * (max_deadline + 1)
    total_profit = 0

    for job in jobs:
        deadline = job[1]
        while schedule[deadline] != -1 and deadline > 0:
            deadline -= 1

        if schedule[deadline] == -1:
            schedule[deadline] = job[0]
            total_profit += job[2]

    result = [job for job in schedule if job != -1]

    return result, total_profit

# Example usage:
scheduled_jobs, total_profit = jobScheduling()

print("Scheduled Jobs:", scheduled_jobs)
print("Total Earned Profit:", total_profit)

