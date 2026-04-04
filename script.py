from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
disp_m = 500 #this is mass in KeV/c^2
m = disp_m * 1000 #this is eV/c^2
HBAR = 6.582119569E-6 #this is 1e10 greater than its actual value in eV/s, but I need to scale everything up so we stay within FP precision
l = 1 #this is in nm
U = 0 #this is potential, probably needs to be turned into a matrix
Lt = 1000000 #this is in nanoseconds, and is the stepping for time
Lx = l/20 #this is the granularity of our finite-difference stepping in x
#coefficients of the matrix
Ai = (np.power(HBAR,2))/m * Lt
Bi = (-2*np.power(HBAR,2)/(m)) - (2*(np.power(Lx,2))*Lt*U) + (4*np.power(Lx,2)*1j*HBAR)
Bl = (2*np.power(HBAR,2)/(m)) + (2*(np.power(Lx,2))*Lt*U) + (4*np.power(Lx,2)*1j*HBAR) #this one is for Di
Ci = (np.power(HBAR,2))/m * Lt
n = 5 #just for the stationary state for now...
current_state = [] #holds all the psi values currently known
DArr = [] #holds the rhs of the equation
TArr = [] #linear transformation to go from each state
#We assume a sinusoidal form of psi initially
def init_psi_sinusoidal():
    for i in range (0, 20):
        #current_state.append(np.sqrt(2/l) * np.sin(n*np.pi*(Lx*i)/l))
        current_state.append(np.sqrt(2/l) * np.exp(-np.pow(((Lx*i)-0.11)/(0.13), 2)))
        DArr.append(-1)
def init_matrix():
    for i in range (0, 20):
        temp = []
        for j in range (0, 20):
            match i-j:
                case -1:
                    temp.append(Ci)
                case 0:
                    temp.append(Bi)
                case 1:
                    temp.append(Ai)
                case _:
                    temp.append(0)
        TArr.append(temp)
    #boundary conditions
    TArr[0][0] = 1
    TArr[0][1] = 0
    TArr[19][18] = 0
    TArr[19][19] = 1
init_matrix()
init_psi_sinusoidal() #yes, I did make a method I'm calling once and only once. There will be a button-y GUI eventually where this comes in handy.
CS = np.array(current_state)
DA = np.array(DArr, complex)
TA = np.array(TArr)
plt.plot(CS, color = 'red')

#These coefficients are largely the same for calculated Di, but some signs are flipped
def set_bounds():
    DA[0] = 0
    DA[19] = 0
def calc_Di():
    set_bounds()
    for i in range (1,19):
        DA[i] = (-Ai * CS[i-1]) + (Bl * CS[i]) - (Ci * CS[i+1])

def anim():
    plt.plot(CS)
ax = plt.subplot()
for k in range (1,100): #as we can see, nothing changes, which is really good and means I didn't mess up
    for j in range (1, 100):
        calc_Di()
        NS = np.linalg.solve(TA,DA) #we will have some kind of interpretation, at some point.
        CS = NS
    plt.plot(CS, color = 'blue')