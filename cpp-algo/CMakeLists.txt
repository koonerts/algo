cmake_minimum_required(VERSION 3.16)
project(cpp_algo)

set(CMAKE_CXX_STANDARD 20)
# add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(cpp_algo src/main.cpp src/topics/arrays-and-strings/arrays.cpp src/topics/arrays-and-strings/strings.cpp src/topics/dp/dp.cpp src/topics/dp/dp.h src/topics/containers/min_heap.cpp src/topics/containers/min_heap.h src/traits/traits.h src/ext/fmt.cpp src/ext/fmt.h)
add_executable(tests test/main_test.cpp src/topics/arrays-and-strings/arrays.cpp src/topics/arrays-and-strings/strings.cpp test/arrays-and-strings/arrays_test.cpp src/topics/dp/dp.cpp src/topics/dp/dp.h test/dp/dp_test.cpp src/topics/containers/min_heap.cpp src/topics/containers/min_heap.h src/traits/traits.h src/ext/fmt.cpp src/ext/fmt.h)

target_link_libraries(cpp_algo ${CONAN_LIBS})
target_link_libraries(tests ${CONAN_LIBS})