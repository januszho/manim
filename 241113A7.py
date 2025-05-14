from manim import *

class KanguruAufgabe(Scene):
    def construct(self):
        self.wait(2)
        t1 = MathTex(r"16^{15}+16^{15}+16^{15}+16^{15}").scale(2)

        self.play(Write(t1))

        self.wait(1)

        t2 = MathTex(r"4 \times 16^{15}").scale(2)

        self.play(ClockwiseTransform(t1, t2))

        self.wait(1)

        t3 = MathTex(r"4 \times 4^{2^{15}}").scale(2)

        self.play(Transform(t1, t3))

        self.wait(1)

        t4 = MathTex(r"4", r"\times 4^{2 \times 15}").scale(2)

        self.play(Transform(t1, t4))

        self.wait(1)

        t5 = MathTex(r"4", r"\times 4^{30}").scale(2)

        self.play(Transform(t1[1], t5[1].next_to(t1[0], RIGHT)))

        self.wait(1)

        t6 = MathTex(r"4^1", r"\times 4^{30}").scale(2)

        self.play(Transform(t1[0], t6[0].next_to(t1[1], LEFT)))

        self.wait(1)

        t7 = MathTex(r"4^{31}").scale(2)

        self.play(Transform(t1, t7))

        self.wait(3)