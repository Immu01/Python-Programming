import heapq
nums=list(map(int,input("\nEnter numbers separated by spaces = ").split()))
k=int(input("\nEnter the value of k = "))
min_heap=[]
for num in nums:
    heapq.heappush(min_heap,num)
    if len(min_heap)>k:
        heapq.heappop(min_heap)
result=min_heap[0]
print(f"\nOutput= {result}")

# Output
# Enter numbers separated by spaces = 3 2 1 5 6 4
# Enter the value of k = 2
# Output= 5