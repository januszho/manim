from manim import *

class PapierStreifen(MovingCameraScene):
    def construct(self):
        p1 = Polygon([-6,3,0], [-6,1,0], [1,1,0], [1,3,0])

        p2 = Polygon([1,3,0], [3,1,0], [3,-2,0], [1,-2,0])

        p3 = Polygon([1,3,0], [3,1,0], [6,1,0], [6,3,0])
        p3 = DashedVMobject(p3, num_dashes=50, dashed_ratio=0.5)

        self.play(Create(p1), Create(p2), Create(p3))

        self.wait(1)

        l1 = Line([-6,3,0], [3,-2,0], color=ORANGE)

        self.play(Create(l1))

        self.wait(1)

        grid = NumberPlane(
            x_range=[-15,15],
            y_range=[-10,10],
            background_line_style={
                "stroke_color": GREY,
                "stroke_opacity": 0.5,
            })

        grid.axes.set_stroke(opacity=0)

        self.play(Create(grid))

        l21 = Line([-6,3,0], [1,3,0], color=YELLOW)
        l22 = Line([1,3,0],[6,3,0], color=YELLOW)

        l2 = VGroup(l21,l22)

        self.play(Create(l2))

        t2 = MathTex("12", font_size=36, color=YELLOW)
        t2.next_to(l2, UP)

        self.play(Write(t2))

        self.wait(1)

        self.play(l22.animate.rotate(-90*DEGREES, about_point=[1,3,0]))

        self.wait(1)

        l3 = Line([1,-2,0], [3,-2,0], color=YELLOW)

        t3 = MathTex("2", font_size=36, color=YELLOW)
        t3.next_to(l3, DOWN)

        g3 = VGroup(l3,t3)
        self.play(Create(g3))

        self.wait(1)

        l41 = DashedLine([-6,3,0], [3,3,0], color=GREEN, dashed_ratio=0.8)
        l42 = DashedLine([3,3,0],[3,0,0], color=GREEN, dashed_ratio=0.8)
        l43 = DashedLine([3,0,0], [5,0,0], color=GREEN, dashed_ratio=0.8)
        l4 = VGroup(l41,l42,l43)
        d4 = Dot([5,0,0], color=GREEN)

        self.play(Create(l4))
        self.play(Create(d4))

        self.wait(1)

        self.play(FadeOut(l4))

        self.play(self.camera.frame.animate.set(width=config.frame_width * 1.5), run_time=2)
        self.wait(1)

        l51 = DashedLine([-6,3,0], [-1,3,0], color=GREEN, dashed_ratio=0.8)
        l52 = DashedLine([-1,3,0],[-1,-4,0], color=GREEN, dashed_ratio=0.8)
        l53 = DashedLine([-1,-4,0], [1,-4,0], color=GREEN, dashed_ratio=0.8)
        l5 = VGroup(l51,l52,l53)
        d5 = Dot([1,-4,0], color=GREEN)

        self.play(Create(l5))
        self.play(Create(d5))

        self.wait(1)

        self.play(FadeOut(l5))

        self.wait(1)

        l6 = DashedLine([0,-5,0], [8,3,0], color=GREEN)

        self.play(Create(l6))

        l7 = DashedLine([-6,3,0], [1,-4,0], color=GREEN)

        self.play(Create(l7))

        rw = RightAngle(l7,l6,
                        length=0.6, quadrant=(-1,-1), stroke_width=4, color=GREEN)

        self.play(Create(rw))

        self.wait(1)

        self.play(l3.animate.rotate(-90*DEGREES, about_point=[1,-2,0]))

        self.play(FadeOut(t2),FadeOut(t3))

        t4 = MathTex("7", font_size=36, color=YELLOW)
        t5 = MathTex("7", font_size=36, color=YELLOW)

        t4.next_to(l21, UP)
        t5.next_to(l22, RIGHT)

        self.play(Write(t4), Write(t5))

        rw1 = RightAngle(l21,l22,
                        length=0.6, quadrant=(-1,1), stroke_width=4, color=YELLOW)

        self.play(Create(rw1))

        self.wait(1)

        self.play(self.camera.frame.animate.set(width=config.frame_width*1.2).shift(3*LEFT+DOWN), run_time=2)
        
        self.wait(1)

        t6 = MathTex(r"\sqrt{7^2+7^2}", font_size=42, color=GREEN)
        t6.next_to(l7.get_center(),DOWN)
        w6 = angle_of_vector(l7.get_unit_vector())
        t6.rotate(w6)

        self.play(Write(t6))

        self.wait(1)

        t7 = MathTex(r"\sqrt{7^2 \times 2}", font_size=42, color=GREEN)
        t7.move_to(t6)
        t7.rotate(w6)

        self.play(ClockwiseTransform(t6,t7))

        self.wait(1)

        t7 = MathTex(r"7\sqrt{2}", font_size=42, color=GREEN)
        t7.move_to(t6)
        t7.rotate(w6)

        self.play(ClockwiseTransform(t6,t7))

        self.wait(1)

        self.play(Indicate(t6))
        self.play(Indicate(t6))
        self.play(Indicate(t6))
        self.play(Indicate(t6))

        self.wait(2)