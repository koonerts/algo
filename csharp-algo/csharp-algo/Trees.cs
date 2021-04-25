#nullable disable
using System;
using System.Collections.Generic;

namespace csharp_algo
{
    public class Trees
    {
        public class TreeNode
        {
            public int val;
            public TreeNode left;
            public TreeNode right;

            public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
            {
                this.val = val;
                this.left = left;
                this.right = right;
            }
        }

        public int MaxPathSum(TreeNode root)
        {
            var maxSum = -1 << 31;
            int dfs(TreeNode node)
            {
                if (node == null)
                    return 0;

                var leftSum = Math.Max(dfs(node.left), 0);
                var rightSum = Math.Max(dfs(node.right), 0);
                var totalSum = leftSum + rightSum + node.val;
                maxSum = Math.Max(maxSum, totalSum);
                return Math.Max(Math.Max(leftSum, rightSum) + node.val, 0);
            }

            dfs(root);
            return maxSum;
        }


        public char[][] UpdateBoard(char[][] board, int[] click)
        {
            var val = board[click[0]][click[1]];
            var visited = new HashSet<(int, int)>();
            switch (val)
            {
                case 'M':
                    board[click[0]][click[1]] = 'X';
                    return board;
                case 'E':
                    var adjMinesCnt = GetAdjMineCount(board, (click[0], click[1]));
                    if (adjMinesCnt == 0)
                    {
                        Reveal(board, visited, (click[0], click[1]));
                    }
                    else
                    {
                        board[click[0]][click[1]] = Convert.ToString(adjMinesCnt)[0];
                    }

                    return board;
                default:
                    return board;
            }
        }

        private void Reveal(char[][] board, HashSet<(int, int)> visited, (int x, int y) origPoint)
        {
            var que = new Queue<(int x, int y)>();
            que.Enqueue(origPoint);
            visited.Add(origPoint);

            while (que.Count > 0)
            {
                var p = que.Dequeue();

                var adjMinesCnt = GetAdjMineCount(board, p);
                if (adjMinesCnt == 0)
                {
                    board[p.x][p.y] = 'B';
                    foreach (var adjP in GetValidAdjacentLocations(p, board.Length, board[0].Length))
                    {
                        if (board[adjP.x][adjP.y] != 'E' || visited.Contains(adjP)) continue;
                        visited.Add(adjP);
                        que.Enqueue(adjP);
                    }
                }
                else
                {
                    board[p.x][p.y] = Convert.ToString(adjMinesCnt)[0];
                }
            }
        }

        private IEnumerable<(int x, int y)> GetValidAdjacentLocations((int x, int y) origPoint, int rows, int cols)
        {
            var adjPoints = new List<(int x, int y)>();
            foreach (var p in new List<(int x, int y)> { (0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1) })
            {
                var newX = p.x + origPoint.x;
                var newY = p.y + origPoint.y;
                if (newX < 0 || newY < 0 || newX >= rows || newY >= cols)
                    continue;
                adjPoints.Add((newX, newY));
            }

            return adjPoints;
        }

        private int GetAdjMineCount(char[][] board, (int x, int y) point)
        {
            var cnt = 0;
            foreach (var p in GetValidAdjacentLocations(point, board.Length, board[0].Length))
            {
                if (board[p.x][p.y] == 'M')
                    cnt++;
            }

            return cnt;
        }
    }
}