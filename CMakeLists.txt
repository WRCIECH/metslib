cmake_minimum_required(VERSION 3.22.1)
project(metslib VERSION 0.6 LANGUAGES CXX)
enable_testing()

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED YES)
set(CMAKE_CXX_EXTENSIONS NO)

add_executable(PermutationProblem test/permutation_problem_test.cc)
target_include_directories(PermutationProblem PUBLIC ${CMAKE_CURRENT_LIST_DIR})
target_compile_definitions(PermutationProblem PUBLIC METSLIB_HAVE_UNORDERED_MAP)

add_executable(TabuList test/tabu_list_test.cc)
target_include_directories(TabuList PUBLIC ${CMAKE_CURRENT_LIST_DIR})
target_compile_definitions(TabuList PUBLIC METSLIB_HAVE_UNORDERED_MAP)

add_executable(Termination test/termination_test.cc)
target_include_directories(Termination PUBLIC ${CMAKE_CURRENT_LIST_DIR})
target_compile_definitions(Termination PUBLIC METSLIB_HAVE_UNORDERED_MAP)

add_test(NAME CheckPermutationProblem COMMAND PermutationProblem)
add_test(NAME CheckTabuList COMMAND TabuList)
add_test(NAME CheckTermination COMMAND Termination)