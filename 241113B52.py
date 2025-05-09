from manim import *

class QuadratMitKreisen2(Scene):
    def construct(self):
        # Seitenlänge des Quadrats
        seitenlaenge = 6

        # Quadrat erstellen
        quadrat = Square(side_length=seitenlaenge)

        # Diagonale erstellen
        diagonale = Line(quadrat.get_corner(DL), 
                         quadrat.get_corner(UR))

        # Mittelpunkt der unteren Seite des Quadrats
        mittelpunkt_unten = quadrat.get_bottom()

        # Halbkreis erstellen
        radius_halbkreis = seitenlaenge / 2
        halbkreis = Sector(radius=radius_halbkreis, 
                           angle=180*DEGREES,
                           arc_center=mittelpunkt_unten)
        halbkreis.set_fill(opacity=0)
        halbkreis.set_stroke(color = WHITE, 
                             width = 4)
        
        #halbkreis = Circle(radius=radius_halbkreis, arc_center=mittelpunkt_unten)

        # Mittelpunkt des Viertelkreises (untere linke Ecke des Quadrats)
        mittelpunkt_viertelkreis = quadrat.get_corner(DL)

        # Viertelkreis erstellen
        radius_viertelkreis = seitenlaenge
        viertelkreis = Sector(radius=radius_viertelkreis, 
                           angle=90*DEGREES,
                           arc_center=mittelpunkt_viertelkreis)
        viertelkreis.set_fill(opacity=0)
        viertelkreis.set_stroke(color = WHITE, 
                             width = 4)
        
        #Circle(radius=radius_viertelkreis, arc_center=mittelpunkt_viertelkreis) # Quadrant unten rechts

        self.wait(2)

        # Alle Objekte zur Szene hinzufügen
        self.play(Create(quadrat), run_time=1)
        self.play(Create(diagonale), run_time=1)
        self.play(Create(halbkreis), run_time=1)
        self.play(Create(viertelkreis), run_time=1)

        ls = Polygon(quadrat.get_corner(DL), 
                     quadrat.get_corner(UL),
                     quadrat.get_corner(UR))
        a1 = Difference(ls, viertelkreis, color=LIGHT_GRAY, fill_opacity=1)
        a2 = Intersection(ls, halbkreis, color=LIGHT_GRAY, fill_opacity=1)
        a3 = Difference(viertelkreis, halbkreis)
        a3 = Difference(a3, ls, color=LIGHT_GRAY, fill_opacity=1)

        self.play(FadeIn(a1))
        self.play(FadeIn(a3))
        self.play(FadeIn(a2))

        self.wait(1)
        self.play(FadeOut(a2), FadeOut(a3), FadeOut(halbkreis))
        self.wait(1)
        self.play(Wiggle(quadrat))

        t1 = Text("6 * 6", color=WHITE, font_size=32)
        t1.to_edge(UR)
        t11 = Text("36", color=WHITE, font_size=32)
        t11.move_to(t1)

        self.play(Write(t1))
        self.play(ReplacementTransform(t1, t11))
        self.wait(1)
        self.play(Wiggle(viertelkreis))

        t2 = Text("1/4 * Pi * 6²", color=WHITE, font_size=32)
        t2.next_to(t1, DOWN)
        t2.shift(LEFT)

        self.play(Write(t2))
        self.wait(1)

        t21 = Text("9 * Pi", color=WHITE, font_size=32)
        t21.move_to(t2)
        t21.shift(RIGHT)

        self.play(ReplacementTransform(t2, t21))

        self.wait(1)

        g1 = VGroup(t11, t21)
        t3 = Text("1/2 (36 - 9 * Pi)", color=WHITE, font_size=32)
        t3.move_to(t11).shift(LEFT)

        self.play(ReplacementTransform(g1, t3))
        self.wait(1)

        self.play(FadeOut(a1), FadeIn(halbkreis), FadeIn(a2))

        l1 = Line(ORIGIN, quadrat.get_corner(DR), color=WHITE)

        self.play(Create(l1))

        l2 = DashedLine(ORIGIN, quadrat.get_bottom(), color=WHITE)

        self.play(Create(l2))
        self.wait(1)
        self.play(Wiggle(halbkreis))

        d1 = Polygon(quadrat.get_corner(DL), quadrat.get_corner(DR), ORIGIN)
        d1.set_color(WHITE)

        self.add(d1)
        self.play(Wiggle(d1))

        t4 = Text("1/2 (1/2 * Pi * 3²)", color=WHITE, font_size=32)
        t4.next_to(t3, DOWN)

        t5 = Text("1/2 * 3 * 3", color=WHITE, font_size=32)
        t5.next_to(t4, DOWN)

        self.play(Write(t4), Write(t5))
        self.wait(1)
        
        t6 = Text("1/4 * 9 * Pi - 1/2 * 9", color=WHITE, font_size=32)
        t6.move_to(t4)

        g2 = VGroup(t4, t5)

        self.play(ReplacementTransform(g2, t6))
        self.wait(2)
        self.play(FadeOut(a2), FadeOut(l2))
        self.play(GrowFromCenter(a3))
        self.wait(1)

        achtelkreis = Sector(radius=radius_viertelkreis, 
                           angle=45*DEGREES,
                           arc_center=mittelpunkt_viertelkreis)
        achtelkreis.set_fill(opacity=0)
        achtelkreis.set_stroke(color = WHITE, 
                             width = 4)
        
        self.add(achtelkreis)
        self.play(Wiggle(achtelkreis))
        self.play(Wiggle(d1))

        a4 = a2.copy().set_fill(opacity=0)
        a4.flip(axis=UP, about_point = ORIGIN)

        self.add(a4)
        self.play(Wiggle(a4))

        t7 = Text("1/8 * 36 * Pi", color=WHITE, font_size=32)
        
        t8 = Text("-1/2(1/2 * 9 * Pi - 9)", color=WHITE, font_size=32)

        t9 = Text("-9", color=WHITE, font_size=32)

        text_group = VGroup(t7, t8, t9)

        text_group.arrange(DOWN, buff=0.2)
        text_group.next_to(t6, DOWN)
        # buff ist der Abstand zwischen den Objekten

        # Optional: Positioniere die gesamte Gruppe
        # text_group.to_edge(UP) # Positioniert die Gruppe am oberen Rand
        # text_group.center()    # Zentriert die Gruppe

        self.play(Write(text_group))
        self.wait(1)

        t10 = Text("2.25 Pi - 4.5", color=WHITE, font_size=32)
        t10.next_to(t6, DOWN)

        self.play(ReplacementTransform(text_group, t10))  
        self.wait(1)

        t11 = Text("-4.5 Pi + 18", color=WHITE, font_size=32)
        t11.move_to(t3)

        t12 = Text("2.25 Pi - 4.5", color=WHITE, font_size=32)
        t12.move_to(t6)
        
        self.play(FadeIn(a1), FadeIn(a2), FadeOut(l1), FadeOut(d1), FadeOut(a4), FadeOut(achtelkreis))
        self.wait(1)
        self.play(ReplacementTransform(t3, t11))
        self.wait(1)
        self.play(ReplacementTransform(t6, t12))
        self.wait(1)

        g3 = VGroup(t10, t11, t12)

        t13 = Text("9", color=WHITE, font_size=32).move_to(t6)

        self.play(ReplacementTransform(g3, t13))
        self.play(Flash(t13))
        self.play(Flash(t13))
        self.play(Flash(t13))
        self.play(Flash(t13))
        

        self.wait(2)