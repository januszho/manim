from manim import *

class MathTableExample(Scene):
    def construct(self):
         # Define the grid's range and length
            x_range = [0, 10, 1]  # (x_min, x_max, x_step)
            y_range = [0, 8, 1]  # (y_min, y_max, y_step)
            x_length = 10  # Width of the grid
            y_length = 8  # Height of the grid

            # Create the NumberPlane
            number_plane = NumberPlane(x_range=x_range, y_range=y_range, 
                                       x_length=x_length, y_length=y_length,
                                       )
            
            
            
            # Customize the grid lines (optional)
            number_plane.background_line_style = {"color": WHITE, "stroke_width": 2}
            number_plane.faded_line_style = {"color": LIGHT_GRAY, "stroke_width": 1}
            number_plane.faded_line_ratio = 2

            #number_plane.add_coordinates()

            plane_width = number_plane.get_width()
            plane_height = number_plane.get_height()

            # Erstelle ein Rechteck mit den gleichen Abmessungen
            border = Rectangle(width=plane_width, height=plane_height)

            # Positioniere das Rechteck so, dass es die NumberPlane umrandet
            border.move_to(number_plane.get_center())

            # Füge die Umrandung zur Szene hinzu
            self.add(border)
 
            
            # Add the NumberPlane to the scene 
            self.play(FadeIn(number_plane))
            self.play(ScaleInPlace(number_plane,0.8),
                      ScaleInPlace(border, 0.8))

            #axes_to_remove = VGroup(number_plane.x_axis, number_plane.y_axis)
            #self.play(Uncreate(axes_to_remove)) 

            # Definiere Ebenenkoordinaten
            pS = [1, 5]
            pA = [8, 4]
            pB = [9, 3]
            pC = [7, 3]
            pD = [8, 2]
            pE = [9, 1]
            

            # Konvertiere Ebenenkoordinaten zu Manim-Punkten
            point1 = Dot(point=number_plane.coords_to_point(*pS), color=WHITE)
            label1 = Tex(f"S").next_to(point1, 0.5*RIGHT + 0.5*DOWN)
            self.play(Create(point1), Create(label1))

            point2 = Dot(point=number_plane.coords_to_point(*pA), color=WHITE)
            label2 = Tex(f"A").next_to(point2, 0.5* RIGHT + 0.5*UP)

            point3 = Dot(point=number_plane.coords_to_point(*pB), color=WHITE)
            label3 = Tex(f"B").next_to(point3, 0.5*RIGHT+0.5*UP)

            point4 = Dot(point=number_plane.coords_to_point(*pC), color=WHITE)
            label4 = Tex(f"C").next_to(point4, 0.5*LEFT + 0.5*DOWN)

            point5 = Dot(point=number_plane.coords_to_point(*pD), color=WHITE)
            label5 = Tex(f"D").next_to(point5, 0.5*LEFT + 0.5*DOWN)

            point6 = Dot(point=number_plane.coords_to_point(*pE), color=WHITE)
            label6= Tex(f"E").next_to(point6, 0.5*LEFT + 0.5*DOWN)

            gp = VGroup(point2, label2,
                        point3, label3,
                        point4, label4,
                        point5, label5,
                        point6, label6,)
            self.play(Create(gp))

            p1 = [0, 8]
            p2 = [0, 2]
            p3 = [4, 4]
            p4 = [6, 4] 
            p5 = [6, 0]
            p6 = [10, 8]

            line1 = Line(start=number_plane.coords_to_point(*p1),
                         end=number_plane.coords_to_point(*p3))
            line2 = Line(start=number_plane.coords_to_point(*p2),
                         end=number_plane.coords_to_point(*p3))
            line3 = Line(start=number_plane.coords_to_point(*p3),
                         end=number_plane.coords_to_point(*p4))
            line4 = Line(start=number_plane.coords_to_point(*p4),
                         end=number_plane.coords_to_point(*p6))
            line5 = Line(start=number_plane.coords_to_point(*p4),
                         end=number_plane.coords_to_point(*p5))
            
            gl = VGroup(line1, line2, line3, line4, line5)

            self.play(FadeIn(gl))

            self.wait(1)

            self.play(ShowPassingFlash(line2.copy().set_color(ORANGE),
                                       run_time=2,
                                       time_width=1))
            line2.set_color(ORANGE)

            pS1 = [3, 1]

            line6 = DashedLine(start=number_plane.coords_to_point(*pS),
                         end=number_plane.coords_to_point(*pS1),
                         color=ORANGE)
            
            self.play(Create(line6))

            self.wait(1)

            pointS1 = Dot(point=number_plane.coords_to_point(*pS1), color=ORANGE)
            labelS1 = MathTex(r"S^\prime", color=ORANGE).next_to(pointS1, 0.5*RIGHT + 0.5*DOWN)
            self.play(Create(pointS1), Create(labelS1))

            self.wait(1)

            self.play(ShowPassingFlash(line5.copy().set_color(ORANGE),
                                       run_time=2,
                                       time_width=1))
            line5.set_color(ORANGE)

            self.wait(1)

            line7 = DashedLine(start=number_plane.coords_to_point(*pS1),
                         end=number_plane.coords_to_point(*pE),
                         color=ORANGE)
            
            self.play(Create(line7))

            self.wait(1)

            self.play(Flash(label6))
            self.play(Flash(label6))
            self.play(Flash(label6))
            self.play(Flash(label6))

            self.wait(3)