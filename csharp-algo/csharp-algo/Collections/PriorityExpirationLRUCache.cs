using System.Collections.Generic;

namespace csharp_algo.Collections
{
    public class PriorityExpirationLRUCacheItem
    {
        public string Key { get; set; }
        public string Value { get; set; }
        public int Priority { get; set; }
        public int ExpiresAt { get; set; }
    }

    public class PriorityComparer : IComparer<PriorityExpirationLRUCacheItem>
    {
        public int Compare(PriorityExpirationLRUCacheItem x, PriorityExpirationLRUCacheItem y)
        {
            if (x.Priority < y.Priority)
                return -1;
            if (x.Priority > y.Priority)
                return -1;
            return 0;
        }
    }

    public class ExpirationComparer : IComparer<PriorityExpirationLRUCacheItem>
    {
        public int Compare(PriorityExpirationLRUCacheItem x, PriorityExpirationLRUCacheItem y)
        {
            if (x.ExpiresAt < y.ExpiresAt)
                return -1;
            if (x.ExpiresAt > y.ExpiresAt)
                return 1;
            return 0;
        }
    }

    public class PriorityExpirationLRUCache
    {
        private readonly SortedSet<PriorityExpirationLRUCacheItem> _prioritySet = new(new PriorityComparer());
        private readonly SortedSet<PriorityExpirationLRUCacheItem> _expirationSet = new(new ExpirationComparer());
        private readonly Dictionary<string, PriorityExpirationLRUCacheItem> _cache = new();
        private Dictionary<int, LinkedList<PriorityExpirationLRUCacheItem>> _prioList = new();
        private int _size = 0;
        private readonly int _capacity;

        public int Size => _size;
        public int Capacity => _capacity;

        public PriorityExpirationLRUCache(int capacity)
        {
            _capacity = capacity;
        }

        public PriorityExpirationLRUCacheItem? Get(string key)
        {
            if (!_cache.ContainsKey(key))
                return null;

            var item = _cache[key];
            _prioList[item.Priority].Remove(item);
            _prioList[item.Priority].AddFirst(item);
            return item;
        }

        public void Set(string key, string val, int priority, int expiresAt)
        {
            if (_cache.ContainsKey(key))
            {
                var item = _cache[key];
                item.Value = val;
                if (item.ExpiresAt != expiresAt || item.Priority != priority)
                {
                    if (item.Priority != priority)
                    {
                        _prioritySet.Remove(item);
                        _prioList[item.Priority].Remove(item);
                        item.Priority = priority;
                        _prioritySet.Add(item);
                        _prioList[item.Priority].AddFirst(item);
                    }

                    if (item.ExpiresAt != expiresAt)
                    {
                        _expirationSet.Remove(item);
                        item.ExpiresAt = expiresAt;
                        _expirationSet.Add(item);
                    }
                }
            }
            else
            {
                var item = new PriorityExpirationLRUCacheItem
                {
                    Key = key,
                    Value = val,
                    Priority = priority,
                    ExpiresAt = expiresAt
                };
                _size++;
                _cache[key] = item;
                _prioritySet.Add(item);
                _prioList[item.Priority].AddFirst(item);
            }

            if (_size > _capacity)
            {
                Evict(0);
            }
        }

        public void Evict(int currentTime)
        {
            if (_expirationSet.Count == 0)
                return;
            PriorityExpirationLRUCacheItem itemToRemove;
            if (_expirationSet.Min?.ExpiresAt <= currentTime)
                itemToRemove = _prioritySet.Min!;
            else
                itemToRemove = _prioList[_prioritySet.Min!.Priority].Last!.ValueRef;

            _prioList[itemToRemove!.Priority].Remove(itemToRemove);
            _prioritySet.Remove(itemToRemove);
            _expirationSet.Remove(itemToRemove);
            _cache.Remove(itemToRemove.Key);
        }
    }
}