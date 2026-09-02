# setdefault is right for the Movement Log because an agent might not have
# a key in the log yet on its first move. setdefault(agent_id, []) inserts
# an empty list only if it's missing, then returns the list either way, so
# the same append line works for the first move and every move after.
#
# A tuple is right for Location because coordinates shouldn't change once
# set - if you want a different position you're really describing a new
# state, not editing the old one. Immutability guarantees nothing else in
# the program can silently change an agent's position from under you.
#
# Author: Kshitiz


def find_common_intelligence(registry):
    knowledge_sets = [agent_data["Knowledge"] for agent_data in registry.values()]
    return set.intersection(*knowledge_sets)


def relocate_agent(registry, log, agent_id, new_location):
    print(f"Attempting direct mutation of {agent_id}'s Location tuple...")
    try:
        registry[agent_id]["Location"][0] = 0
    except TypeError as e:
        print(f"TypeError caught: {e}")
        print("Tuples are immutable; reassigning a new tuple instead.")

    registry[agent_id]["Location"] = new_location
    log.setdefault(agent_id, []).append(new_location)

    print(f"{agent_id} new state: {registry[agent_id]}")
    print(f"Movement Log: {log}")


agent_registry = {
    "Agent_Alpha": {
        "Location": (10, 20),
        "Knowledge": {"grid_map", "comm_protocol", "telemetry_sync"},
    },
    "Agent_Beta": {
        "Location": (15, 5),
        "Knowledge": {"grid_map", "comm_protocol", "power_grid"},
    },
    "Agent_Gamma": {
        "Location": (0, 0),
        "Knowledge": {"grid_map", "comm_protocol", "power_grid", "telemetry_sync"},
    },
}

movement_log = {}

print("--- Common Intelligence Across All Agents ---")
print(find_common_intelligence(agent_registry))
print()

print("--- Relocating Agent_Alpha ---")
relocate_agent(agent_registry, movement_log, "Agent_Alpha", (12, 22))
print()

print("--- Relocating Agent_Alpha again ---")
relocate_agent(agent_registry, movement_log, "Agent_Alpha", (14, 25))
print()

summary_report = {
    agent_id: len(data["Knowledge"]) for agent_id, data in agent_registry.items()
}
print("--- Summary Report (Dictionary Comprehension) ---")
print(summary_report)

# Submission Note: the TypeError says a tuple "does not support item
# assignment" - meaning the slots inside a tuple aren't writable after
# creation. A list stores pointers to objects in a mutable array, so
# list[0] = x just swaps what that slot points to. A tuple's slots are
# fixed at creation time, so there's no operation in the type that lets
# you rewrite one - the only way to get a "different" tuple is to build
# a new one and rebind the name to it, which is exactly what
# relocate_agent does after the failed mutation attempt.
