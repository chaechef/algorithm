from collections import deque
import sys



def solution(arr):
    graph = {}
    graph[1] = set() | set([1])
    print(graph)

if __name__ == "__main__":
    solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])