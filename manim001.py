
# prompt: ein Vierteilkreissektor dazu ein Halbkreis im Viertelkreis in manim

from manim import *

class QuarterCircleWithHalfCircle(Scene):
    def construct(self):
        # Create the quarter circle
        quarter_circle = Sector(
            start_angle=0,
            angle=PI / 2,
            radius=4,
            color=BLUE,
            stroke_color=WHITE,
            stroke_width=4
        ).shift(LEFT * 2).shift(DOWN*2)

        # Create the half circle
        half_circle = Sector(
            start_angle=2*PI/2,
            angle=2*PI / 2,
            radius=1.78,
            stroke_color=WHITE,
            stroke_width=4
        ).shift(LEFT * 0.2).shift(DOWN*0.2)
        half_circle.set_fill(YELLOW,
                             opacity=0.5)

        line1 = Line((0,0,0),(2*1.78,1.78,0)
              ,color=RED).shift(LEFT * 2).shift(DOWN*2)

        line2 = Line((2*1.78,0,0),(2*1.78,1.78,0)
              ,color=RED).shift(LEFT * 2).shift(DOWN*2)

        line3 = Line((0,0,0),(2*1.78,0,0)
              ,color=RED).shift(LEFT * 2).shift(DOWN*2)


        # Create the semicircle within the quarter circle
        #semi_circle_in_quarter = Circle(radius=0.5).shift(UP*1)

        # Add the quarter circle and the half circle to the scene
        self.play(Create(quarter_circle))
        self.wait(1)
        self.play(Create(half_circle))
        self.wait(1)
        self.play(Create(line1))
        self.wait(1)
        self.play(Create(line2))
        self.wait(1)
        self.play(Create(line3))
        self.wait(1)

        shapes = VGroup(quarter_circle,
                        half_circle,
                        line1,
                        line2,
                        line3)

        self.play(shapes.animate.shift(LEFT*4).rotate(2*PI))

        self.play(Write(MathTex(r"\pi")))

        self.wait(1)
