# Stack Implementation for MoMo Transaction History
def momo_transaction_stack():
    """
    Simulates MoMo transaction stack where steps are pushed and undone (popped)
    """
    # Initialize empty stack for MoMo transactions
    momo_stack = []
    
    # Push transaction steps onto the stack
    momo_stack.append("Step1")
    momo_stack.append("Step2") 
    momo_stack.append("Step3")
    
    print("Initial MoMo transaction stack:")
    print(momo_stack)
    print(f"Top of stack: {momo_stack[-1]}")
    print()
    
    # Undo one step (pop the last element)
    undone_step = momo_stack.pop()
    print(f"Undid: {undone_step}")
    print("Stack after undo:")
    print(momo_stack)
    print(f"Step left on top: {momo_stack[-1]}")
    
    return momo_stack[-1]  # Return the step left on top

# Execute and display results
print("=" * 50)
print("MOCO TRANSACTION STACK SIMULATION")
print("=" * 50)
result1 = momo_transaction_stack()
print("=" * 50)


# Stack Implementation for UR Student Lectures
def ur_lecture_stack():
    """
    Simulates UR student lecture stack where lectures are pushed and multiple undos performed
    """
    # Initialize empty stack for lectures
    lecture_stack = []
    
    # Push lectures onto the stack
    lecture_stack.append("Lecture1")
    lecture_stack.append("Lecture2")
    lecture_stack.append("Lecture3")
    
    print("Initial UR lecture stack:")
    print(lecture_stack)
    print(f"Top of stack: {lecture_stack[-1]}")
    print()
    
    # Undo two lectures (pop twice)
    first_undo = lecture_stack.pop()
    second_undo = lecture_stack.pop()
    
    print(f"Undid: {first_undo}")
    print(f"Undid: {second_undo}")
    print("Stack after 2 undos:")
    print(lecture_stack)
    
    if lecture_stack:
        print(f"Lecture on top: {lecture_stack[-1]}")
        return lecture_stack[-1]
    else:
        print("Stack is empty!")
        return None

# Execute and display results
print("\n" + "=" * 50)
print("UR LECTURE STACK SIMULATION")
print("=" * 50)
result2 = ur_lecture_stack()
print("=" * 50)

# Challenge: Complete Stack Operations
def stack_challenge():
    """
    Challenge: Push elements, then pop all, and see what remains
    """
    # Initialize stack
    challenge_stack = []
    
    # Algorithm Step 1: Push three elements
    print("Step 1: Pushing elements A, B, C onto stack")
    challenge_stack.append("A")  # Push A
    challenge_stack.append("B")  # Push B  
    challenge_stack.append("C")  # Push C
    print(f"Stack after pushes: {challenge_stack}")
    print()
    
    # Algorithm Step 2: Pop all elements
    print("Step 2: Popping all elements from stack")
    while challenge_stack:  # Continue until stack is empty
        popped_element = challenge_stack.pop()
        print(f"Popped: {popped_element}")
    
    # Algorithm Step 3: Check what remains
    print("\nStep 3: Checking stack contents")
    print(f"Stack after popping all: {challenge_stack}")
    
    if not challenge_stack:
        print("RESULT: Stack is empty - no elements left")
        return "Empty"
    else:
        print(f"RESULT: {len(challenge_stack)} elements remain")
        return challenge_stack

# Execute challenge
print("\n" + "=" * 50)
print("STACK CHALLENGE: PUSH A,B,C THEN POP ALL")
print("=" * 50)
challenge_result = stack_challenge()
print("=" * 50)

# Queue Implementation for Nyabugogo Buses
def nyabugogo_bus_queue():
    """
    Simulates bus queue at Nyabugogo taxi park with FIFO principle
    """
    from collections import deque
    
    # Initialize queue for buses
    bus_queue = deque()
    
    # Add 9 buses to the queue (Bus1 through Bus9)
    for i in range(1, 10):
        bus_queue.append(f"Bus{i}")
    
    print("Initial Nyabugogo bus queue:")
    print(list(bus_queue))
    print(f"Front of queue: {bus_queue[0]}")
    print(f"Number of buses: {len(bus_queue)}")
    print()
    
    # Algorithm: 6 buses depart (dequeue 6 times)
    print("Departing 6 buses...")
    for i in range(6):
        departed_bus = bus_queue.popleft()
        print(f"Departed: {departed_bus}")
    
    print("\nQueue after 6 departures:")
    print(list(bus_queue))
    
    if bus_queue:
        print(f"Front bus now: {bus_queue[0]}")
        return bus_queue[0]
    else:
        print("Queue is empty!")
        return None

# Execute bus queue simulation
print("\n" + "=" * 50)
print("NYABUGOGO BUS QUEUE SIMULATION")
print("=" * 50)
bus_result = nyabugogo_bus_queue()
print("=" * 50)

# Challenge: Queue vs Stack for Service Tickets
def service_ticket_system():
    """
    Analysis of why queue is better than stack for service ticket systems
    """
    print("ANALYSIS: Queue vs Stack for Service Tickets")
    print("=" * 50)
    
    # Algorithm Step 1: Understand the service requirement
    print("Step 1: Service ticket systems require FAIRNESS")
    print("   - First come, first served principle")
    print("   - Customers expect to be served in arrival order")
    print()
    
    # Algorithm Step 2: Queue implementation (CORRECT approach)
    print("Step 2: Queue Implementation (FIFO - First In First Out)")
    print("   - enqueue(): New tickets added to the end")
    print("   - dequeue(): Oldest tickets served first")
    print("   - Ensures chronological order is maintained")
    print()
    
    # Algorithm Step 3: Stack implementation (WRONG approach)
    print("Step 3: Stack Implementation (LIFO - Last In First Out)")
    print("   - push(): New tickets added to the top") 
    print("   - pop(): Newest tickets served first")
    print("   - Violates fairness: latecomers get served first")
    print()
    
    # Algorithm Step 4: Comparative demonstration
    print("Step 4: Practical Demonstration")
    
    # Queue example
    from collections import deque
    queue_tickets = deque()
    queue_tickets.append("Ticket1@09:00")
    queue_tickets.append("Ticket2@09:05") 
    queue_tickets.append("Ticket3@09:10")
    
    print("   Queue system serves:", queue_tickets.popleft())  # Correct: Ticket1 first
    
    # Stack example (problematic)
    stack_tickets = []
    stack_tickets.append("Ticket1@09:00")
    stack_tickets.append("Ticket2@09:05")
    stack_tickets.append("Ticket3@09:10")
    
    print("   Stack system serves:", stack_tickets.pop())  # Wrong: Ticket3 first!
    print()
    
    # Algorithm Step 5: Conclusion
    print("Step 5: Conclusion")
    print("   ✓ QUEUE is correct for service tickets")
    print("   ✗ STACK would cause customer dissatisfaction")
    print("   ✓ FIFO ensures fairness and proper ordering")
    
    return "Queue is the right choice"

# Execute the analysis
print("\n" + "=" * 50)
print("SERVICE TICKET SYSTEM ANALYSIS")
print("=" * 50)
ticket_analysis = service_ticket_system()
print("=" * 50)