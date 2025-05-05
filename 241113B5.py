from manim import *

class QuadratMitKreisen(Scene):
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
        self.play(FadeIn(a2))
        self.play(FadeIn(a3))

        # Szene für einen Moment anzeigen
        self.wait(1)

        #a3 = a3.flip()

        self.play(a3.animate.flip(axis = diagonale.get_unit_vector(), about_point = ORIGIN))

        self.wait(1)

        self.play(
            Rotate(
                a2,
                angle = -90*DEGREES,
                about_point=ORIGIN,
                rate_func=linear,
            ))

        self.wait(2)