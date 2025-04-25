from manim import *
config.background_color = LIGHT_GRAY
class c8(Scene):
    def construct(self):
        # Erzeugt ein gleichseitiges Dreieck
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
        b2.set_color(WHITE)
        b2text = b2.get_tex("16")
        b2text.set_color(WHITE)

        self.play(Write(b2))
        self.play(Write(b2text))
        # Wartet für 2 Sekunden

        self.wait(2)

        self.play(FadeOut(b2,b2text))

        self.play(kreis2.animate.move_to(ORIGIN))

        line5 = Line((1.75,0,0),(1.75,2.4 ,0),
                    color=PINK,
                    stroke_width=8
                    )

        self.play(Create(line5))

        b5 = Brace(line5, 
                   direction=line5.copy().rotate(3*PI/2).get_unit_vector())
        b5.set_color(BLACK)
        b5text = b5.get_tex("8")
        b5text.set_color(BLACK)
  
        self.play(Write(b5))
        self.play(Write(b5text))

        self.wait(3)

        self.play(FadeOut(b5, b5text))

        g1 = VGroup(kreis1,kreis2,line1,line2,line5)

        self.play(g1.animate.shift(3*LEFT))

        self.wait(2)

        line6 = Line((1.75,0,0),(1.75,2.4 ,0),
                    color=PINK,
                    stroke_width=8
                    ).shift(RIGHT)
        
     
        self.play(Create(line6))

        self.play(Rotate(line5,
                         angle=2*PI,
                         about_point=(-3,0,0)),
                  Rotate(line6,
                         angle=2*PI,
                         about_point=(2.75,0,0)),
                         run_time=4)

        self.wait(1)
        
        s1 = Sector(radius=2.4,
                    angle=-360 *DEGREES,
                    start_angle=90*DEGREES)
        s1.move_to([2.75, 0, 0])
        s1.set_color(PINK)

        self.play(Create(s1), run_time=3)

        line7 = Line((1.75,0,0),(1.75,2.4 ,0),
                    color=BLACK,
                    stroke_width=8
                    ).shift(RIGHT)
        
        self.play(Create(line7))

        b7 = Brace(line7, 
                   direction=line5.copy().rotate(3*PI/2).get_unit_vector())
        b7.set_color(BLACK)
        b7text = b7.get_tex("8")
        b7text.set_color(BLACK)

        self.play(Write(b7))
        self.play(Write(b7text))

        t1 = MathTex("A = \pi 8^2", 
                     font_size=72,
                     color=BLACK)
        t1.move_to((2.75,-1,0))
        
        t2 = MathTex("A = 64 \pi", 
                     font_size=72,
                     color=BLACK)
        t2.move_to((2.75,-1,0))

        self.play(Create(t1))
        self.wait(2)
        self.play(ReplacementTransform(t1,t2))
        self.wait(5) 
   
   