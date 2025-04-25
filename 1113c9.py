from manim import *

class MathTableExample(Scene):
    def construct(self):
        a = Circle().set_color(BLACK).scale(0.3)
        a.set_stroke_width(0)
        t0 = MobjectTable(
            [[a.copy(),a.copy(),a.copy(),
              a.copy(),a.copy(),a.copy(),
              a.copy(),a.copy(),a.copy(),a.copy()],
            [a.copy(),a.copy(),a.copy(),
              a.copy(),a.copy(),a.copy(),
              a.copy(),a.copy(),a.copy(),a.copy()],
            [a.copy(),a.copy(),a.copy(),
              a.copy(),a.copy(),a.copy(),
              a.copy(),a.copy(),a.copy(),a.copy()],
            [a.copy(),a.copy(),a.copy(),
              a.copy(),Text("20"),Text("25"),
              a.copy(),a.copy(),a.copy(),a.copy()],
            [a.copy(),a.copy(),a.copy(),
              a.copy(),a.copy(),a.copy(),
              a.copy(),a.copy(),a.copy(),a.copy()],
            [a.copy(),a.copy(),a.copy(),
              a.copy(),a.copy(),a.copy(),
              a.copy(),a.copy(),a.copy(),a.copy()],
            [a.copy(),a.copy(),a.copy(),
              a.copy(),a.copy(),a.copy(),
              a.copy(),a.copy(),a.copy(),a.copy()]],
            include_outer_lines=True)
        t0.scale(0.7)
        self.play(DrawBorderThenFill(t0))

        self.wait(1)

        for x in range(1,4):
            for y in range(1,5):
                t0.add_highlighted_cell((x,y), color=BLUE_C)

        self.wait(1)

        for x in range(4,8):
            for y in range(1,4):
                t0.add_highlighted_cell((x,y), color=ORANGE)

        self.wait(1)

        for x in range(4,8):
            for y in range(4,7):
                t0.add_highlighted_cell((x,y), color=GREEN_C)

        self.wait(1)

        for x in range(5,8):
            for y in range(7,11):
                t0.add_highlighted_cell((x,y), color=BLUE_C )

        self.wait(1)

        for x in range(1,5):
            for y in range(5,8):
                t0.add_highlighted_cell((x,y), color=ORANGE )

        self.wait(1)
 
        for x in range(1,5):
            for y in range(8,11):
                t0.add_highlighted_cell((x,y), color=GREEN_C)

        self.wait(1)

        r1 = Rectangle(width=5.0, 
                       height=2.5,
                       fill_color=WHITE,
                       fill_opacity=0.75)
        
        r1.move_to((-4,2,0))
        
        t1 = Text("0", font_size=200, color=BLACK)
        t1.move_to((-4,2,0))

        self.play(Create(r1))
        self.play(Write(t1))

        self.wait(1)

        r2 = Rectangle(width=3.6, 
                       height=3.5,
                       fill_color=WHITE,
                       fill_opacity=0.75)
        
        r2.move_to((-4.7,-1.5,0))

        t2 = Text("0", font_size=200, color=BLACK)
        t2.move_to((-4.7,-1.5,0))

        self.play(Create(r2))
        self.play(Write(t2))

        r3 = Rectangle(width=3.6, 
                       height=3.5,
                       fill_color=WHITE,
                       fill_opacity=0.75)
        
        r3.move_to((4.7,1.5,0))

        t3 = Text("0", font_size=200, color=BLACK)
        t3.move_to((4.7,1.5,0))

        self.play(Create(r3))
        self.play(Write(t3))
        

        r4 = Rectangle(width=5.0, 
                       height=2.5,
                       fill_color=WHITE,
                       fill_opacity=0.75)
        
        r4.move_to((4,-2,0))
        
        t4 = Text("0", font_size=200, color=BLACK)
        t4.move_to((4,-2,0))

        self.play(Create(r4))
        self.play(Write(t4))
    
        r5 = Rectangle(width=2.5, 
                       height=0.8,
                       fill_color=WHITE,
                       fill_opacity=0.75)
        
        r5.move_to((0,0,0))
        
        t5 = Text("45", font_size=50, color=BLACK)
        t5.move_to((0,0,0))

        self.play(Create(r5))
        self.play(Write(t5))
 
        p1 = Polygon([-1.25, 3.3, 0], 
                     [2.6, 3.3, 0], 
                     [2.6, -0.4, 0],
                     [1.45, -0.4, 0],
                     [1.45, 0.57, 0],
                     [-1.25, 0.57, 0],
                     fill_color=WHITE,
                     fill_opacity=0.75,
                     stroke_width=0)
        
        t6 = Tex("-45", font_size=175, color=BLACK)
        t6.move_to((0.5,2,0))

     
        self.play(Create(p1))
        self.play(Write(t6))

        p2 = p1.copy()
        p2.rotate(angle=PI)
        p2.move_to((-0.68,-1.48,0))
        
        t7 = Tex("-45", font_size=175, color=BLACK)
        t7.move_to((-1,-2,0))

     
        self.play(Create(p2))
        self.play(Write(t7))

        self.play(FadeOut(t5,t6))

        self.wait(4)