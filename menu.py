import stdio, sys, stddraw

def main() -> None: #not a main
    stddraw.setXscale(0, 100)
    stddraw.setYscale(0, 100)
    while True:
        
        stddraw.clear()
        
        stddraw.setFontSize(20)
        stddraw.text(50, 80, "COSMIC RANGERS")
        stddraw.text(50, 60, "Press <A> to move left, Press <D> to move right")
        stddraw.text(50, 40, "Press <SPACE> to start")
    
        stddraw.show(10)
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()

            if key == ' ':
                return

            elif key == 'x':
                sys.exit()

if __name__ == "__main__": main()
