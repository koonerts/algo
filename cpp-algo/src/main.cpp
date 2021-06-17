#include <cassert>
#include <cstdint>
#include <iostream>
#include <iomanip>
#include <sstream>


using namespace std;

using codepoint = std::uint32_t;
using utf16 = std::uint16_t;

struct surrogate {
    utf16 high; // Leading
    utf16 low;  // Trailing
};

constexpr surrogate split(codepoint const in) noexcept {
    auto const inMinus0x10000 = (in - 0x10000);
    surrogate const r{
            static_cast<utf16>((inMinus0x10000 / 0x400) + 0xd800), // High
            static_cast<utf16>((inMinus0x10000 % 0x400) + 0xdc00)}; // Low
    return r;
}

constexpr codepoint combine(surrogate const s) noexcept {
    return static_cast<codepoint>(
            ((s.high - 0xd800) * 0x400) + (s.low - 0xdc00) + 0x10000);
}

constexpr bool isValidUtf16Surrogate(utf16 v) noexcept
{ return (v & 0xf800) == 0xd800; }

constexpr bool isValidCodePoint(codepoint v) noexcept {
    return (v <= 0x10ffff)
           && ((v >= 0x10000) || !isValidUtf16Surrogate(static_cast<utf16>(v)));
}

constexpr bool isValidUtf16HighSurrogate(utf16 v) noexcept
{ return (v & 0xfc00) == 0xd800; }

constexpr bool isValidUtf16LowSurrogate(utf16 v) noexcept
{ return (v & 0xfc00) == 0xdc00; }

constexpr bool codePointNeedsUtf16Surrogates(codepoint v) noexcept
{ return (v >= 0x10000) && (v <= 0x10ffff); }


template< typename T >
std::string int_to_hex( T i )
{
    std::stringstream stream;
    stream << "0x"
           << std::setfill ('0') << std::setw(sizeof(T)*2)
           << std::hex << i;
    return stream.str();
}



void test(codepoint const in) {
    assert(isValidCodePoint(in));
    assert(codePointNeedsUtf16Surrogates(in));
    auto const s = split(in);
    assert(isValidUtf16HighSurrogate(s.high));
    assert(isValidUtf16LowSurrogate(s.low));

    cout << int_to_hex(s.high) << " " << int_to_hex(s.low) << endl;

    auto const out = combine(s);
    assert(isValidCodePoint(out));
    assert(in == out);
}

int main() {
    /*cout << "0xd83c + 0xd000 -> " << int_to_hex(combine({0xd83c, 0xd000})) << endl;
    cout << "0xd83c + 0xdfff -> " << int_to_hex(combine({0xd83c, 0xdfff})) << endl;
    cout << endl;

    cout << "0xd83d + 0xd000 -> " << int_to_hex(combine({0xd83d, 0xd000})) << endl;
    cout << "0xd83d + 0xdfff -> " << int_to_hex(combine({0xd83d, 0xdfff})) << endl;
    cout << endl;

    cout << "0xd83e + 0xd800 -> " << int_to_hex(combine({0xd83e, 0xd000})) << endl;
    cout << "0xd83e + 0xdfff -> " << int_to_hex(combine({0xd83e, 0xdfff})) << endl;
    cout << endl;*/

    /*for (codepoint c = 0x1f3ff; c <= 0x10ffff; ++c)
        test(c);*/
}
