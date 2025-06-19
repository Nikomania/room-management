import heapq

"""
Paradigma de projeto de algoritmos utilizado:
é empregado um algoritmo guloso (greedy) na variante de interval partitioning. 
No início, é ordenado as reuniões pelo horário de início; 
Em seguida, para cada reunião, liberamos (heap pop) todas as salas cujo término
é <= início atual e, então, ocupa-se uma sala (heap push) com o término da reunião. Se não houver sala disponível, a heap cresce, alocando uma sala adicional.

Complexidade:

* ordenação dos n intervalos: O(n log n)
* para cada reunião, até uma remoção e uma inserção na heap: O(log n) cada
  → total O(n log n).

Justificativa gulosa:
A cada passo, a decisão local é “reusar a sala que liberta mais cedo” (menor término na heap). 
Essa escolha não prejudica alocações futuras, pois maximiza a chance de haver salas livres nos próximos intervalos, levando a um número global mínimo de salas.
"""

def time_to_minutes(time_str):
    hours, minutes = time_str.split(':')
    return int(hours) * 60 + int(minutes)

def main():
    meetings = []
    
    n = int(input("number of meetings: "))
    for i in range(n):
        meeting_id = input(f"meeting {i+1} ID: ")
        start = input(f"meeting {i+1} start (HH:MM): ")
        end = input(f"meeting {i+1} end (HH:MM): ")
        meetings.append((meeting_id, time_to_minutes(start), time_to_minutes(end)))
    
    # sort meetings by start time
    meetings.sort(key=lambda x: x[1])
    
    # min-heap to track end times of occupied rooms
    occupied_rooms = []
    max_rooms = 0
    
    for id, start, end in meetings:
        # remove meetings that have ended before current start time
        while occupied_rooms and occupied_rooms[0] <= start:
            heapq.heappop(occupied_rooms)
        
        # assign room for current meeting
        heapq.heappush(occupied_rooms, end)
        
        # update maximum room count
        if len(occupied_rooms) > max_rooms:
            max_rooms = len(occupied_rooms)
    
    print(f"minimum rooms required: {max_rooms}")

if __name__ == "__main__":
    main()
