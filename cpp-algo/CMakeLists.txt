cmake_minimum_required(VERSION 3.16)
project(cpp_algo)

set(CMAKE_CXX_STANDARD 20)
# add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(cpp_algo src/main.cpp src/topics/Arrays.cpp src/topics/Strings.cpp src/topics/Dp.cpp src/topics/Dp.h src/containers/MinHeap.cpp src/containers/MinHeap.h src/traits/traits.h src/ext/fmt.cpp src/ext/fmt.h src/topics/Graphs.cpp src/topics/Graphs.h src/ents/ListNode.cpp src/ents/ListNode.h src/topics/LinkedLists.cpp src/topics/LinkedLists.h)
add_executable(tests test/main_test.cpp src/topics/Arrays.cpp src/topics/Strings.cpp test/arrays_test.cpp src/topics/Dp.cpp src/topics/Dp.h test/dp_test.cpp src/containers/MinHeap.cpp src/containers/MinHeap.h src/traits/traits.h src/ext/fmt.cpp src/ext/fmt.h src/topics/Graphs.cpp src/topics/Graphs.h src/topics/LinkedLists.cpp src/topics/LinkedLists.h)

target_link_libraries(cpp_algo ${CONAN_LIBS})
target_link_libraries(tests ${CONAN_LIBS})