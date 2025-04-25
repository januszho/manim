from manim import *
config.background_color = GRAY
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

        line3 = Line((0,0,0),(1.75,0 ,0),
                    color=PINK,
                    stroke_width=8
                    )
        
        line4 = Line((0,0,0),(1.75,2.4 ,0),
                    color=PINK,
                    stroke_width=8
                    )

        line5 = Line((1.75,0,0),(1.75,2.4 ,0),
                    color=PINK,
                    stroke_width=8
                    )

        self.play(Create(line3))
        self.play(Create(line4))
        self.play(Create(line5))

        b3 = Brace(line3, 
                   direction=line3.copy().rotate(3*PI/2).get_unit_vector())
        b3.set_color(BLACK)
        b3text = b3.get_tex("r")
        b3text.set_color(BLACK )

        self.play(Write(b3))
        self.play(Write(b3text))

        b4 = Brace(line4, 
                   direction=line4.copy().rotate(PI/2).get_unit_vector())
        b4.set_color(BLACK)
        b4text = b4.get_tex("R")
        b4text.set_color(BLACK)

        self.play(Write(b4))
        self.play(Write(b4text))

        b5 = Brace(line5, 
                   direction=line5.copy().rotate(3*PI/2).get_unit_vector())
        b5.set_color(BLACK)
        b5text = b5.get_tex("8")
        b5text.set_color(BLACK)
  
        self.play(Write(b5))
        self.play(Write(b5text))

        self.wait(2)

        text1 = MarkupText("R<sup>2</sup> = r<sup>2</sup> + 8<sup>2</sup>",
                           font_size=36)
        text2 = MarkupText("R<sup>2</sup> - r<sup>2</sup> = 64",
                           font_size=36)

        g2 = VGroup(text1,text2)
        g2.move_to((5,3,0))

        g2.arrange(DOWN, center=False, aligned_edge=LEFT)

        self.play(Create(g2))
        self.wait(2)

        text3 = MarkupText('A<span foreground="blue"><sub>●</sub></span> = π • R<sup>2</sup>',
                           font_size=36)
        text4 = MarkupText('A<span foreground="orange"><sub>●</sub></span> = π • r<sup>2</sup>',
                           font_size=36)
        text5 = MarkupText('A<sub>?</sub> = A<span foreground="blue"><sub>●</sub></span> - A<span foreground="orange"><sub>●</sub></span>',
                           font_size=36)
        text6 = MarkupText('A<sub>?</sub> = πR<sup>2</sup> - πr<sup>2</sup>',
                           font_size=36)
        text7 = MarkupText('A<sub>?</sub> = π(R<sup>2</sup> - r<sup>2</sup>)',
                           font_size=36)

        g3 = VGroup(text3,text4, text5, text6, text7)
        g3.move_to((5,1,0))

        g3.arrange(DOWN, center=False, aligned_edge=LEFT)
        
        self.wait(2)

        self.play(Write(g3))

        #self.wait(2)

        self.play(Wiggle(text2,
                         scale_value=1.5,
                         n_wiggles=24,
                         run_time=4),
                         run_time=4)
        
 
        text8 = MarkupText("A<sub>?</sub> = π • 64",
                           font_size=36)
        
        text8.move_to((5,-3,0))
        self.play(Write(text8))

        self.wait(1)
        text9 = MarkupText("A<sub>?</sub> = 64π",
                           font_size=36)
        text9.move_to((5,-3,0))
        self.play(Transform(text8,text9))

        self.wait(2)
  
   