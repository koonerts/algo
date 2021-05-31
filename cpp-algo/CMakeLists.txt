cmake_minimum_required(VERSION 3.16)
project(cpp_algo)

set(CMAKE_CXX_STANDARD 20)
# add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(cpp_algo main.cpp arrays-and-strings/arrays.cpp arrays-and-strings/arrays.h arrays-and-strings/strings.cpp arrays-and-strings/strings.h)
add_executable(tests tests.cpp)

target_link_libraries(cpp_algo ${CONAN_LIBS})
target_link_libraries(tests ${CONAN_LIBS})