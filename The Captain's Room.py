K = int(input())
room_numbers = list(map(int, input().split()))

unique_rooms = set(room_numbers)

captain_room = (K * sum(unique_rooms) - sum(room_numbers)) // (K-1)
print(captain_room)
