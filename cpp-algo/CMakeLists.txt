cmake_minimum_required(VERSION 3.16)
project(cpp_algo)

set(CMAKE_CXX_STANDARD 20)
# add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(cpp_algo src/main.cpp src/arrays-and-strings/arrays.cpp src/arrays-and-strings/strings.cpp)
add_executable(tests test/main.cpp src/arrays-and-strings/arrays.cpp src/arrays-and-strings/strings.cpp test/arrays-and-strings/arrays.cpp)

target_link_libraries(cpp_algo ${CONAN_LIBS})
target_link_libraries(tests ${CONAN_LIBS})