from manim import *

class KreisDreiecke2(Scene):
    def construct(self):
        kreis = Circle(radius=3.5, color=BLUE)

        self.wait(2)

        self.play(Create(kreis))

        punkte = VGroup()

        for i in range(12): 
            punkt = Dot([3.5,0,0], 
                        color=ORANGE).rotate(30*i*DEGREES, 
                                             about_point=ORIGIN)
            punkte.add(punkt)

        self.play(Rotate(punkte,105*DEGREES, rate_func=smoothererstep))

        self.wait(1)

        self.add(Dot(ORIGIN, color=ORANGE))

        self.wait(1)

        d1 = Polygon(punkte[1].get_center(),
                     punkte[4].get_center(),
                     ORIGIN)
        
        self.play(Create(d1))

        self.wait(1)

        rw = RightAngle(Line(punkte[1].get_center(), ORIGIN),
                        Line(punkte[4].get_center(),ORIGIN),
                        color=BLUE,
                        length=0.4, quadrant=(-1,-1), stroke_width=4)
        
        self.play(Create(rw))

        self.wait(1)

        self.play(FadeOut(rw))

        x = [5,6,7,8,9,10,11,0]
        
        for i in x:
            d2 = Polygon(punkte[1].get_center(),
                     punkte[4].get_center(),
                     punkte[i].get_center())
            self.play(Transform(d1, d2))

        self.wait(1.5)

        d3 = Polygon(punkte[1].get_center(),
                     punkte[4].get_center(),
                     ORIGIN)
        
        self.play(Transform(d1, d3))

        self.wait(1)

        for _ in range(12):
            self.play(
                Rotate(
                    d1, 30*DEGREES, about_point=ORIGIN, run_time=0.6
            )           
            )
            self.wait(0.4)

        self.wait(1)
            
        d4 = Polygon(punkte[1].get_center(),
                     punkte[4].get_center(),
                     punkte[7].get_center())
        
        self.play(Transform(d1, d4))

        self.wait(1)

        self.play(FadeOut(d1))
        self.wait(1)

        d5 = Polygon(punkte[4].get_center(),
                     punkte[7].get_center(),
                     punkte[1].get_center())
        
        self.play(Create(d5), run_time=2)

        self.wait(1)

        self.play(Indicate(d5))
        self.play(Indicate(d5))
        self.play(Indicate(d5))

        for i in range(12):
            self.play(
                Rotate(
                    d5, 30*DEGREES, about_point=ORIGIN, run_time=0.6
            )           
            )
            self.wait(0.4)

        self.wait(3)