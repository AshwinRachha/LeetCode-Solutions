class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) 
    {
        queue <pair <int, int>> q;
        q.push({entrance[0], entrance[1]});
        int moves = 1;
        maze[entrance[0]][entrance[1]] = '+';
        vector <vector <int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int rows = maze.size(); int cols = maze[0].size();
        while(!q.empty())
        {
            int size = q.size();
            for(int i = 0; i < size; i++)
            {
                auto [x, y] = q.front();
                q.pop();
                for(auto v : directions)
                {
                    int x1 = x + v[0];
                    int y1 = y + v[1];
                    if(x1 < 0 || x1 >= rows || y1 < 0 || y1 >= cols || maze[x1][y1] == '+')
                        continue;
                    if(x1 == 0 || x1 == rows - 1 || y1 == 0 || y1 == cols - 1)
                        return moves;
                    maze[x1][y1] = '+';
                    q.push({x1, y1});
                }
                
            }
            moves++;
        }
        
        return -1;
    }
};