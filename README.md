#SchrodingerSolver

What happens when you take a below-average CS student, throw him into the physics department for a year to become a below-average Physics student, and give him some free time? This thing.

##About

The repo contains a Jupyter notebook, describing the math and containing the code for my 1-D Schrodinger equation simulator. I used the Crank-Nicolson method as described [here by Robert A. Jones of Simon Fraser University](https://www.sfu.ca/~rjones/bus864/notes/notes.html) and am currently using numpy's built-in Gaussian-Jordan elimination method.

##Features

The animation is show in real-time, and you can select between currently 3 U(x) functions - an infinite square well, a harmonic potential, or a finite barrier. You can also select between 3 wave-functions, a sinusoid and 2 Gaussians. More presets and the ability to input custom wavefunctions and potentials will be added eventually.

##Things to do

1. Look at the default conditions. With the infinite square well and the sinusoidal eigenstate, you can see that the wavefunction is static in time.
2. Play with the other wavefunctions in the infinite square well. Bouncy bounce.
3. Swap to the finite square well and the left-shifted Gaussian. Observe the tunnelling of the wavefunction.
4. Swap to the harmonic potential and observe the lateral oscillations of the various wave functions.
5. This is where I'd tell you to experiment with your own wavefunctions, but that feature hasn't been added.

##Features to be done

1. Complex absorbing potentials. Right now, the infinite square well is always in place, limiting the wavefunction to the displayed space. This creates reflection artifacts. CAPs negate that.
2. User-customizable functions. I'll need to parse text input into a function, but I'm sure it's doable.
3. More displayed data (expected values, phase), and other niceties (a pause button, sliders for timescale, cleaning up my units, sliders for energy levels)
