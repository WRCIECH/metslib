add_executable(PermutationProblem permutation_problem_test.cc)
add_test(NAME CheckPermutationProblem COMMAND PermutationProblem)

add_executable(TabuList tabu_list_test.cc)
add_test(NAME CheckTabuList COMMAND TabuList)

add_executable(Termination termination_test.cc)
add_test(NAME CheckTermination COMMAND Termination)