#!/usr/bin/env hhvm

namespace HackAlgo {

    use namespace Facebook\AutoloadMap;

    <<__EntryPoint>>
    async function main_async(): Awaitable<void> {
        require_once(__DIR__.'/../vendor/autoload.hack');
        AutoloadMap\initialize();
        \pln(dict['a'=>1,'b'=>2,'c'=>3]);
    }

}

namespace {

    function len(Container<mixed> $container): int {
        return HH\Lib\C\count($container);
    }

    function div(num $dividend, num $divisor): int {
        return (int)($dividend / $divisor);
    }

    function pln<T>(T $val): void {
        if ($val is num || $val is string) {
            echo $val."\n";
        } else if ($val is KeyedContainer<_, _>) {
            $is_list = \HH\is_list_like($val);
            $is_set = \HH\is_keyset($val);
            $str = $is_list ? '[' : '{';
            foreach ($val as $key => $value) {
                if ($str !== '[' && $str !== '{') {
                    $str .= ', ';
                }

                if ($is_list || $is_set) {
                    $str .= (string)$value;
                } else {
                    $str .= ((string)$key.':'.(string)$value);
                }
            }
            $str .= $is_list ? ']' : '}';
            echo $str."\n";
        } else {
            \print_r($val);
        }
    }

}
