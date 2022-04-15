class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        # Base Case
        if source == target:
            return 0
        
        # Creating graph or routes
        graph = defaultdict(set)
        
        # Since index represents bus_number on a route, suppose i is the bus number 
        # and stops are the values present at that index
        
        for bus_number, stops in enumerate(routes):
            #print(bus_number, stops)
            for stop in stops:
                graph[stop].add(bus_number)
        #print(graph)
        
        #Using BFS
        bfs = deque([(source, 0)])
        
        # Visited Stops
        seen_stops = set()
        
        #Visited Buses
        seen_buses = set()
        
        while bfs:
            stop, count = bfs.popleft()
            if stop == target:
                return count
            
            for bus_number in graph[stop]:
                if bus_number not in seen_buses:
                    seen_buses.add(bus_number)
                    
                    for stop in routes[bus_number]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            bfs.append((stop, count + 1))
        return -1