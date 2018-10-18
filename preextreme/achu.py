bx , by = map(int , raw_input().split())
ix ,iy = map(int , raw_input().split())
steps = 0
for _ in range(input()):
    cx , cy = map(int , raw_input().split())
    nx , ny = ix + cx , iy + cy
    if(nx > bx or ny > by or nx < (-1 * bx) or ny < (-1 * by) ):continue
    steps += max(abs(cx) , abs(cy))
print steps

#works
