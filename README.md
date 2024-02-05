# Multidimentional Optimization Benchmarking

This project will test two RNGs Side-by-side in Creating Random Solution Vectors, then apply gradient descent to optimize the random vectors.

The program is driven by the main.py file. This file will execute _all_ optimization problems for all generators, overwriting the output csv files and printing to the terminal the new runtime and other statistical analysis for all optimization functions.

First, navigate to the LCG Directory. Once there, we must compile the C element of the project and turn it into a shared object to import into our python project.

    cd LCG
    # linux
    gcc -shared -o lcg.so -fPIC lcg.c

    # windows
    gcc -shared -o lcg.dll lcg.c


This will create a shared library to be loaded into the python project. Note that this project was built in Windows so if compilation occurs on linux, you may need to change the filename or update the LCG.py file to look for 'lcg.so'.

Once the library is built, the project has some dependancies. Namely, Pandas. This can be done by executing:

    pip install pandas


Once the shared library is built and the dependancies are installed, you can now execute the main.py file. Be advised that this will overwrite all CSV Data in the 'out' directory. For the sake of this project, all original data referenced in my report is preserved in this remote repository.

    python3 main.py



### LCG implementation in Python
___
Initially, since this project came to be, I thought it advantagious to
include Mersenne Twister due to its native implementation in Python.

The Linear Congruential Generators (LCG) however, proved simple in concept
however writing them seems to be interesting. So interesting, that I can't seem
to find code for it within the keywords on Github. I did find an implementation of
Knuths LCG which has an optimal period length. This algorithm I specifically wrote about in my Seminar. That said, it was not in my language so I'm going to see about what I can do about this, see if I can dissect it or understand the manipulation of the recurrences.

For now, I will swallow my pride and use the GNU C library which I also wrote about in my seminar which has less optimal periods. I also suspect the accuracy of my implementation to be system-dependant because of the nature of my linux installation and the amount of different C libraries with a 'rand' function. I will attempt to use the one cited in that specific paper.

The LCG is implemented in a C file, and is loaded as an extension through the python API. It currently supports raw random numbers and random range elements.

The Python-built-in MT however, requires this range by default.

Implementing the random range in the c standard library, it is possible to use a modulus with subtraction so even negative range numbers will be produced.

### MT Algorithm Testing 
After creating a Main that could dynamically support new algorithms, I created a quick blind search algorithm that creates thirty random numbers then calculates the Schwefels problems, then created a while loop that executes some 10000000000 times. my current record for random blind search 'algorithm' is the following:

best fitness: 5806.505692340973

solution vector: [254.89479094129325, -24.032701079686237, 183.03331464412364, 150.0566089183145, -1.4889431005767566, 411.0203477479716, 201.83882048234008, 192.0916464920763, -24.032701079686237, 382.6682431123425, 187.2494660983785, 403.95754647883354, 36.97823846866161, 386.76729800750405, 276.17955751672804, 166.81213414568282, 383.414660856447, 414.39054664591555, 71.66819779366934, 63.59527345175039, 65.93608970363647, 360.0784445267731, 416.93076927530075, 415.7866094562764, 383.414660856447, 201.66390689765862, 383.414660856447, 130.2948484917168, -47.031451158116845, 335.46042221080546]

I would let it run longer but it's 1:30 AM.

---

### System Random (Cryptographicaly secure)

An experiment I started by introducing three threads to generate these random sequences, comparing each generation to the last best fitness in an attempt to find a better value. This yeilded the following results:

* Threading was implemented to accellerate the generation process
* Each thread executes 1,000,000,000 generations of uniform UDEV Floats
* The program stalled or I could not discern whether or not it was still running, so I shut it down.

best fitness: 5196.913154673443

solution vector: [380.49128120675977, 418.675397279684, 417.002374290661, 407.6544993182336, 17.592729395073132, -118.27123530224372, 175.06891193917622, 383.65541151581647, 58.51743027661644, 320.05174516829305, 63.46548945517588, 296.53444326061214, 392.8896356406589, -224.27894389857474, -71.45145411792383, 408.79202356050433, 292.1542355314778, 53.41814905316261, 370.6266255876463, 227.1546044561721, 166.84268292901248, 380.5025537607302, 229.32076725878585, 397.1703374201966, 56.41411945086024, 414.94957553040695, 322.0917662549592, 384.8424053234337, 394.8540447903115, 355.8722389908778]

## The Optimization Algorithm

The Blind Random Search algorithm initially implemented works on the following steps:
    * Generate a random array of n elements where n is the dimentionality of the problem
    * Calculate the output of the function such that each element is added to the equation and a fitness is calculated. This Fitness is returned, along with the solution vector which created it.

As you may notice, the first iteration of the blind search algorithm is quite inefficient and is unlikely to produce optimal outcomes. The premise on why a randomized blind search is predicated on the idea that it is exponentially difficult to calculate the problem in moderate values of n dimensions. Likewise it is also unlikely to guess the optimal value also for n dimensions.

This will be difficult due to the probability of independant events.
a solution vector could approach a global optima on x_3, and then be regenerated once more, at a less optimal value for this function at that value.

For example, the probability that we guess a global optima in n dimensions is something akin to the number of numbers in the functions defined range and then raised to the power of dimensions. Lets take Schwefels for example, it takes parameters in a range of -500 to 500, if we are just talking integers (which I will for the sake of simplicity) the likelyhood of guessing the global optima on thirty dimensions is:

1 in 1000^30

## Gradient Descent
Since the functions are defined on positive and negative values it is important to attempt to descend a gradient by adding or subtracting an alpha value by each dimention of x to 'optimize' the randomly generated values of the solution vector. This is implemented using a parent class, since the process is inspecific to each of the functions. Even in only descending the gradient with a negative alpha value, the fitness of each of the solution vectors was extraordinarily better than even the most testing of blind search outlined above.

Choosing an alpha value was difficult, I noticed that for most of the functions, that the global minimas were at most 0.7 away from an optimal value. I figured an alpha of 1.0 was sufficient to find a decent value around the global minima.

One problem I did notice is no matter how many times the vectors were generated, I kept discovering local minimas. For example: Schwefels returned values of either 421, -421, -66, 66, -204, 204, -5 and 5. These appear to be either the approximate global minima (Scwefels output is approximately zero for input values at 420.9687) or the closest local minima from the number generated.

These local minimas are the minimas closest to the random number generated, and since it's descending any gradient it gets a better output for, it's going to fail to find the global minima most of the time.

## Doubly Random walk
As you can see, this becomes incredibly unlikely for anything like a calculation based on 30 dimensions. If the global optima for the function is the same for every dimension of the solution vector, we can exploit the probability of guessing an optima by guessing each dimension one after the other, keeping the previous vectors calculated for context, and once the desired dimensionality is reached, the fitness should be better, since the probability of generating a global optima for a single value for Schwefels is one in 1000. This would also reduce the number of times these random sequences must be generated. If we exploit this new algorithm, it may be able to guess a good value approaching the global optima in only two-thousand or three-thousand random generations times the dimensionality.

2000*(30)

## Doubly Random walk + Gradient Descent

Doubly Random walk and Gradient descent are far from perfect, with only marginal theoretical improvement on doubly random walk on it's own. However, if this increases the odds of finding the gradient of the global optima it may be possible to increase the odds of the algorithm discovering the gradient on the global optima, and resulting in a better fitness.


