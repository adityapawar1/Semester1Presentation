from manim import (
    BLUE,
    LEFT,
    PURPLE,
    Create,
    Dot,
    DrawBorderThenFill,
    FadeIn,
    Line,
    MathTex,
    NumberPlane,
    Scene,
    VGroup,
    Write,
    RED,
)
import numpy as np


class ArcLengthProofScene(Scene):
    @staticmethod
    def fx(x: float):
        return -(x**2) + 5

    def construct(self):
        plane = NumberPlane(
            x_range=[-6, 6, 1], y_range=[-5, 9], x_length=15, y_length=10
        )

        plane.add_coordinates()

        axes_label = plane.get_axis_labels("x", "f(x)")

        graph = plane.plot(self.fx, color=PURPLE)
        # graph_label = plane.get_graph_label(graph, MathTex("f(x)=-x^2+5"))

        # graph_group = VGroup(graph, graph_label)

        self.play(DrawBorderThenFill(plane), Write(axes_label))
        self.play(Create(graph), run_time=2)
        # self.play(Write(graph_label))
        self.wait()

        x0, x1 = 0, -2
        point0 = plane.c2p(x0, self.fx(x0))
        point1 = plane.c2p(x1, self.fx(x1))

        dot1 = Dot(point0, color=RED)
        dot2 = Dot(point1, color=RED)
        arc_line = Line(point0, point1)
        distance_label = MathTex("d=\sqrt{x^2+y^2}").next_to(arc_line, LEFT, buff=0.2)

        self.play(FadeIn(dot1, dot2))
        self.play(FadeIn(arc_line))
        self.play(Write(distance_label))
