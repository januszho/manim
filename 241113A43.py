from manim import *

class fastsq(MovingCameraScene):
    def construct(self):
        quadrate = VGroup(*[Square(side_length=1.5, fill_opacity=0) 
                            for _ in range(9)])
        quadrate.arrange_in_grid(rows=3, cols=3, buff=0)

        self.play(Create(quadrate), run_time=0.5)
        self.wait(1)

        ecken =  [quadrate[0], quadrate[2], quadrate[6], quadrate[8]]

        dreiecke = []

        for i in ecken:
            a = i.get_corner(UL)
            b = i.get_corner(UR)
            c = i.get_corner(DL)
            d = i.get_corner(DR)
            if ecken.index(i) == 0:
                dreiecke.append(Polygon(a,b,d, color=WHITE))
                dreiecke.append(Polygon(a,c,d, color=WHITE))

            if ecken.index(i) == 1:
                dreiecke.append(Polygon(a,b,c, color=WHITE))
                dreiecke.append(Polygon(b,c,d, color=WHITE))

            if ecken.index(i) == 2:
                dreiecke.append(Polygon(a,b,c, color=WHITE))
                dreiecke.append(Polygon(b,c,d, color=WHITE))

            if ecken.index(i) == 3:
                dreiecke.append(Polygon(a,b,d, color=WHITE))
                dreiecke.append(Polygon(a,c,d, color=WHITE))

        self.play(*[SpinInFromNothing(d,angle=2 * PI) for d in dreiecke])
       
        self.wait(1)

        self.play(
            self.camera.frame.animate.set(
                width=quadrate[0].width * 4).move_to(
                    quadrate[0].get_corner(DR)),
            run_time=1
        )
        self.wait(1)

        self.play(FocusOn(quadrate[0].get_corner(DR)), run_time=1)
        self.play(FocusOn(quadrate[0].get_corner(DR)), run_time=0.75)
        self.play(FocusOn(quadrate[0].get_corner(DR)), run_time=0.5)

        self.wait(1)

        self.play(dreiecke[1].animate.set_fill(GREEN,1))
        self.play(dreiecke[0].animate.set_fill(RED,1))
        self.play(quadrate[1].animate.set_fill(ORANGE,1))
        self.play(quadrate[4].animate.set_fill(PURPLE,1))
        self.play(quadrate[3].animate.set_fill(BLUE,1))

        self.wait(1)

        self.play(
            self.camera.frame.animate.set(
                width=config.frame_width).move_to(
                    ORIGIN),
            run_time=1
        )

        self.play(
            dreiecke[2].animate.set_fill(RED,1),
            dreiecke[5].animate.set_fill(RED,1),
            dreiecke[7].animate.set_fill(RED,1)
        )

        self.play(
            dreiecke[3].animate.set_fill(GREEN,1),
            dreiecke[4].animate.set_fill(GREEN,1),
            dreiecke[6].animate.set_fill(GREEN,1)
        )

        self.play(
            quadrate[5].animate.set_fill(BLUE,1),
            quadrate[7].animate.set_fill(ORANGE,1)
        )

        self.wait(3)