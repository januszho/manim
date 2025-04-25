from manim import *

class mk1113c8(Scene):
    def construct(self):
        self.wait(1)
        hexagon = RegularPolygon(n=6, radius=3, color=GREEN)
        self.play(Create(hexagon))
        self.wait(1)

        # Zugriff auf die Eckpunkte
        vh = hexagon.get_vertices()
        
        xp=0.5

        d1 = Polygon(vh[1], vh[2], [xp,vh[4][1],0],
                     color=BLUE) 

        self.play(FadeIn(d1))

        self.play(d1.animate.set_fill(color=BLUE, opacity=0.6))

        t1 = MathTex(r"64", color=WHITE).move_to(d1.get_center_of_mass())
        self.play(Write(t1))


        d2 = Polygon(vh[0], vh[1], [xp,vh[4][1],0],
                     color=BLUE) 

        self.play(FadeIn(d2))

        self.play(d2.animate.set_fill(color=BLUE, opacity=0.6))

        t2 = MathTex(r"42", color=WHITE).move_to(d2.get_center_of_mass())
        self.play(Write(t2))

        d3 = Polygon(vh[2], vh[3], [xp,vh[4][1],0],
                     color=BLUE) 

        self.play(FadeIn(d3))

        self.play(d3.animate.set_fill(color=BLUE, opacity=0.6))

        t3 = MathTex(r"?", color=WHITE).move_to(d3.get_center_of_mass())
        self.play(Write(t3))

        l1 = Line(start=vh[2], end=vh[4],
                  color=ORANGE)
        
        self.play(Create(l1))

        l2 = Line(start=vh[1], end=vh[5],
                  color=ORANGE)
        
        self.play(Create(l2))

        l3 = Line(start=vh[3], end=vh[0],
                  color=ORANGE)
        
        self.play(Create(l3))

        self.wait(1)

        d11 = Polygon(vh[1], vh[2], vh[5],
                     color=BLUE,
                     fill_color=ORANGE,
                     fill_opacity=0.6) 
        


        self.play(d1.animate.become(d11),
                  t1.animate.move_to(d11.get_center_of_mass()))

        d4 = Polygon([xp,vh[4][1],0], vh[5], vh[0],
                     color=BLUE,
                     fill_color=ORANGE,
                     fill_opacity=0.6) 
        
        d5 = Polygon([xp,vh[4][1],0], vh[3], vh[4],
                     color=BLUE,
                     fill_color=ORANGE,
                     fill_opacity=0.6) 
        
        self.play(FadeIn(d4,d5))

        self.wait(1)

        d41 = Polygon([xp,vh[4][1],0], vh[5], [vh[1][0],vh[0][1],0],
                     color=BLUE,
                     fill_color=ORANGE,
                     fill_opacity=0.6) 
        
        d51 = Polygon([xp,vh[4][1],0], [vh[2][0],vh[0][1],0], vh[4],
                     color=BLUE,
                     fill_color=ORANGE,
                     fill_opacity=0.6) 
        
        self.play(d4.animate.become(d41),
                  d5.animate.become(d51))
        
        self.play(FadeOut(d2,d3,t2,t3))
        self.wait(1)

        self.play(FadeOut(d4,d5))

        d12 = Polygon(vh[1], vh[2], vh[4], vh[5],
                     color=BLUE,
                     fill_color=ORANGE,
                     fill_opacity=0.6) 
        
        t2 = MathTex(r"128", color=WHITE).move_to(d12.get_center_of_mass())

        self.play(d1.animate.become(d12),
                  t1.animate.become(t2))

        self.wait(1)

        d13 = Polygon(vh[1], vh[2], [vh[2][0],vh[0][1],0], [vh[1][0],vh[0][1],0],
                     color=BLUE,
                     fill_color=ORANGE,
                     fill_opacity=0.6) 
        
        t3 = MathTex(r"64", color=WHITE).move_to(d13.get_center_of_mass())

        self.play(d1.animate.become(d13),
                  t1.animate.become(t3))
        
        self.wait(1)

        self.play(FadeIn(d4,d5))

        self.wait(1)

        d42 = Polygon(vh[5], vh[5], vh[5],
                     color=BLUE,
                     fill_color=ORANGE,
                     fill_opacity=0.6) 
        
        d52 = Polygon(vh[5], [vh[2][0],vh[0][1],0], vh[4],
                     color=BLUE,
                     fill_color=ORANGE,
                     fill_opacity=0.6) 
        
        self.play(d4.animate.become(d42),
                  d5.animate.become(d52))
        
        t4 = MathTex(r"32", color=WHITE).move_to(d5.get_center_of_mass())

        self.play(FadeOut(l3))

        self.play(Write(t4))


        d53 = Polygon(vh[5], vh[3], vh[4],
                     color=BLUE,
                     fill_color=ORANGE,
                     fill_opacity=0.6) 
        
        self.play(d5.animate.become(d53),
                  t4.animate.move_to(d53.get_center_of_mass()))
        
        d54 = Polygon(vh[4], vh[2], vh[3],
                     color=BLUE,
                     fill_color=ORANGE,
                     fill_opacity=0.6) 
        
        self.wait(1)

        self.play(d5.animate.become(d54),
                  t4.animate.move_to(d54.get_center_of_mass()))
        
        self.wait(1)
        
        self.play(d1.animate.become(d12),
                  t1.animate.become(t2))
        
        d6 = Polygon(vh[0], vh[1], vh[5],
                     color=BLUE,
                     fill_color=ORANGE,
                     fill_opacity=0.6) 
        
        t6 = MathTex(r"32", color=WHITE).move_to(d6.get_center_of_mass())

        self.play(FadeIn(d6,t6))

        self.wait(1)

        h2 = RegularPolygon(n=6, radius=3, color=BLUE,
                            fill_color=ORANGE, fill_opacity=0.6)
        
        t7 = MathTex(r"192", color=WHITE).move_to(h2.get_center_of_mass())
        
        self.play(Create(h2), Write(t7),
                  FadeOut(d6,d5,t4,t6,d1,t1,l1,l2))
        
        self.wait(2)

        d1 = Polygon(vh[1], vh[2], [xp,vh[4][1],0],
                     color=BLUE) 

        self.play(FadeIn(d1))

        self.play(d1.animate.set_fill(color=BLUE, opacity=0.6))

        t1 = MathTex(r"64", color=WHITE).move_to(d1.get_center_of_mass())
        self.play(Write(t1))


        d2 = Polygon(vh[0], vh[1], [xp,vh[4][1],0],
                     color=BLUE) 

        self.play(FadeIn(d2))

        self.play(d2.animate.set_fill(color=BLUE, opacity=0.6))

        t2 = MathTex(r"42", color=WHITE).move_to(d2.get_center_of_mass())
        self.play(Write(t2))

        d3 = Polygon(vh[2], vh[3], [xp,vh[4][1],0],
                     color=BLUE) 

        self.play(FadeIn(d3))

        self.play(d3.animate.set_fill(color=GREEN, opacity=0.6))

        t3 = MathTex(r"?", color=WHITE).move_to(d3.get_center_of_mass())
        self.play(Write(t3))

        d4 = Polygon([xp,vh[4][1],0], vh[5], vh[0],
                     color=BLUE,
                     fill_color=BLUE,
                     fill_opacity=0.6) 
        
        d5 = Polygon([xp,vh[4][1],0], vh[3], vh[4],
                     color=BLUE,
                     fill_color=BLUE,
                     fill_opacity=0.6) 
        
        t8 = MathTex(r"32", color=WHITE).move_to((0,-3,0))

        self.play(FadeIn(d4,d5),Write(t8))

        t31 = MathTex(r"192").move_to(d3.get_center_of_mass())

        t9 = t7.copy()

        self.play(t9.animate.move_to(d3.get_center_of_mass()), 
                  t3.animate.become(t31))
        
        self.wait(1)

        self.play(FadeOut(t7,t9))

        t9 = t1.copy()

        t32 = MathTex(r"128").move_to(d3.get_center_of_mass())
        self.play(t9.animate.move_to(d3.get_center_of_mass()), 
                  t3.animate.become(t32))
        
        self.play(FadeOut(t9,t1))

        self.wait(1)

        t9 = t2.copy()

        t32 = MathTex(r"86").move_to(d3.get_center_of_mass())
        self.play(t9.animate.move_to(d3.get_center_of_mass()), 
                  t3.animate.become(t32))
        
        self.play(FadeOut(t9,t2))

        t9 = t8.copy()

        t32 = MathTex(r"54").move_to(d3.get_center_of_mass())
        self.play(t9.animate.move_to(d3.get_center_of_mass()), 
                  t3.animate.become(t32))
        
        self.play(FadeOut(t9,t8))

        self.wait(1)

        self.play(Flash(t3))
        self.play(Flash(t3))
        self.play(Flash(t3))
        self.play(Flash(t3))
        
        self.wait(4)