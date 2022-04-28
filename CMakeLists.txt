cmake_minimum_required(VERSION 3.22.1)
project(metslib VERSION 0.6 LANGUAGES CXX)
enable_testing()

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED YES)
set(CMAKE_CXX_EXTENSIONS NO)

add_compile_definitions(METSLIB_HAVE_UNORDERED_MAP)
include_directories(${CMAKE_CURRENT_LIST_DIR})

# Do not run tests if the project is not top-level CMake project.
if(CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
    add_subdirectory(test)
endif()