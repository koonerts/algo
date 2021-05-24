
namespace HackAlgo\Arr;

use namespace HH\Lib\C;

function binary_search(vec<num> $nums, num $targ): int {
    list($lo, $hi) = tuple(0, C\count($nums) - 1);
    while ($lo <= $hi) {
        $mid = (int)(($lo + $hi)/2);
        if ($nums[$mid] === $targ) {
            return $mid;
        } else if ($nums[$mid] > $targ) {
            $hi = $mid-1;
        } else {
            $lo = $mid+1;
        }
    }
    return -1;
}
