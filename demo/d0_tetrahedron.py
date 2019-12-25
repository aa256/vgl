import vgl

out_path = "out/d0.html"

v0 = vgl.vec3(0,0,1)
v1 = vgl.vec3(0,1,0)
v2 = vgl.vec3(1,0,1)
v3 = vgl.vec3(1,1,1)
V = [v0, v1, v2, v3]

shift = vgl.vec2(100,100)
p0 = vgl.vec3(1,1,0.5)
p1 = vgl.vec3(-1,1,0)
p0 = p0*(100/p0.l2())
p1 = p1*(100/p1.l2())
P = vgl.Mat(x=p0, y=p1)
print(P)

for i in range(len(V)):
    V[i] = P*V[i] + shift
[v0,v1,v2,v3] = V

l0 = vgl.Line(v0, v1)
l1 = vgl.Line(v0, v2)
l2 = vgl.Line(v0, v3)
l3 = vgl.Line(v1, v2)
l4 = vgl.Line(v1, v3)
l5 = vgl.Line(v2, v3)
L = [l0, l1, l2, l3, l4, l5]

a = vgl.vec2(0,0)
b = vgl.vec2(0,300)
c = vgl.vec2(300, 300)
d = vgl.vec2(300,0)
L.append(vgl.Line(a,b))
L.append(vgl.Line(b,c))
L.append(vgl.Line(c,d))
L.append(vgl.Line(d,a))

f = open(out_path, "w")
f.write("<html><body><svg viewBox=\"0 0 300 300\">\n")
for l in L:
    f.write(l.svg() + "\n")
f.write("</svg></body></html>\n")
f.close()
