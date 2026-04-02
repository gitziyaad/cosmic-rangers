import stdio, sys, stddraw #sys not really needed can be removed later

def main() -> None: #not a main
    stddraw.setXscale(0, 100)
    stddraw.setYscale(0, 100)
    while True:
        
        stddraw.clear()
        
        stddraw.setFontSize(20)
        stddraw.text(50, 80, "COSMIC RANGERS")
        stddraw.text(50, 60, "Press <A> to move left, Press <D> to move right")
        stddraw.text(50, 40, "Press <SPACE> to start") #controls to the game
    
        stddraw.show(10) #refreshes every 10ms
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()

            if key == ' ':
                return

            elif key == 'x':
                sys.exit() #exit game (maybe add to control list later)

if __name__ == "__main__": main()
