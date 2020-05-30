class Print_Alpha:

    def a(self):
        for i in range(1,11):
            for j in range(1,11):
                if (i in [1,5] or j in [1,10]):
                    print("*",end='')
                else:
                    print(' ',end='')
            print()
    def b(self):
        for i in range(1,11):
            for j in range(1,11):
                if (i in [1,5,10] or j in [1,10]):
                    print("*",end='')
                else:
                    print(' ',end='')
            print()
    def c(self):
        for i in range(1,11):
            for j in range(1,11):
                if (i in [1,10] or j in [1]):
                    print("* ",end='')
                else:
                    print('',end='')
            print()
    def d(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i in [1,10] or j in [3,10]):
                    print("*",end='')
                else:
                    print(' ',end='')
            print()
    def e(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i in [1,5,10] or j==3):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def f(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i in [1,5] or j in [3]):
                    print('*',end='')

                else:
                    print(' ',end='')
            print()

    def g(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i==1 or j==1 or (i==10 and j in list(range(1,6))) or (j==5 and i in list(range(5,10))) or ( j in range(5,11) and i==5) or (j==10 and i in list(range(5,11))) ):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def h(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i==5 or j in [1,10]):
                    print('*',end='')

                else:
                    print(' ',end='')
            print()
    def i(self):
        for I in range(1,11):
            for j in range(1,11):
                if(I in [1,10] or j==5):
                    print('*',end='')

                else:
                    print(' ',end='')
            print()
    def j(self):
        for i in range(1,11):
            for J in range(1,11):
                if(i==1 or J==5 or (i==10 and J in list(range(1,6)))or (J==1 and i in list(range(7,11)))):
                    print('*',end='')

                else:
                    print(' ',end='')
            print()
    def k(self):
        for i in range(1,11):
            for j in range(1,11):
                if((j==1 and i in list(range(1,7))) or ((i,j) in [(1,4),(2,3),(3,2),(4,2),(5,3),(6,4)])):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def l(self):
        for i in range(1,11):
            for j in range(1,11):
                if(j==1 or i==10 or (j==10 and i in range(9,11))):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def n(self):
        for i in range(1,11):
            for j in range(1,11):
                if(j==1 or j==10 or i==j):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def o(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i in [1,10] or j in [1,10]):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def p(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i in [1,5] or j==2 or (j==10 and i in list(range(1,6)))):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def m(self):
        for i in range(1,11):
            for j in range(1,11):
                if(j in [1,10] or (i==j and i<=5) or (i==11-j and i<=5)):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()   
    def u(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i==10 or j in [1,10]):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def t(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i==1 or j==5):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()  
    def s(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i in [1,10,5] or ( j==1 and i in list(range(1,6))) or (j==10 and i in list(range(5,11)))):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def z(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i  in [1,10] or j==11-i):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def r(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i in [1,5] or j==2 or (j==10 and i in list(range(1,6))) or (i==j and i>=5)):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def w(self):
        for i in range(1,11):
            for j in range(1,11):
                if(j in [1,10] or(i==j and i>=5) or (j==11-i and i>5)):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def x(self):
        for i in range(1,11):
            for j in range(1,11):
                if(i==j or j==11-i):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def y(self):
        for i in range(1,11):
            for j in range(1,11):
                if((i==j and i<=5) or (j==11-i)):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def v(self):
        for i in range(1,11):
            for j in range(1,11):
                if((i==j and i<=5) or (j==11-i and i<=5)):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
    def q(self):
        for i in range(1,11):
            for j in range(1,11):
                if((i in [1,10] or j in [1,10]) or (i==j and i>=5)):
                    print('*',end='')
                else:
                    print(' ',end='')
            print()
            