a = [12,2,32,4,12,45,65,34,2,1]
end = len(a) - 1
def partition(a,start,end):
    pivot = a[end]
    loc = start - 1
    for i in range (start,end):
        if a[i] <= pivot :
            loc = loc + 1
            (a[loc],a[i]) = (a[i],a[loc])
    (a[loc+1],a[end]) = (a[end],a[loc+1])
    return loc + 1

def quick_sort (a,start,end):
    if start < end :
        pi = partition(a,start,end)
        quick_sort(a,start,pi-1)
        quick_sort(a,pi+1,end)

quick_sort(a,0,end)
print (a)