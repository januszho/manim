from manim import *

class KreisDreiecke(Scene):
    def construct(self):
        kreis = Circle(3, BLUE)
        self.wait(2)
        self.play(GrowFromCenter(kreis))

        punkte = VGroup()

        for i in range(12): 
            punkt = Dot([3,0,0], 
                        color=ORANGE).rotate(30*i*DEGREES, 
                                             about_point=ORIGIN)
            punkte.add(punkt)

        self.play(Rotate(punkte,105*DEGREES, rate_func=smoothererstep))

        self.add(Dot(ORIGIN, color=ORANGE))

        self.wait(1)

        d1 = Polygon(punkte[1].get_center(),
                     punkte[4].get_center(),
                     ORIGIN, 
                     color=GREEN,
                     fill_color=GREEN,
                     fill_opacity=0.3)
        
        rw = RightAngle(Line(punkte[1].get_center(), ORIGIN),
                        Line(punkte[4].get_center(),ORIGIN),
                        color=GREEN,
                        length=0.4, quadrant=(-1,-1), stroke_width=4)

        self.play(Create(d1))
        self.play(Create(rw))

        self.wait(2)

        self.play(Uncreate(rw))

        dg = VGroup()

        x = [5,6,7,8,9,10,11,0]
        for i in x:

            dg.add(Polygon(punkte[1].get_center(),
                     punkte[4].get_center(),
                     punkte[i].get_center(),
                     color=GREEN,
                     fill_color=GREEN,
                     fill_opacity=0.2)
            )
            

        self.play(Transform(d1, dg[0]))
        self.wait(2)
        self.play(Create(dg[1:11]), run_time=4)

        self.wait(2)

        self.play(FadeOut(d1), FadeIn(dg[0]))

        for i in range(12):
            self.play(
                Rotate(dg, 30*DEGREES, about_point=ORIGIN, run_time=0.6/(i/4+1))
            )
            self.wait(0.4/(i/4+1))

        dg1 = dg.copy()
        dg1.set_fill(color=PURPLE)
        dg1.set_stroke(color=PURPLE)

        self.play(FadeIn(dg1))

        for i in range(3):
            self.play(
                Rotate(dg1, 30*DEGREES, about_point=ORIGIN, run_time=0.6/(i/4+1))
            )
            self.wait(0.4/(i/4+1))

        d2 = Polygon(punkte[1].get_center(),
                     punkte[4].get_center(),
                     punkte[7].get_center(),
                     color=RED,
                     fill_color=RED,
                     fill_opacity=0.2)
        
        self.wait(1)
            
        self.play(Create(d2))

        self.wait(1)

        self.play(Indicate(d2), run_time=1)
        self.play(Indicate(d2), run_time=0.75)
        self.play(Indicate(d2), run_time=0.5)

        self.play(FadeOut(dg), FadeOut(dg1))

        self.wait(1)

        for i in range(12):
            self.play(
                Rotate(d2, 30*DEGREES, about_point=ORIGIN, run_time=0.6/(i/4+1))
            )
            self.wait(0.4/(i/4+1))

        self.wait(4)