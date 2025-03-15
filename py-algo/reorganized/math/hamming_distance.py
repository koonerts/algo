"""
Distance

"""
def hammingDistance(x: int, y: int) -> int:
        cntr = 0
        while x > 0 or y > 0:
            if x == 0 and y > 0:
                while y > 0:
                    y &= y-1
                    cntr += 1
                break
            elif y == 0 and x > 0:
                while x > 0:
                    x &= x-1
                    cntr += 1
            else:
                lowest_bit_x = x & ~(x-1)
                lowest_bit_y = y & ~(y-1)

                if lowest_bit_x < lowest_bit_y:
                    x -= lowest_bit_x
                    cntr += 1
                elif lowest_bit_y < lowest_bit_x:
                    y -= lowest_bit_y
                    cntr += 1
                else:
                    x -= lowest_bit_x
                    y -= lowest_bit_y

        return cntr



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to hammingDistance
    print(hammingDistance([]))
