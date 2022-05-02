from itertools import count
from unittest import result
from fastapi import FastAPI, Header, Query
from typing import List, Optional
import uvicorn
import math
import statistics

app = FastAPI()

# http://127.0.0.1:8000/min/3?q=1&q=2&q=3&q=4&q=5&q=6
@app.get("/min/{num}")
def read_min(num: int, l: List[int] = Query(None)):

    count = 0
    for i in l:
        if i < num:
            count +=1
            print(count)

    return {"Min numbers": count}

@app.get("/max/{num}")
def read_max(num: int, l: List[int] = Query(None)):

    count = 0
 
    for i in l:
        if i > num:
            count +=1
            print(count)

    return {"Max numbers": count}

# http://127.0.0.1:8000/avg?q=1&q=2&q=3&q=4&q=5&q=6
@app.get("/avg")
def avg(l: List[int] = Query(None)):

    result = sum(l) / len(l)

    return {"AVG": result}


@app.get("/median")
def median(l: List[int] = Query(None)):

    result = statistics.median(l)
    '''q.sort()
    mid = len(q) // 2
    result = (q[mid] + q[~mid]) / 2'''

    return {"Median": result}

@app.get("/percentile/{num}")
def percentile(num: int, l: List[int] = Query(None)):

    if num > 0 and num <= 100:
        result = (num*len(l))/100
        return {"Percentile": result}
        
    return{"Give a number between 0 and 100"}


if __name__ == "__main__":

    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)
