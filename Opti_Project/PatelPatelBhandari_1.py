#!/usr/bin/env python
# coding: utf-8

## SUBMITTED BY:
# Yash Patel
# Yash Patel
# Kritika Bhandari

# In[1]:
from gurobipy import *
import os
import csv


# In[94]:
file_name = "XYZ.csv"

with open(file_name, 'r') as file:
    csv_reader = csv.reader(file)
    data = []

    for row in csv_reader:
        data.extend(row)

data_file_name = file.name


# In[96]:
s = [32, 40]
r = [int(value) for value in data]

## limit input size for trial runs
#r = r[0:400]


# In[98]:
# Model Initiation
m = Model("Shift_Distribution_Problem")

# as our decision variable is Xit, we initiate indices for i and t
i_indices = range(len(s))

t_indices = range(len(r))


# In[100]:
## Decision Variable Xit
X = m.addVars(i_indices, t_indices, vtype=GRB.INTEGER, name="X")


# In[101]:
# Objective function
m.setObjective(quicksum(X[i, t] for i in i_indices for t in t_indices), GRB.MINIMIZE)


# In[102]:
## Constraints
# (1) Coverage Requirement
for t in t_indices:
    m.addConstr(quicksum(X[i, tau] for i in i_indices for tau in range(max(0, t - s[i] + 1), t + 1)) >= r[t], name=f"demand_constraint_{t}")


# In[103]:
# (2) Last few shifts should not be initialized
for t in range(len(t_indices)-31, len(t_indices)):
    m.addConstr(X[0, t] == 0, name=f"last_zeroes_8hours_{t}")

for t in range(len(t_indices)-39, len(t_indices)):
    m.addConstr(X[1, t] == 0, name=f"last_zeroes_10hours_{t}")


# In[104]:
# (3) Non-negativity constraint
for i in i_indices:
    for t in t_indices:
        m.addConstr(X[i, t] >= 0, name=f"non-negativity_{i},{t}")
    

# In[105]:
m.Params.timeLimit = 10


# In[106]:
m.optimize()


# In[107]:
# Check if the optimization was successful
if m.status == GRB.OPTIMAL:
    # Access and print the values of decision variables X
    for i in i_indices:
        for t in t_indices:
            if X[i, t].x != 0:
                print(f"X[{i},{t}] = {X[i, t].x}")

    # Access and print the objective value
    print(f"Optimal Objective Value: {m.objVal}")
else:
    print("Optimization was not successful.")


# In[108]:
model_status = ""

if m.status == GRB.OPTIMAL:
    model_status += f"Termination status: Optimal\n"
    model_status += f"Best objective value: {m.objVal}\n"
    model_status += f"Elapsed wall-clock time: {m.Runtime} seconds\n"
    model_status += f"Optimality gap at termination: {m.MIPGap}%\n"
elif m.status == GRB.INFEASIBLE:
    model_status += "Termination status: Infeasible\n"
    model_status += f"Infeasibility reason: {m.UnbdRay}\n"
elif m.status == GRB.UNBOUNDED:
    model_status += "Termination status: Unbounded\n"
elif m.status == GRB.TIME_LIMIT:
    model_status += "Termination status: Time Limit Exceeded\n"
    model_status += f"Best objective value: {m.objVal}\n"
    model_status += f"Optimality gap at termination: {m.MIPGap}%\n"
else:
    model_status += f"Optimization terminated with status: {m.status}\n"

print(model_status)


# In[109]:
# How many total shifts are required?
count_total_shifts = 0
for i in i_indices:
    for t in t_indices:
        if X[i, t].x != 0:
            count_total_shifts = count_total_shifts + X[i, t].x

print(int(count_total_shifts))


# In[110]:
# When does shifts start?
## Note that first shift will be printed as "1" and not "0"
distribution_text = ""

for i in i_indices:
    for t in t_indices:
        if X[i, t].x != 0:
            if i == 0:
                distribution_text += f"from {t+1}th period {t+33}th period, {int(X[i, t].x)} count of 8-hour shift needed\n"
            if i == 1:
                distribution_text += f"from {t+1}th period {t+41}th period, {int(X[i, t].x)} count of 10-hour shift needed\n"

print(distribution_text)


# In[111]:
# How many 8-hours shifts are required?
count_8_hours = 0
for t in t_indices:
    if X[0, t].x != 0:
            count_8_hours = count_8_hours + X[i, t].x

print(int(count_8_hours))


# In[112]:
# How many 10-hours shifts are required?
count_10_hours = 0
for t in t_indices:
    if X[1, t].x != 0:
            count_10_hours = count_10_hours + X[i, t].x

print(int(count_10_hours))


# In[113]:
file_path = "PatelPatelBhandari.txt"

#with open(file_path, "w") as file: pass

with open(file_path, "a") as file:
    file.write(f"For data obtained from {data_file_name}:\n\n")
    file.write("Model Status:\n")
    file.write(model_status)
    file.write("\n")
    file.write("Shift_Distribution_Problem_results:\n")
    file.write(distribution_text)
    file.write("\n\n--XX--XX--XX--XX--XX--XX--XX--XX--XX--XX--XX--XX--XX--\n\n")
