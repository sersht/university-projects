def graph_input():    
    nodes = int(input())

    graph = []
    for i in range(nodes):
        row = input().split()
        for j in range(len(row)):
            row[j] = int(row[j])
        graph.append(row) 

    return nodes, graph

if __name__ == "__main__":
    nodes, graph = graph_input()

    ans = 0
    for mask in range((1 << nodes)):
        marked_nodes = []
        for i in range(nodes):
            if (mask & (1 << i)) != 0:
                marked_nodes.append(i)
        
        good_nodes = True
        for i in marked_nodes:
            for j in marked_nodes:
                good_nodes = good_nodes and (graph[i][j] == 0)

        if good_nodes:
            ans = max(ans, len(marked_nodes))

    print(ans)
    