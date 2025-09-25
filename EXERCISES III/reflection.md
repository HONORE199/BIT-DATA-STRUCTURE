Reflection Questions (Theoretical Discussion Only)
Stack Reflection:
Why stack ensures last changes are reversed first?

Stacks follow the LIFO (Last-In-First-Out) principle, which means the most recently added element is the first one to be removed. This behavior is fundamental to stack data structure design. When we "undo" operations in applications like MoMo transactions or text editors, the stack perfectly mirrors the natural workflow where users typically want to reverse their most recent actions first. The sequential nature of stack operations (push/pop) directly maps to chronological task execution, making it ideal for scenarios requiring reverse chronological processing.

Queue Reflection:
Why FIFO prevents disputes in services?

FIFO (First-In-First-Out) principle inherent in queues ensures absolute fairness in service systems. By guaranteeing that the first person to arrive is the first to be served, queues eliminate ambiguity and prevent disputes over service order. This objective, timestamp-based processing creates a transparent system where service order is determined solely by arrival time rather than subjective factors. In public service contexts like bus stations or government offices, FIFO provides an indisputable, verifiable sequence that maintains social order and customer trust.