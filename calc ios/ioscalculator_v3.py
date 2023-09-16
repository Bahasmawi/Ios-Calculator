from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from math import*
app=QApplication([])

def plus():
    w.res.setText(w.res.text()+"+")
    w.affiche.setText("")
    
def moin():
    w.res.setText(w.res.text()+"-")
    w.affiche.setText("")
def fois():
    w.res.setText(w.res.text()+"*")
    w.affiche.setText("")
def sur():
    w.res.setText(w.res.text()+"/")
    w.affiche.setText("")

        
def egale():
    ch=w.res.text()
    s=round(eval(ch),2)
    w.affiche.setText(str(s))
def ac():
    w.res.setText("0")
    w.affiche.setText("0")
def k1():
    w.res.setText(w.res.text()+"(")
    w.affiche.setText("")
def k2():
    w.res.setText(w.res.text()+")")
    w.affiche.setText("")
def power():
    w.res.setText(w.res.text()+"**")
    w.affiche.setText("")
def div():
    w.res.setText(w.res.text()+"//")
    w.affiche.setText("")
def mod():
    w.res.setText(w.res.text()+"%")
    w.affiche.setText("")
def c():
    ch=w.res.text()
    w.res.setText(ch[:-1])
    w.affiche.setText("")
def b0():
    ch=w.res.text()
    if ch!="0":
        ch=w.res.text()+"0"
        w.affiche.setText(w.affiche.text()+"0")
    else:
        ch="0"
        w.affiche.setText("0")
    w.res.setText(ch)
def b1():
    ch=w.res.text()
    if ch!="0":
        ch=w.res.text()+"1"
        if ch[-1] in ["+","-","*","/"]:
            w.affiche.setText("1")
        else:
            w.affiche.setText(w.affiche.text()+"1")
    else:
        
        ch="1"
        w.affiche.setText("1")
    w.res.setText(ch)
def b2():
    ch=w.res.text()
    if ch!="0":
        ch=w.res.text()+"2"
        w.affiche.setText(w.affiche.text()+"2")
    else:
        ch="2"
        w.affiche.setText("2")
    w.res.setText(ch)
def b3():
    ch=w.res.text()
    if ch!="0":
        ch=w.res.text()+"3"
        w.affiche.setText(w.affiche.text()+"3")
    else:
        ch="3"
        w.affiche.setText("3")
    w.res.setText(ch)
def b4():
    ch=w.res.text()
    if ch!="0":
        ch=w.res.text()+"4"
        w.affiche.setText(w.affiche.text()+"4")
    else:
        ch="4"
        w.affiche.setText("4")
    w.res.setText(ch)
def b5():
    ch=w.res.text()
    if ch!="0":
        ch=w.res.text()+"5"
        w.affiche.setText(w.affiche.text()+"5")
    else:
        ch="5"
        w.affiche.setText("5")
    w.res.setText(ch)
def b6():
    ch=w.res.text()
    if ch!="0":
        ch=w.res.text()+"6"
        w.affiche.setText(w.affiche.text()+"6")
    else:
        ch="6"
        w.affiche.setText("6")
    w.res.setText(ch)
def b7():
    ch=w.res.text()
    if ch!="0":
        ch=w.res.text()+"7"
        w.affiche.setText(w.affiche.text()+"7")
    else:
        ch="7"
        w.affiche.setText("7")
    w.res.setText(ch)
def b8():
    ch=w.res.text()
    if ch!="0":
        ch=w.res.text()+"8"
        w.affiche.setText(w.affiche.text()+"8")
    else:
        ch="8"
        w.affiche.setText("8")
    w.res.setText(ch)
def b9():
    ch=w.res.text()
    if ch!="0":
        ch=w.res.text()+"9"
        w.affiche.setText(w.affiche.text()+"9")
    else:
        ch="9"
        w.affiche.setText("9")
    w.res.setText(ch)

