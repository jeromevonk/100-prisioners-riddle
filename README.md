# 100-prisioners-riddle

This is an attempt to simulate the answer to 100 priosioners riddle, as described in this video: https://www.youtube.com/watch?v=iSNsgj1OCLA

This script uses a True Random Number Generator to create the sequences, using [random.org API](https://api.random.org/dashboard).

## General idea

To simulate this riddle with code, **we actually don't need to implement the "each prisoner enters the room" part.**
We just have to **generate the loops and check if there is any loop bigger than 50**.

* If there is, it's guaranteed that at least one prisoner would fail;
* If there is not, it's guaranteed that all prisoners would suceed.

#### Rate limit

I have commited my API key from random.org on this code, which is good for 1,000 requests per day. If it stops working, then register youself on random.org and get your own key ;)

#### Running locally
`python main.py`
