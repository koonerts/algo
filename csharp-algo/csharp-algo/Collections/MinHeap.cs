using System;
using System.Collections.Generic;

namespace csharp_algo.Collections
{
    public class MinHeap<T> where T : IComparable<T>
    {
        public int Count => _heap.Count;
        private List<T> _heap;


        public MinHeap()
        {
            _heap = new List<T>();
        }

        public MinHeap(List<T> arr)
        {
            _heap = arr;
            Heapify();
        }

        public void Heapify()
        {
            for (var i = _heap.Count / 2; i >= 0; i--)
                SiftUp(i);
        }

        private void SiftDown(int startIdx, int swapIdx)
        {
            T node = _heap[swapIdx];
            while (startIdx < swapIdx)
            {
                int parentIdx = (swapIdx - 1) / 2;
                if (node.CompareTo(_heap[parentIdx]) == -1)
                {
                    _heap[swapIdx] = _heap[parentIdx];
                    swapIdx = parentIdx;
                    continue;
                }

                break;
            }

            _heap[swapIdx] = node;
        }

        private void SiftUp(int startIdx)
        {
            T node = _heap[startIdx];
            int swapIdx = startIdx;
            int leftIdx = startIdx * 2 + 1;
            while (leftIdx < _heap.Count)
            {
                int rightIdx = leftIdx + 1;
                if (rightIdx < _heap.Count && _heap[rightIdx].CompareTo(_heap[leftIdx]) <= 0)
                    leftIdx = rightIdx;
                _heap[swapIdx] = _heap[leftIdx];
                swapIdx = leftIdx;
                leftIdx = leftIdx * 2 + 1;
            }

            _heap[swapIdx] = node;
            SiftDown(startIdx, swapIdx);
        }

        public void Push(T val)
        {
            _heap.Add(val);
            SiftDown(0, _heap.Count - 1);
        }

        public T Pop()
        {
            T last = _heap[^1];
            _heap.RemoveAt(_heap.Count-1);
            if (_heap.Count == 0) return last;

            T first = _heap[0];
            _heap[0] = last;
            SiftUp(0);
            return first;
        }

        public T Peek()
        {
            return _heap[0];
        }
    }
}