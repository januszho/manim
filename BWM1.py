from manim import *
import numpy as np

class DreieckMitKoordinaten(MovingCameraScene):
    def construct(self):
        # Definiere die Koordinaten der Eckpunkte
        punkt_a = np.array([0, 0, 0])
        punkt_b = np.array([4, 0, 0])
        punkt_c = np.array([3, 2, 0])
        
        punkt_a1 = np.array([8, 0, 0])
        punkt_b1 = np.array([2, 4, 0])
        punkt_c1 = np.array([-3, -2, 0])

        # Erstelle das Dreieck mit den definierten Punkten
        mein_dreieck = Polygon(punkt_a, punkt_b, punkt_c, color=GREEN, fill_opacity=0.7)
        
        mein_dreieck1 = Polygon(punkt_a1, punkt_b1, punkt_c1, color=BLUE, fill_opacity=0.7)
        

        # Erstelle Punkte an den Eckpunkten zur besseren Visualisierung (optional)
        dot_a = Dot(punkt_a, color=RED)
        dot_b = Dot(punkt_b, color=RED)
        dot_c = Dot(punkt_c, color=RED)

        dot_a1 = Dot(punkt_a1, color=RED,fill_opacity=1)
        dot_b1 = Dot(punkt_b1, color=RED,fill_opacity=1)
        dot_c1 = Dot(punkt_c1, color=RED,fill_opacity=1)
        
        self.wait(2)

        i1 = Text("Bundeswettbewerb Mathematik 1978, 1. Runde, Aufgabe 4",
                  color=WHITE,
                  font_size=32)
        i1.to_edge(UP)
        self.play(Write(i1))
        
        self.wait(1)
        i2 = Text("Im Dreieck ABC wird A an B, B an C und C an A gespiegelt.",
                  color=WHITE,
                  font_size=32)
        i3 = Text("Man konstruiere das Dreieck ABC aus den gespiegelten Punkten.",
                  color=WHITE,
                  font_size=32)
        i2.next_to(i1, 2*DOWN)
        i3.next_to(i2,DOWN)

        self.play(Write(i2),Write(i3))
        self.wait(1)

       
        self.wait(5)

        self.play(FadeOut(i1,i2,i3))

        self.wait(1)
        self.camera.frame.move_to(mein_dreieck.get_center_of_mass())

        dreieck=VGroup(mein_dreieck, dot_a, dot_b, dot_c)
        #dreieck.move_to(ORIGIN)

        dreieck1=VGroup(mein_dreieck1, dot_a1, dot_b1, dot_c1)
        #dreieck1.move_to(ORIGIN)
        dreieck1.set_z_index(-1)
        mein_dreieck1.set_z_index(-6)

        # Zeige das Dreieck und die Punkte/Beschriftungen auf dem Bildschirm
       

        self.play(Create(dreieck))
        self.wait(1)

        l1 = DashedLine(dot_a.copy().shift((-2,0,0)), dot_a1, color=ORANGE)
        self.play(Create(l1))
        self.play(Create(dot_a1))

        l2 = DashedLine(dot_b.copy().shift((0.5,-1,0)), dot_b1, color=ORANGE)
        self.play(Create(l2))
        self.play(Create(dot_b1))

        l3 = DashedLine(dot_c.copy().shift((1.5,1,0)), dot_c1, color=ORANGE)
        self.play(Create(l3))
        self.play(Create(dot_c1)) 

        l1.set_z_index(5)
        l2.set_z_index(5)
        l3.set_z_index(5)

        self.wait(1)

        self.play(FadeIn(mein_dreieck1))
        self.wait(1)

        la = Line(dot_b1, dot_c1)

        in1 = line_intersection([l1.get_start(), l1.get_end()], [la.get_start(), la.get_end()])

        dot_in1 = Dot(in1, color=RED,fill_opacity=1)

        self.play(Create(dot_in1))

        self.wait(1)

        ll = DashedLine(dot_a, dot_b1, color=ORANGE)
        self.play(Create(ll))

        self.wait(1)

        t1 = Text("1", color=WHITE, font_size=50)
        t1.move_to(mein_dreieck.get_center_of_mass())
        self.play(Wiggle(mein_dreieck))
        self.play(Write(t1))

        self.wait(1)
        
        d2 = Polygon(punkt_a, punkt_c, punkt_b1, color=BLUE, fill_opacity=0.5)
        t12=t1.copy()
        d2.set_z_index(-1)
        self.play(Wiggle(d2))
        self.play(Write(t12.move_to(d2.get_center_of_mass()+UP+0.3*RIGHT)))

        self.wait(1)
        t11 = t1.copy()
        d3 = Polygon(punkt_c1, punkt_a, punkt_b1, color=BLUE, fill_opacity=0.5)
        d3.set_z_index(-1)
        self.play(Wiggle(d3))
        self.play(Write(t11.move_to(d3.get_center_of_mass())))

        self.wait(1)

        #self.play(FadeOut(d2,d3))

        #self.wait(1)

        d5 = Polygon(punkt_a, in1, punkt_c1, color=ORANGE, fill_opacity=0.5)
        d5.set_z_index(-1)
        self.play(Wiggle(d5))
        t3 = Text("x", color=YELLOW, font_size=30)
        self.play(Write(t3.move_to(d5.get_center_of_mass())))

        self.wait(1)

        l4 = DashedLine(in1, punkt_c, color=ORANGE)
        self.play(Create(l4))

        self.wait(1)

        d6 = Polygon(punkt_a, in1, punkt_c, color=ORANGE, fill_opacity=0.5)
        d6.set_z_index(-1)
        self.play(Wiggle(d6))
        t4 = Text("x", color=YELLOW, font_size=30)
        self.play(Write(t4.move_to(d6.get_center_of_mass())))

        self.wait(1)

        d7 = Polygon(in1, punkt_c, punkt_b1, color=ORANGE, fill_opacity=0.5)
        d7.set_z_index(-1)
        self.play(Wiggle(d7))
        t5 = Text("x+1", color=YELLOW, font_size=30)
        self.play(Write(t5.move_to(d7.get_center_of_mass())))

        self.wait(1)

        t6 = Text("3x+1",color=YELLOW, font_size=30)
        t6.move_to((-3,2,0))

        g1 = VGroup(t3,t4,t5)

        self.play(g1.animate.become(t6))

        self.wait(1)

        self.play(FadeOut(d7,d6,d5,l4))

        self.wait(1)

        g2 = VGroup(t11,t12)

        t7 = Text(" = 2", color=YELLOW, font_size=30)
        t7.next_to(t6,RIGHT)
        self.play(g2.animate.become(t7))

        self.wait(1)

        t8 = Text("x = 1/3", color=YELLOW, font_size=30)
        t8.move_to(t6)
        g3 = VGroup(g1,g2)
        self.play(g3.animate.become(t8))

        self.wait(1)

        t9 = Text("1/3", color=YELLOW, font_size=24)
        t9.move_to(d5.get_center_of_mass())
        self.play(g3.animate.become(t9))

        self.wait(1)

        t10 = Text("2/3", color=YELLOW, font_size=24)
        d8 = Polygon(in1, punkt_a, punkt_b1)
        t10.move_to(d8.get_center_of_mass())
        self.play(Write(t10))

        self.wait(1)

        l5 = Line(punkt_c1, in1, color=WHITE, stroke_width=4)
        b5 = Brace(l5,
                   direction=l5.copy().rotate(PI/2).get_unit_vector())
        b5.set_color(WHITE)

        t5 = Text("a", color=WHITE, font_size=32)
        t5.next_to(b5,LEFT).shift(0.8*RIGHT+0.3*UP)
    
        self.play(Create(l5))
        self.play(FadeIn(b5), Write(t5))

        self.wait(1)

        l6 = Line(in1, punkt_b1, color=WHITE, stroke_width=4)
        b6= Brace(l6,
                   direction=l6.copy().rotate(PI/2).get_unit_vector())
        b6.set_color(WHITE)

        t6 = Text("2a", color=WHITE, font_size=32)
        t6.next_to(b6,LEFT).shift(1.7*RIGHT+0.4*UP)
    
        self.play(Create(l6))
        self.play(FadeIn(b6), Write(t6))

        self.wait(2)
