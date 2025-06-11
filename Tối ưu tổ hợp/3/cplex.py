# import cplex
# from docplex.mp.model import Model

# #model
# model=Model(name="LP1")
# #variables
# x1=model.continuous_var(lb=0,ub=cplex.infinity,name='x1') #x1 >=0
# x2=model.continuous_var(lb=0,ub=cplex.infinity,name='x2') #x2 >=0

# #objective
# model.maximize(2*x1+x2)

# #constraints
# model.add_constraint(x1<=10)
# model.add_constraint(x1+2*x2<=12)
# model.add_constraint(x1-2*x2>=-8)

# #solve
# model.print_information()
# solution=model.solve()
# model.print_solution()