namespace HackAlgo\Collection;

class Heap<T> {
    private Vector<T> $arr;

    public function __construct(
        ?Vector<T> $arr,
        private (function(T, T): int) $comparator
    ) {
        if ($arr is null) {
            $arr = Vector<T>{};
        }
        $this->arr = $arr;
        $this->heapify();
    }

    public function len(): int {
        return \len($this->arr);
    }

    public function peek(): ?T {
        return idx($this->arr, 0);
    }

    public function push(T $val): void {
        $this->arr->add($val);
        $this->siftDown(0, $this->len()-1);
    }

    public function pop(): ?T {
        if ($this->len() === 0) {
            return null;
        }

        $last = $this->arr->pop();
        if ($this->len() === 0) {
            return $last;
        } else {
            $first = $this->arr[0];
            $this->arr[0] = $last;
            $this->siftUp(0);
            return $first;
        }
    }

    private function heapify(): void {
        $mid = \div($this->len(), 2);
        for ($i = $mid; $i >= 0; $i--) {
            $this->siftUp($i);
        }
    }

    private function siftUp(int $startIdx): void {
        $node = $this->arr[$startIdx];
        $swapIdx = $startIdx;
        $leftIdx = 2*$swapIdx + 1;
        $size = $this->len();
        $comparator = $this->comparator;

        while ($leftIdx < $size) {
            $rightIdx = $leftIdx + 1;
            if ($rightIdx < $size && $comparator($this->arr[$rightIdx], $this->arr[$leftIdx]) <= 0) {
                $leftIdx = $rightIdx;
            }
            $this->arr[$swapIdx] = $this->arr[$leftIdx];
            $swapIdx = $leftIdx;
            $leftIdx = $leftIdx*2 + 1;
        }

        $this->arr[$swapIdx] = $node;
        $this->siftDown($startIdx, $swapIdx);
    }

    private function siftDown(int $startIdx, int $endIdx): void {
        $node = $this->arr[$endIdx];
        $comparator = $this->comparator;

        while ($startIdx < $endIdx) {
            $parentIdx = \div($endIdx-1, 2);
            if ($comparator($node, $this->arr[$parentIdx]) < 0) {
                $this->arr[$endIdx] = $this->arr[$parentIdx];
                $endIdx = $parentIdx;
                continue;
            }
            break;
        }

        $this->arr[$endIdx] = $node;
    }
}
