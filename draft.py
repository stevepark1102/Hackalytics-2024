from gurobipy import GRB,Model,quicksum

model1 = Model("Minimize Cost")

z_i = model1.addVars(lb = 0, name = "z_i")
x_d = model1.addVar(name = 'x_d',lb=0)
x_g = model1.addVar(name = 'x_g',lb=0)
x_l = model1.addVar(name = 'x_l',lb=0)
x_c = model1.addVar(name = 'x_c',lb=0)
x_o = model1.addVar(name = 'x_o',lb=0)
y_p = model1.addVar(name = 'y_p',lb=0)
y_b = model1.addVar(name = 'y_b',lb=0)

model1.setObjective(3.969*x_d+3.028*x_g+3.166*x_l+2.85*x_c+3*x_o+0.28*y_p+
0.56*y_b, GRB.MINIMIZE)

model1.addConstr(z_i>=93852)
model1.addConstr((y_p+y_b)/(x_d+x_g+x_l+x_c+x_o+y_p+y_b)>=0.045)
model1.addConstr(y_b<=70684761)
model1.addConstr(y_b>=49684761)
model1.addConstr(y_p>=728800760)
model1.addConstr(y_p>=588800760)
model1.addConstr(x_d>=452371818)
model1.addConstr(x_g>=82297855)
model1.addConstr(x_l>=8480840)
model1.addConstr(x_c>=172177278)
model1.addConstr(x_o>=659520)
model1.addConstr(z_i=x_d/45237181+
x_g/82297855+x_l/8480840+x_c/172177278+
x_o/659520+y_p/5888007630+y_b/49684761)


model1.optimize()
status_code = {1:'LOADED', 2:'OPTIMAL', 3:'INFEASIBLE',\
4:'INF_OR_UNBD', 5:'UNBOUNDED'}
status = model1.status
print('The optimization status is {}'.format(status_code[status]))
if status == 2:

    print('Optimal solution:')
    for v in model1.getVars():
        print('%s = %g' % (v.varName, v.x))
        print('Optimal objective value:\n{}'.format(model1.objVal))

