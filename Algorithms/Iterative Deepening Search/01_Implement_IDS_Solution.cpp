#include <bits/stdc++.h>
using namespace std;

void ids(vector<int> graph[], int source, int visited[], int depth[], int max_depth)
{
    // Mark source as visited
    visited[source] = 1;

    cout << "Explored  " << source << " at depth " << depth[source] << endl;

    // Iterate through the neighbours of the current source
    for (int neighbour : graph[source])
    {
        // if neighbour isn't visited yet
        if (visited[neighbour] == 0)
        {
            // increase depth
            depth[neighbour] = depth[source] + 1;

            // if neighbours depth excess the max depth limit then continue
            if (depth[neighbour] > max_depth)
            {
                continue;
            }
            // else do recursion
            else
                ids(graph, neighbour, visited, depth, max_depth);
        }
    }
}

int main()
{

    freopen("input.txt", "r", stdin);

    int nodes, edges, source, a, b;

    // Take input for nodes and edges
    cin >> nodes >> edges;

    // Declare a vector to store edge connections
    vector<int> graph[nodes];

    // Take input and store bi-directional edges
    while (edges--)
    {
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    // Take source input
    cin >> source;

    // Iterating upto highest depth limit
    for (int max_depth = 0; max_depth < 10; max_depth++)
    {
        int visited[nodes] = {0};
        int depth[nodes] = {0};

        cout << "\nWhen depth limit: " << max_depth << endl << endl;

        // Call the IDS function
        ids(graph, source, visited, depth, max_depth);
    }

    cout << endl << endl;
}
