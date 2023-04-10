from vector import Vector


def main():
    vec = Vector([[0.0, 1.0, 2.0, 3.0]])
    print(vec.values)
    vec2 = Vector([[0.0], [1.0], [2.0], [3.0], [4.0], [5.0]])
    print(vec2.shape)
    vec3 = Vector(3)
    print(vec3.values)
    vec1 = Vector((10, 16))
    print(vec1.values)
    vec.T()
    count = vec1.dot(vec2)
    print(count)
    vec2.T()
    print(vec.values)
    vec = vec / 0

    print(vec.values)
    print(vec2.values)


main()
