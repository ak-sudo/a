m/s=(m/s**2)

ask=input("You have the value in m/s or km/h?   ")
if ask=="m/s":
    v=int(input("what is the final velocity? "))
    print(v,"m/s")
    u=int(input("what is the initial velocity?  m/s"))
    print(u,"m/s")
    t=int(input("what is the time?  s"))
    print(t,"s")

    print("Please wait....")
    Acceleration=(v-u)/t
    print("Acceleration =", Acceleration,m/s)

if ask=="km/h":
    v2=int(input("what is the final velocity?  km/h"))
    print(v2,"km/h")
    u2=int(input("what is the initial velocity?  km/h"))
    print(u2,"km/h")
    t2=int(input("what is the time?  h"))
    print(t2,"h")
    
    print("Please wait....")
    Acceleration=(v-u)/t
    print("Acceleration =", Acceleration,"km/h**2")
    print("In m/s**2")
    input()
