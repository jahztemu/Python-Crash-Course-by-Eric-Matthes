# 3.1
client = ["paul", "peter", "mary", "john"]
print(client[0])
print(client[1])
print(client[2].upper())
print(client[3].title())

print("/////")

# 3.2
client = ["paul", "peter", "mary", "john"]
print(f"Mr {client[0]} want his project completed by tomorrow".title())
print(f"The new client is Mr {client[1]}")
print(f"Our best client is Mr {client[2]} ")
print(f"The most promising client is Mr {client[3]}")

print("/////")

# 3.3
modes = ["boat", "ferry", "airplane", "taxi"]
print(
    "If you are a traveler you need to consider various means, let say you just taking a "
    f"city tour try considering {modes[3]} otherwise {modes[0]} if there are canals,"
    f" but if let say river {modes[1]} should be the best option."
    f" lastly wanna travel through continent then try {modes[2]}."
)

print("/////")

# 3.4
invitees = ["John", "James", "Andrew", "Hope", "Trust"]
print(f"I would like {invitees[0]} to be present in the meeting")
print(f"Also {invitees[1]} should also be present")
print("\nVIP list")
print(f"A special invite to {invitees[2]}")
print(f"The board member chairman {invitees[3]} should be around")
print(f"lastly the managing director should be around that`s {invitees[4]}")

print("/////")

# 3.5
print(
    "\nSome people won`t be making it to the meeting the names are "
    f"{invitees[1]} and {invitees[2]}"
)
invitees[1] = "Mary"
invitees[2] = "Rico"
print(f"I would love {invitees[0]} to be present in the meeting")
print(f"Also {invitees[1]} should also be present")
print("\nVIP list")
print(f"A special invite to {invitees[2]}")
print(f"The board member chairman {invitees[3]} should be around")
print(f"Lastly the managing director should be around that`s {invitees[4]}")

print("/////")

# 3.6
print(
    "We are moving the dinner meeting to a new location which can accommodate"
    " more people so the guest list is going to increase"
)
print("we would be inviting 3 new more guest")
new_invite_list = invitees.copy()
new_invite_list.insert(0, "Walker")
new_invite_list.insert(3, "Ryan")
new_invite_list.insert(7, "Prince")

print(
    f"Mr {new_invite_list[0]} you have been invited to a dinner with some honorable "
    "board members, we would love to see you attend"
)
print(
    f"Mr {new_invite_list[1]} you have been invited to a dinner with some honorable "
    "board members, we would love to see you attend"
)
print(
    f"Mrs {new_invite_list[2]} you have been invited to a dinner with some honorable "
    "board members, we would love to see you attend"
)
print(
    f"Mr {new_invite_list[3]} you have been invited to a dinner with some honorable "
    "board members, we would love to see you attend"
)
print(
    f"Mr {new_invite_list[4]} you have been invited to a dinner with some honorable "
    "board members, we would love to see you attend"
)
print(
    f"Mrs {new_invite_list[5]} you have been invited to a dinner with some honorable "
    "board members, we would love to see you attend"
)
print(
    f"Mr {new_invite_list[6]} you have been invited to a dinner with some honorable "
    "board members, we would love to see you attend"
)
print(
    f"Mr {new_invite_list[7]} you have been invited to a dinner with some honorable "
    "board members, we would love to see you attend"
)

print("/////")

# 3.7
edit_list = new_invite_list
print("Due to some certain occurrence, we can only invite two people")
print(f"\nMr {edit_list.pop()} you are no longer invited to the dinner meeting")
print(f"Mr {edit_list.pop()} you are no longer invited to the dinner meeting")
print(f"Mr {edit_list.pop()} you are no longer invited to the dinner meeting")
print(f"Mr {edit_list.pop()} you are no longer invited to the dinner meeting")
print(f"Mr {edit_list.pop()} you are no longer invited to the dinner meeting")
print(f"Mr {edit_list.pop()} you are no longer invited to the dinner meeting")

print(
    f"Mr {edit_list[0]} you are still in for the meeting; we are expecting your arrival"
)
print(
    f"Mr {edit_list[1]} you are still in for the meeting; we are expecting your arrival"
)

print(edit_list)
edit_list.remove("Walker")
edit_list.remove("John")
print(edit_list)

print("/////")

# 3.8
location = ["lagos", "abuja", "portharcourt", "asaba", "enugu", "warri", "ozoro"]
print(location)
print(sorted(location))
print(location)
print(sorted(location, reverse=True))
print(location)
location.reverse()
print(location)
location.reverse()
print(location)
location.sort()
print(location)
location.sort(reverse=True)
print(location)

print("/////")

# 3.9
print(len(invitees))
