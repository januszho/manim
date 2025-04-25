from manim import *
config.background_color = LIGHT_GRAY
class c8(Scene):
    def construct(self):
        
        self.wait(2)

        kreis1 = Circle(radius=3,
                        fill_color=BLUE,
                        fill_opacity=1,
                        stroke_color=WHITE,
                        stroke_width=4) 
        kreis2 = Circle(radius=1.75,
                        fill_color=ORANGE,
                        fill_opacity=0.75,
                        stroke_color=WHITE,
                        stroke_width=4)
         
        line1 = Line((0,-3,0),(0,3,0),
                     color=WHITE,
                     stroke_width=8
                     ) 
        
        line2 = Line((1.75,-2.45,0),(1.75,2.45 ,0),
                    color=WHITE,
                    stroke_width=8
                    )
 
        self.play(Create(kreis1))
        self.play(Create(kreis2.shift(1.25*UP)))
        self.play(Create(line1))
        self.play(Create(line2))

        b2 = Brace(line2, 
                   direction=line2.copy().rotate(3* PI / 2).get_unit_vector())
        b2.set_color(BLACK)
        b2text = b2.get_tex("16")
        b2text.set_color(BLACK)

        self.play(Write(b2))
        self.play(Write(b2text))
        # Wartet für 2 Sekunden

        self.wait(2)

        self.play(FadeOut(b2,b2text))

        line5 = Line((0,0,0),(1.75,0 ,0),
                    color=PINK,
                    stroke_width=8
                    )
        line6 = Line((1.75,0,0),(3,0 ,0),
                    color=PINK,
                    stroke_width=8
                    ) 
        line7 = Line((0,0,0),(-3,0 ,0),
                    color=PINK,
                    stroke_width=8
                    ) 
        line8 = Line((1.75,0,0),(1.75,2.4,0),
                    color=PINK,
                    stroke_width=8
                    )
        line9 = Line((1.75,0,0),(1.75,-2.4,0),
                    color=PINK,   
                    stroke_width=8
                    ) 
    
        g1 = VGroup(line5,line6,line7,line8,line9)
        self.play(Create(g1))

        b5 = Brace(line5, 
                   direction=line5.copy().rotate(PI/2).get_unit_vector())
        b5.set_color(BLACK)
        b5text = b5.get_tex("r")
        b5text.set_color(BLACK)
  
        self.play(Write(b5))
        self.play(Write(b5text))

        b6 = Brace(line6, 
                   direction=line6.copy().rotate(3*PI/2).get_unit_vector())
        b6.set_color(BLACK)
        b6text = b6.get_tex("x")
        b6text.set_color(BLACK)
  
        self.play(Write(b6))
        self.play(Write(b6text)) 

        b7 = Brace(line7, 
                   direction=line7.copy().rotate( PI/2).get_unit_vector())
        b7.set_color(BLACK)
        b7text = b7.get_tex("r+x")
        b7text.set_color(BLACK)
  
        self.play(Write(b7))
        self.play(Write(b7text)) 

        b8 = Brace(line8, 
                   direction=line8.copy().rotate(3*PI/2).get_unit_vector())
        b8.set_color(BLACK)
        b8text = b8.get_tex("8")
        b8text.set_color(BLACK)
  
        self.play(Write(b8))
        self.play(Write(b8text)) 

        b9 = Brace(line9, 
                   direction=line9.copy().rotate(3*PI/2).get_unit_vector())
        b9.set_color(BLACK)
        b9text = b9.get_tex("8")
        b9text.set_color(BLACK)
  
        self.play(Write(b9))
        self.play(Write(b9text))

        self.wait(3)

        g1 = VGroup(kreis1,kreis2,line1,line2,line5,
                    line6,line7,line8,line9,
                    b5, b5text, b6,b6text, b7, b8, b9,
                    b7text, b8text, b9text)

        self.play(g1.animate.shift(3*LEFT))

        self.wait(2)

        t1 = Tex("Sehnensatz",
                 color=BLACK,
                 font_size=80)
        t1.move_to((3,2,0))
        
        self.play(Create(t1))

        self.wait(1)


        t2 = MathTex("x \cdot (r+r+x) = 8 \cdot 8",
                    color=BLACK,
                    font_size=60)
        t2.move_to((3,2,0))

        self.play(ReplacementTransform(t1,t2))

        self.wait(1)

        t3 = MathTex("2rx+x^2 = 64",
                    color=BLACK,
                    font_size=60)
        t3.move_to((3,2,0))

        self.play(ReplacementTransform(t2,t3))

        self.wait(1)

        t4 = MathTex(r"A_\bigcirc = \pi \cdot",
                     r"(r+x)^2",
                     font_size=60,
                     color=BLACK)
        t4.move_to((3,1,0))

        self.play(Create(t4))

        self.wait(1)

        t41 = MathTex(r"A_\bigcirc = \pi \cdot",
                      r" (r^2+",
                      r"2rx+x^2)",
                     font_size=60,
                     color=BLACK)
        t41.move_to((3.5,1,0))

        self.play(ReplacementTransform(t4,t41))

        self.wait(1)
 
        self.play(Wiggle(t3))
        self.play(Wiggle(t41[2]))
        g2 = VGroup(t3,t41[2])
        self.play(Wiggle(g2))
        
        self.wait(1)

        #t42 = MathTex(r"A_\bigcirc = \pi \cdot",
        #              r"(r^2+64)",
        #             font_size=60,
        #             color=BLACK)
        #t42.move_to((3,1,0))

        t42 = MathTex("64)",
                      font_size=60,
                      color=BLACK)

        self.play(ReplacementTransform(t41[2],t42.next_to(t41[1],RIGHT)))

        self.wait(1)

        t5 = MathTex(r"A_\circ = \pi \cdot r^2",
                     font_size=60,
                     color=BLACK)
        t5.next_to(t4, DOWN)

        self.play(Create(t5))

        self.wait(1)

        t6 = MathTex(r"A_\bigcirc  - A_\circ =",
                     r" \pi \cdot",
                     r" (r^2+64)",
                     r" - \pi \cdot r^2",
                     font_size=60,
                     color=BLACK)
        t6.move_to((2,-3,0))

        self.play(Create(t6))

        self.wait(1)

        t7 = MathTex(r"A_\bigcirc - A_\circ =",
                     r"\pi \cdot r^2",
                     r" + \pi \cdot 64",
                     r" - \pi \cdot r^2",
                     font_size=60,
                     color=BLACK)
        t7.move_to((2,-3,0))

        self.play(ReplacementTransform(t6,t7))

        self.wait(2)

        t7.set_color_by_tex("dot r^2",PURE_RED)
        
        g3 = VGroup(t7[1],t7[3])
        self.play(Wiggle(g3))

        self.wait(2)

        t8 = MathTex(r"A_\bigcirc - A_\circ =",
                     r" \pi \cdot 64",
                     font_size=60,
                     color=BLACK)
        t8.move_to((2,-3,0))
        
        self.play(ReplacementTransform(t7,t8))

        self.wait(2)

        t9 = MathTex(r"A_\bigcirc - A_\circ =",
                     r"64\pi",
                     font_size=60,
                     color=BLACK)
        t9.next_to(t5, DOWN)
        
        self.play(ReplacementTransform(t8,t9))

        self.wait(5)
   
   