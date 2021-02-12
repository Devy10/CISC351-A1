# Test Results
Headers are going to be tuples of values, (`max_steps`, `shuffled_queens`)

## (12, 8) [baseline]



| N             | Time (s)      |
| ------------- |:-------------:|
| 10            | 0.0088        |
| 100           | 0.0096        |
| 1,000         | 0.0357        |
| 10,000        | 0.2553        |
| 100,000       | 3.5005        |
| 1,000,000     | 32.078        |
| 10,000,000    | 252.92        |

## (100,8) [high max-steps]

| N             | Time (s)      |
| ------------- |:-------------:|
| 10            | 0.0054        |
| 100           | 0.0015        |
| 1,000         | 0.0154        |
| 10,000        | 0.1412        |
| 100,000       | 1.0925        |
| 1,000,000     | 11.158        |
| 10,000,000    | 97.309        |

## (1000, 8) [**extreme max-steps**]

| N             | Time (s)      |
| ------------- |:-------------:|
| 10            | 0.0013        |
| 100           | 0.0027        |
| 1,000         | 0.0199        |
| 10,000        | 0.2399        |
| 100,000       | 1.4969        |
| 1,000,000     | 10.473        |
| 10,000,000    | 93.517        |

### Note: Seems to be unstable over `max-steps = 1000`.  

Since it appears that keeping `max-steps` at 100 gives us the fastest time and most stable time, now we have to see how high we can crank `shuffled-queens` to really see how hard we can push the algorithm.

## (100, 15)

| N             | Time (s)      |
| ------------- |:-------------:|
| 10            | 0.0103        |
| 100           | 1.1836        |
| 1,000         | 0.9789        |
| 10,000        | 11.596        |
| 100,000       | 31.439        |
| 1,000,000     | 224.88        |
| 10,000,000    | 1191.7        |

Since we are unsure if we need to do 10M, we decided to leave `max-steps = 100` and `shuffled-queens = 8`, since it gave good results and will work well on most hardware.