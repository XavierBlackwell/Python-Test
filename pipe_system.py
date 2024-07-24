def connected_sinks(input_file, output_file):
    # Read the input file and parse the data
    with open(input_file, 'r', encoding='utf-8') as file:
        data = [line.strip().split() for line in file]

    # Create a grid to represent the pipe system
    grid = {}
    source = None
    sinks = set()
    for item, x, y in data:
        x, y = int(x), int(y)
        grid[(x, y)] = item
        if item == '*':
            source = (x, y)
        elif item.isupper():
            sinks.add(item)

    # Define the connections for each pipe type
    pipe_connections = {
        '═': [(1, 0), (-1, 0)],
        '║': [(0, 1), (0, -1)],
        '╔': [(1, 0), (0, 1)],
        '╗': [(-1, 0), (0, 1)],
        '╚': [(1, 0), (0, -1)],
        '╝': [(-1, 0), (0, -1)],
        '╠': [(1, 0), (0, 1), (0, -1)],
        '╣': [(-1, 0), (0, 1), (0, -1)],
        '╦': [(1, 0), (-1, 0), (0, 1)],
        '╩': [(1, 0), (-1, 0), (0, -1)],
        '*': [(1, 0), (-1, 0), (0, 1), (0, -1)],
    }

    # Function to check if two cells are connected
    def is_connected(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        item1 = grid.get(pos1)
        item2 = grid.get(pos2)
        if item1 is None or item2 is None:
            return False
        if item1.isupper():
            item1 = '*'
        if item2.isupper():
            item2 = '*'
        dx, dy = x2 - x1, y2 - y1
        return (dx, dy) in pipe_connections.get(item1, []) and (-dx, -dy) in pipe_connections.get(item2, [])

    # Perform DFS to find connected sinks
    def dfs(pos, visited):
        visited.add(pos)
        x, y = pos
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (x + dx, y + dy)
            if new_pos not in visited and is_connected(pos, new_pos):
                dfs(new_pos, visited)

    # Find all connected sinks
    visited = set()
    dfs(source, visited)
    connected = [sink for sink in sinks if any((x, y) in visited for x, y in grid if grid[(x, y)] == sink)]
    result = ''.join(sorted(connected))

    # Write the result to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(result)

    return result

# Use the function
input_file = 'input.txt'
output_file = 'output.txt'
result = connected_sinks(input_file, output_file)
print(f"Connected sinks: {result}")
print(f"Result written to {output_file}")