#!/usr/bin/env hhvm

namespace HackAlgo {

    <<__EntryPoint>>
    async function main_async(): Awaitable<void> {
        require_once(__DIR__.'/../vendor/autoload.hack');
        \Facebook\AutoloadMap\initialize();
        $h = new Collection\Heap(Vector<int>{4,5,1,2,-1}, ($n1, $n2) ==> $n1 <=> $n2);
        \print_r($h);
    }

}

namespace {

    function len(Container<mixed> $container): int {
        return HH\Lib\C\count($container);
    }

    function div(num $dividend, num $divisor): int {
        return (int)($dividend/$divisor);
    }

}
