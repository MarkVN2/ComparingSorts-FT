from time import time
from random import sample


def quicksort(v):
  if len(v) <= 1: return v    
  pivô = v[0]
  iguais  = [x for x in v if x == pivô]
  menores = [x for x in v if x <  pivô]
  maiores = [x for x in v if x >  pivô]
  return quicksort(menores) + iguais + quicksort(maiores)

def selection(v):
    r = []
    while v:
        m = min(v) 
        r.append(m)
        v.remove(m)
    return r
     
def mergesort(v):
    if len(v) <= 1: return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

t_total = 0
tam = 1000000
print(f'Size  | Merge  | Quick  | Selec  | Native')
while t_total < 30:

    v = sample(range(tam),tam)
    
    copied_v = list(v)
    
    t1 = time()
    mergesort(v)
    t2 = time()
    tm = t2-t1
    
    v = list(copied_v)
    t1 = time()
    quicksort(v)
    t2 = time()
    qt = t2 - t1
    t_total += qt   
    
    v = list(copied_v)
    t1 = time()
    v.sort() 
    t2 = time()

    nt = t2 - t1
    t_total += nt

    v = list(copied_v)
    t1 = time()
    selection(v)
    t2 = time()
    st = t2 - t1
    t_total += st

    print(f"{tam} |  {tm:.2f}  |  {qt:.2f}  | {st:.2f}  | {nt:.2f} ")
    tam = tam + 2000