w=loadUi("ioscalculator_v3.ui")
w.show()
w.plus.clicked.connect(plus)
w.moin.clicked.connect(moin)
w.fois.clicked.connect(fois)
w.sur.clicked.connect(sur)
w.ac.clicked.connect(ac)
w.egale.clicked.connect(egale)
w.k1.clicked.connect(k1)
w.k2.clicked.connect(k2)
w.div.clicked.connect(div)
w.mod.clicked.connect(mod)
w.c.clicked.connect(c)
w.power.clicked.connect(power)
w.b1.clicked.connect(b1)
w.b2.clicked.connect(b2)
w.b3.clicked.connect(b3)
w.b4.clicked.connect(b4)
w.b5.clicked.connect(b5)
w.b6.clicked.connect(b6)
w.b7.clicked.connect(b7)
w.b8.clicked.connect(b8)
w.b9.clicked.connect(b9)
w.b0.clicked.connect(b0)
#solver

def b0_2():
    ch=w.r.text()
    w.r.setText(ch+"0")

def b1_2():
    ch=w.r.text()
    w.r.setText(ch+"1")
def b2_2():
    ch=w.r.text()
    w.r.setText(ch+"2")
def b3_2():
    ch=w.r.text()
    w.r.setText(ch+"3")
def b4_2():
    ch=w.r.text()
    w.r.setText(ch+"4")
def b5_2():
    ch=w.r.text()
    w.r.setText(ch+"5")
def b6_2():
    ch=w.r.text()
    w.r.setText(ch+"6")
def b7_2():
    ch=w.r.text()
    w.r.setText(ch+"7")
def b8_2():
    ch=w.r.text()
    w.r.setText(ch+"8")
def b9_2():
    ch=w.r.text()
    w.r.setText(ch+"9")
def plus_2():
    w.r.setText(w.r.text()+"+")
def moin_2():
    w.r.setText(w.r.text()+"-")
def x():
    w.r.setText(w.r.text()+"x")
def xsquare():
    w.r.setText(w.r.text()+"x²")
def c_2():
    ch=w.r.text()
    w.r.setText(ch[:-1])
def ac_2():
    w.r.setText("")
def find_coef(ch):
    if ch[0]!="-":
        ch="+"+ch
    posx2=ch.find("x²")
    a=int(ch[:posx2])
    ch=ch[posx2+2:]
    print("a=",a)
    posx=ch.find("x")
    b=int(ch[:posx])
    ch=ch[posx+1:]
    print("b=",b)
    c=int(ch)
    print("c=",c)
    return a,b,c
def find_delta(a,b,c):
    d=(b**2)-(4*a*c)
    return d
def solution(a,b,c,D):
    x1=(-b-sqrt(D))/(2*a)
    x2=(-b+sqrt(D))/(2*a)
    return x1,x2
def solve():
    ch=w.r.text()
    a,b,c=find_coef(ch)
    D=find_delta(a,b,c)
    x1,x2=solution(a,b,c,D)
    x1=str(verif(x1))
    x2=str(verif(x2))
    w.x1.setText(x1)
    w.x2.setText(x2)
def verif(x):
    if round(x)==x:
        return int(x)
    else:
        return round(x,2)
w.plus_2.clicked.connect(plus_2)
w.moin_2.clicked.connect(moin_2)
w.x.clicked.connect(x)
w.xsquare.clicked.connect(xsquare)
w.c_2.clicked.connect(c_2)
w.ac_2.clicked.connect(ac_2)
w.solve.clicked.connect(solve)
w.b1_2.clicked.connect(b1_2)
w.b2_2.clicked.connect(b2_2)
w.b3_2.clicked.connect(b3_2)
w.b4_2.clicked.connect(b4_2)
w.b5_2.clicked.connect(b5_2)
w.b6_2.clicked.connect(b6_2)
w.b7_2.clicked.connect(b7_2)
w.b8_2.clicked.connect(b8_2)
w.b9_2.clicked.connect(b9_2)
w.b0_2.clicked.connect(b0_2)

app.exec_()
